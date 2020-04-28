import json
import tweepy
import pandas as pd

consumer_key = 'Hidden'
consumer_secret = 'Hidden'
access_token = 'Hidden'
access_token_secret = 'Hidden'

lst=[]


def get_tweets(name, username):
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        print("Running for "+username)
        number_of_tweets=15
        tweets = api.user_timeline(screen_name=username, count=150, exclude_replies=True, include_rts=False)
        
        f=open(name+".txt", "w+")
        for tweet in tweets:
            f.write(tweet.text.encode('utf-8')+'\n\n')
        f.close()
        

    except tweepy.TweepError:
         print(">>>>>>>>>>>>>>>>>>>>Failed to run the command on "+username+", Skipping...<<<<<<<<<<<<<<<<<<<<<<<<")
         lst.append(username)
    
    print('\n--------------------------------------------------\n')

if __name__=="__main__":
    df=pd.read_csv('twitter_handles_list.csv')
    actor_names=df['Name'].values.tolist()
    handles_list=df['Twitter Handle'].values.tolist()
    for i in range(0, 199):
       get_tweets(actor_names[i], handles_list[i])
    print(lst)

