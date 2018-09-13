import praw
import pandas as pd
from textblob import TextBlob
import math

reddit = praw.Reddit(client_id='2Z9jtpZEaQkCnw', client_secret='fAWBjV_hPkyY0ia7ECY_1bLCPeg', user_agent='PySentiment',
                     username='Shupy', password='Papermoon7')

ratio = {
    'subreddit': [],
    'ratio': []
}

with open('./files/subreddits.txt') as f:
    for line in f:
        subreddit = reddit.subreddit(line.strip())
        sub_submissions = subreddit.hot(limit=1)

        sub_sentiment = 0
        num_comments = 0

        for submission in sub_submissions:
            if submission.num_comments <= 200:
                if not submission.stickied:
                    submission.comments.replace_more(limit=0)
                    for comment in submission.comments.list():
                        blob = TextBlob(comment.body)

                        comment_sentiment = blob.sentiment.polarity
                        sub_sentiment += comment_sentiment

                        num_comments += 1

        ratio['subreddit'].append('/r/' + str(subreddit.display_name))
        print('/r/' + str(subreddit.display_name))
        try:
            rate = str(math.floor(sub_sentiment / num_comments * 100))
            ratio['ratio'].append(rate)
            print('Ratio: ' + rate + '\n')
        except:
            ratio['ratio'].append('No comment sentiment')
            print('No comment sentiment' + '\n')
            ZeroDivisionError
df = pd.DataFrame(ratio)
df.drop(df.ratio != 'No comment sentiment')

df.to_csv('./files/sentiment_ratio.csv', sep=',', encoding='utf8', index=False)
