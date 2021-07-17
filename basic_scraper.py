import praw
from configs import * ## configs is a hidden file
import pandas as pd

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=SECRET, user_agent=AGENT)

hot_posts = reddit.subreddit('Singapore').hot(limit=10)
for post in hot_posts:
    print(post.title)



posts = []
ml_subreddit = reddit.subreddit('Singapore')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)