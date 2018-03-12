import pandas as pd
import glob

def combine_csv(path):
    df_list = []
    for loc_csv in glob.glob(path):
        df = pd.read_csv(loc_csv)
        df_list.append(df)
    df = pd.concat(df_list)
    return df

#merge individual csv
df_loc=combine_csv('location/*.csv')
df_agency=combine_csv('agency/*.csv')
df_provider=combine_csv('provider/*.csv')

#change column names
df_loc=df_loc.loc[:,['LocationNO','Country','State_Abbv','State','County','City','ZipCode']]
df_loc.columns=['loc_no','country','abbv','state','county','city','zipcode']

df_agency=df_agency.loc[:,['state', 'LocationNO', 'Certification_NO', 'Address',
       'LicenseRenewalDate', 'Offers Nursing Care Services',
       'Offers Physical Therapy Services', 'Offers Speech Pathology Services',
       'Offers Home Health Aide Services', 'Date Certified', 'Service Quality',
       'ServiceQualityRating', 'Type of Ownership']]
    #lrd=LicenseRenewalDate,
    #ncs=Offers Nursing Care Services
    #pts=Offers Physical Therapy Services
    #sps=Offers Speech Pathology Services
    #hhas=Offers Home Health Aide Services
    #sq=Service Quality
    #sqr=ServiceQualityRating
df_agency.columns=['state', 'loc_no', 'cer_no', 'address', 'lrd', 'ncs',
       'pts', 'sps','hhas', 'date_cer', 'sq','sqr', 'ownership']

df_provider=df_provider.loc[:,['CertificationNO', 'Provider Name', 'State']]
df_provider.columns=['cer_no','name','abbv']

#merge all csv
df=df_agency.merge(df_provider,how='inner', on='cer_no')
df=df.merge(df_loc,how='inner',on=['loc_no','abbv','state'])
df=df.loc[:,['country','state', 'abbv','county','city','address','zipcode','loc_no',
             'name','cer_no','date_cer', 'ownership','lrd', 'ncs', 'pts', 'sps',
             'hhas', 'sq', 'sqr']]

df.to_csv('data.csv',index=False)
