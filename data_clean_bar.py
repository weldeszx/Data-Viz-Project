import pandas as pd

df=pd.read_csv('data.csv')
df=df.loc[:,['abbv','date_cer','ncs','pts','sps','hhas','c_sqr']]



print(df.head())
