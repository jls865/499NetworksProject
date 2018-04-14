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
    #generate_data()
    pass

# Generate a series of data and put them into files
def generate_data():
    types = ["top", "hot"]
    amount = [10, 100, 1000]

    # For each type of submission
    for type in types:
        # For each amount we need to grab
        for a in amount:
            # Create a list to hold the full dictionary of data about a submission
            submission_list = []
            # The fields we want to know about
            fields = ('title', 'score', 'id', 'author', 'subreddit', 'created', 'url')

            # For every submission that we want to see
            for submission in reddit.front.top(limit=a):
                # Get the different variables that pertain to it
                to_dict = vars(submission)
                # Create a dictionary that contains all of the fields that we want
                # and their related values in the submission
                sub_dict = {field:str(to_dict[field]) for field in fields}
                # Add it to the list of submissions
                submission_list.append(sub_dict)

            # Create the filename that we want to save each set into
            filename = "Data/"+type+str(a)+"_data.json"
            with open(filename, 'w+', encoding='utf-16') as f:
                # For every submission
                for submission in submission_list:
                    f.write(str(submission))
                    f.write("\n")

if __name__ == "__main__":
    main()


