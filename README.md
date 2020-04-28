### Aim

The aim of this project is to determine Big-5 personality traits of indian celebrities on the basis of their twitter history.

### Process:

**Step 1** 
The first requirement was data of the indian celebrities names and their twitter handles. To gather this data we used web scraping. The data was scraped from [socialsamosa.com](http://www.socialsamosa.com/). The code can be found in ```Scraping\twitter_list\twitter_list\spiders.handles.py```

**Step 2**
The next step was fetching the tweets from the twitter handles gathered in previous step. Twitter API was used for fetching the tweets. Maximum of 150 tweets were gathered per user. Its code can be found in ```tweets_api.py```. The results (i.e. tweets) were stores in text files.

**Step 3**
The next step was using these text files to determine the traits. These files were passes to the IBM Cloud API. IBM Watson's Personality Insights was used. The output received from cloud was in the form of .json file. So it was parsed down and the results were appropriately stored in ```actor_personality.csv```. The values for personality traits can be found for each celebrity against their name in the mentioned csv file.

**Note**
Inclusion of images was attempted but could not be performed because of lack of time and depreciation of most libraries/modules suitable for automating the task (like ```google_images_download``` module). The idea was to automate the downloading of images, convert them to array using ```img_to_array``` and store them in the csv file.



