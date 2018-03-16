import pandas as pd
import flask
import json

df=pd.read_csv('data.csv')

#set app
app = flask.Flask(__name__)

#bar chart
df_bar=df.loc[:,['abbv','date_cer','ncs','pts','sps','hhas','c_sqr']]

def service_count(df,pts='NO',sps='NO',hhas='NO'):
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
    df_final=df_final.reset_index().drop(['index'],axis=1)
    return df_final

@app.route('/')
def homepage():
     return flask.render_template('index.html')

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
    df=service_count(df_bar,pts=pts,sps=sps,hhas=hhas)
    df=df.to_dict()
    return flask.jsonify(df)



#run
if __name__ == '__main__':
    app.run(debug=True)
