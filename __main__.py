__author__= "LingoPros"

from Config import Config
import praw
import datetime
import operator

def get_time(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

redditConfig = Config()

reddit = redditConfig.getReddit()

def main():
    subreddits = {}

    for submission in reddit.front.top(limit=1000):
        '''
        print(submission.title)  # Output: the submission's title
        print(submission.score)  # Output: the submission's score
        print(submission.id)     # Output: the submission's ID
        print(submission.url)    # Output: the URL the submission points to
                                 # or the submission's URL if it's a self post
        print(submission.author)
        print(submission.subreddit)
        print(get_time(submission))'''

        subreddit_name = submission.subreddit.display_name
        if subreddit_name not in subreddits:
            subreddits[subreddit_name] = 1
        else:
            subreddits[subreddit_name] += 1

    print(subreddits)
    sorted_subs = sorted(subreddits.items(), key = operator.itemgetter(1))
    sorted_subs.reverse()
    print(sorted_subs)



def get_time(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)





main()


