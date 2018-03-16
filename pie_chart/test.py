import pandas as pd

df=pd.read_csv('data.csv')

#pie chart
df_pie=df.loc[:,['abbv','date_cer','ncs','pts','sps','hhas','c_sqr']]

states_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def pie_count(state,df=df_pie):
    state=state.upper()
    if not (state in states_list):
        return 'error'
    df=df.loc[df['abbv']==state,:]
    label=['type 1','type 2','type 3','type 4','type 5','type 6','type 7','type 8']
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
    return data






print(pie_count('tx'))
