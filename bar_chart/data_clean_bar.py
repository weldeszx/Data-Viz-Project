import pandas as pd

df=pd.read_csv('data.csv')

#trim data for bar chart
df_bar=df.loc[:,['abbv','date_cer','ncs','pts','sps','hhas','c_sqr']]

#calculate total avg_sqr
#df_avg_sqr=df_bar.groupby('abbv').agg({'c_sqr':'mean'}).round(2)
#df_avg_sqr.columns=['avg_sqr']

#count service by state
def service_count(df,pts='NO',sps='NO',hhas='NO',name='test.json'):
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
    #df_final.to_json(name)
    return df_final

df_all=service_count(df_bar,'YES','YES','YES','bar_all.json')
df_none=service_count(df_bar,'NO','NO','NO','bar_none.json')
df_pts=service_count(df_bar,'YES','NO','NO','bar_pts.json')
df_sps=service_count(df_bar,'NO','YES','NO','bar_sps.json')
df_hhas=service_count(df_bar,'NO','NO','YES','bar_hhas.json')
df_pts_sps=service_count(df_bar,'YES','YES','NO','bar_pts_sps.json')
df_pts_hhas=service_count(df_bar,'YES','NO','YES','bar_pts_hhas.json')
df_sps_hhas=service_count(df_bar,'NO','YES','YES','bar_sps_hhas.json')
