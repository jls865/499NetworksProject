# 499NetworksProject
Here lies the source code for our Reddit network analysis project

# How to reproduce our analysis:
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
