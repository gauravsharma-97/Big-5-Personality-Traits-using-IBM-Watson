#Getting list of names
import pandas as pd

df=pd.read_csv('twitter_handles_list.csv')
names=df['Name'].values.tolist()

#Downloading images
import flickrapi
import urllib
from PIL import Image

key='728fc6d41df2cb8f20b9f34ab11fddf7'
secret='f49a3862638b9169'
# Flickr api access key 

flickr=flickrapi.FlickrAPI(key, secret, cache=True)

for name in names:
	photo = flickr.photos.search(text=name, tag_mode='all', extras='url_m, url_q',  per_page=1, sort='relevance')    
	url = photo.get('url_m, url_q')
	#urllib.urlretrieve(url, name)
	#image = Image.open(name) 
	#image = image.resize((256, 256), Image.ANTIALIAS)
	#image.save(name)




