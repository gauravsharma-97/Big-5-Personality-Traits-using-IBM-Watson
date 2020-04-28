from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import json
import os
from os.path import join, dirname
import pandas as pd
from csv import writer

API_Key='Hidden'
url='Hidden'

authenticator_IAM = IAMAuthenticator(API_Key)
personality_insights = PersonalityInsightsV3(
    version='2020-04-28',
    authenticator=authenticator_IAM
)

personality_insights.set_service_url(url)

#cols=["big5_openness", "big5_conscientiousness", "big5_extraversion", "big5_agreeableness", "big5_neuroticism"]
#col_datas=[]

pos=0
        
try:
    # Invoke a Personality Insights method
    #files=os.listdir('Tweets Texts')
    #pos=3
    df=pd.read_csv('twitter_handles_list.csv')
    df=df['Name'].values.tolist()
    
    for file in df[pos:]:
         path=join('Tweets Texts', (file+'.txt'))
         pos+=1
         if os.path.exists(path):
             
             with open(path, 'rb') as profile_txt:
                 print(path+"---> "+file)
                 profile = personality_insights.profile(
                     profile_txt,
                     'application/json',
                     content_type='text/plain', 
                     consumption_preferences=True,
                     raw_scores=False
                     ).get_result()
                 profile_txt.close()
                 tmp=[] #tmp is a list for a single row
                 tmp.append(file)
                 
                 for i in range(5):
                     tmp.append(str(profile['personality'][i]['percentile']))
                
                 with open("actor_personality.txt", "a") as fp:
                     wr = writer(fp, dialect='excel')
                     wr.writerow(tmp)
                     fp.close()   
                  
except ApiException as ex:
    print("pos= "+df[pos]+" "+";; "+"Method failed with status code " + str(ex.code) + ": " + ex.message)

