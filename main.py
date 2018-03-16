import pandas as pd
import flask
import json

df=pd.read_csv('data.csv')

#set app
app = flask.Flask(__name__)

@app.route('/')
def homepage():
     return flask.render_template('index.html')

#bar chart
df_bar=df.loc[:,['abbv','date_cer','ncs','pts','sps','hhas','c_sqr']]

def bar_count(df,pts='NO',sps='NO',hhas='NO'):
    df['count']=(df.pts==pts)&(df.sps==sps)&(df.hhas==hhas)
    df_avgsqr=df.loc[df['count'],:]
    df_avgsqr=df_avgsqr.groupby('abbv').agg({'c_sqr':'mean'})
    df_avgsqr.columns=['avg_sqr']
    df_avgsqr=df_avgsqr.reset_index()
    df_count=df.groupby('abbv').agg({'count':'sum'})
    df_count=df_count['count'].astype(int).reset_index()
    df_final=df_count.merge(df_avgsqr,how='outer',on='abbv')
    df_final=df_final.sort_values('count',ascending=False)
    df_final['avg_sqr']=df_final['avg_sqr'].round(2)
    return df_final

@app.route('/bar/<name>')
def get_bar_data(name='pts_sps_hhas'):
    name=name.split('_')
    (pts,sps,hhas) = ('NO','NO','NO')
    if ('pts' in name):
        pts='YES'
    if ('sps' in name):
        sps='YES'
    if ('hhas' in name):
        hhas='YES'
    df=bar_count(df_bar,pts=pts,sps=sps,hhas=hhas)
    df['count']=df['count'].astype(str)
    df['avg_sqr']=df['avg_sqr'].astype(str)
    df=df.set_index('abbv')
    df=df.to_dict()
    return flask.jsonify(df)

#pie chart
df_pie=df.loc[:,['abbv','date_cer','ncs','pts','sps','hhas','c_sqr']]

states_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

@app.route('/pie/<state>')
def get_pie_data(state):
    state=state.upper()
    if not (state in states_list):
        return 'error'
    df=df_pie.loc[df_pie['abbv']==state,:]
    label=['None','PTS','SPS','HHAS','PTS+SPS','PTS+HHAS','SPS+HHAS','PTS+SPS+HHAS']
    all_no=df.loc[(df['pts']=='NO')&(df['sps']=='NO')&(df['hhas']=='NO'),:].shape[0]
    pts=df.loc[(df['pts']=='YES')&(df['sps']=='NO')&(df['hhas']=='NO'),:].shape[0]
    sps=df.loc[(df['pts']=='NO')&(df['sps']=='YES')&(df['hhas']=='NO'),:].shape[0]
    hhas=df.loc[(df['pts']=='NO')&(df['sps']=='NO')&(df['hhas']=='YES'),:].shape[0]
    pts_sps=df.loc[(df['pts']=='YES')&(df['sps']=='YES')&(df['hhas']=='NO'),:].shape[0]
    pts_hhas=df.loc[(df['pts']=='YES')&(df['sps']=='NO')&(df['hhas']=='YES'),:].shape[0]
    sps_hhas=df.loc[(df['pts']=='NO')&(df['sps']=='YES')&(df['hhas']=='YES'),:].shape[0]
    pts_sps_hhas=df.loc[(df['pts']=='YES')&(df['sps']=='YES')&(df['hhas']=='YES'),:].shape[0]
    data={label[0]:all_no, label[1]:pts, label[2]:sps, label[3]:hhas, label[4]:pts_sps,
         label[5]:pts_hhas,label[6]:sps_hhas, label[7]:pts_sps_hhas}
    return flask.jsonify(data)

#run
if __name__ == '__main__':
    app.run(debug=True)
