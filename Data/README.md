# Data Set Information
Here is a list of our current data sets and their information:

hot1000_data- 1000 posts from the frontpage of reddit r/all <br/>
hot100_data- 100 posts from the frontpage of reddit r/all <br/>
hot10_data- 10 posts from the frontpage of reddit r/all <br/>
top1000_data- 1000 posts from the frontpage of reddit r/all
top100_data- 100 posts from the frontpage of reddit r/all
top10_data- 10 posts from the frontpage of reddit r/all

For every post gathered in the above data sets this information is collected:

title- The title of the post
score- The overall score of the post (upvotes-downvotes)
id- The unique id given to the post
author- The reddit user who created the post
subreddit- The subreddit that the post originated from
created- The time that has elapsed from UTC to the time of creation
url- The url link that was attached to the post

# How to reproduce our data sets or create your own data sets:
### Step 1: Configure PRAW with personal data for __main__.py
1. Inside the same directory as __main__.py create a Config folder.
2. Create a Config.py file inside the Config folder
3. Create a __init__.py file inside the Config folder
4. Visit PRAW documentation on Configuration here: https://praw.readthedocs.io/en/latest/getting_started/configuration/reddit_initialization.html
5. Set up the Config.py file according to the below template filling in with your personal information:



```
import praw

class Config:

    def __init__(self):
        self.reddit = praw.Reddit(client_id='SI8pN3DSbt0zor',
                             client_secret='xaxkj7HNh8kwg8e5t4m6KvSrbTI',
                             password='1guiwevlfo00esyy',
                             user_agent='testscript by /u/fakebot3',
                             username='fakebot3')

    def getReddit(self):
        return self.reddit

```
6. Set up the __init__.py file with this same information:
```
from .Config import Config
```
7. Once you have valid configuration setup you can test to see if it's working

8. While in the same directory as __main__.py run the following command:
```
python __main__.py
```
9. Then open the Data folder and view the data sets you should have just created.

10. If any errors occured they should be displayed in the command line or the JSON files are not properly formatted. Only errors should be from improper configuration so repeat Step 1 and use PRAW documentation to fix them.
