# 499NetworksProject
Here lies the source code for our Reddit network analysis project

# How to reproduce our analysis:
Step 1: Configure PRAW with personal data for __main__.py
1. Inside the same directory as __main__.py create a Config folder.
2. Create a Config.py file inside the Config folder
3. Create a __init__.py file inside the Config folder
4. Visit PRAW documentation on Configuration here: https://praw.readthedocs.io/en/latest/getting_started/configuration/reddit_initialization.html
5. Set up the Config.py file according to the below template filling in with your personal information:
   reddit = praw.Reddit(client_id='SI8pN3DSbt0zor',
                        client_secret='xaxkj7HNh8kwg8e5t4m6KvSrbTI',
                        password='1guiwevlfo00esyy',
                        user_agent='testscript by /u/fakebot3',
                        username='fakebot3')
6. Set up the __init__.py file with this same information:
    from .Config import Config
