__author__= "LingoPros"

from Config import Config
import praw
import datetime

def get_time(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

redditConfig = Config()

reddit = redditConfig.getReddit()



for submission in reddit.subreddit("nomansskythegame").top(limit=2):
        print(submission.title)  # Output: the submission's title
        print(submission.score)  # Output: the submission's score
        print(submission.id)     # Output: the submission's ID
        print(submission.url)    # Output: the URL the submission points to
                                 # or the submission's URL if it's a self post
        
        print(get_time(submission))
        print()
        

