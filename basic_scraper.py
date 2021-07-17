import praw
from configs import * ## configs is a hidden file

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=SECRET, user_agent=AGENT)

hot_posts = reddit.subreddit('Singapore').hot(limit=10)
for post in hot_posts:
    print(post)
