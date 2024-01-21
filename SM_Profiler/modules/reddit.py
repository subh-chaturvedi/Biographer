import praw #reddit API library
import json
import pandas as pd
import jsonProfileWriter as jpw #to write to the json profile

# Reading the API keys from json file
keys = open('./SM_Profiler/API_Keys/api_keys.json')
keys_data = json.load(keys)

# Read-only instance of reddit
reddit = praw.Reddit(client_id=keys_data["reddit"]["client_id"],        
                               client_secret=keys_data["reddit"]["client_secret"],      
                               user_agent=keys_data["reddit"]["user_agent"])        

print("Connect to Reddit API Successful!!!")

allSubreddits = []

# Find all the subreddits the user has commented in
#TODO:change predefined user to variable and convert the whole instance to callable function
for comment in reddit.redditor("subhchatu").comments.new(limit=500):
    #print(comment.subreddit)
    allSubreddits.append(comment.subreddit.display_name)

#convert list recieved to a dataframe and then sort & filter to only get top 10 with more than 10 comments
allSub = pd.DataFrame(allSubreddits,columns = ['Subs'])
subreddit_counts=allSub['Subs'].value_counts()
subreddit_counts = subreddit_counts[subreddit_counts > 10]

#convert the dataframe to a list to push into json and also print for debugging
top_10_subreddits = subreddit_counts.head(10)
top_10_subreddits_list = top_10_subreddits.index.tolist()
print("List of most used subreddits",top_10_subreddits_list)

#convert into dictionary and push into json using JPW module
subs = {"subreddit_interests":top_10_subreddits_list}
jpw.writeSMRecord("test4",subs)