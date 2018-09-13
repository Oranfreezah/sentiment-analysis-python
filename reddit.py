import praw
import pandas as pd
import subreddit_scraper as ss
import utils

reddit = praw.Reddit(client_id='2Z9jtpZEaQkCnw', client_secret='fAWBjV_hPkyY0ia7ECY_1bLCPeg', user_agent='PySentiment', username='Shupy', password='Papermoon7')

dataset = []

# ss.sublist()

with open('./files/subreddits.txt') as f:

    for line in f:
        subreddit = reddit.subreddit(line.strip())
        sub_submissions = subreddit.hot(limit=1)

        for submission in sub_submissions:

            if submission.num_comments >= 2000:
                # print('✎ ' + subreddit.display_name)
                # print('★ ' + subreddit.title)
                # print('❤ ' + subreddit.description)

                dict = {
                    'title': [],
                    'subreddit': [],
                    'score': [],
                    'id': [],
                    'url': [],
                    'num_comments': [],
                    'comments': [],
                    'created': [],
                    'body': []
                }
                dict['title'].append(submission.title)
                dict['subreddit'].append(submission.subreddit.display_name)
                dict['score'].append(submission.score)
                dict['id'].append(submission.id)
                dict['url'].append(submission.url)
                dict['num_comments'].append(submission.num_comments)
                dict['created'].append(submission.created)
                dict['body'].append(submission.selftext)

                # submission.comments.replace_more(limit=0)
                # for comments in submission.comments:
                #     dict['comments'].append(comments.body)

                # print('✉ ' + dict['title'][0])

                dict["created"] = utils.get_date(dict['created'][0])
                dataset.append(dict)

    df = pd.DataFrame(dataset).to_csv('./files/submissions.csv', sep=',', encoding='utf8', index=False)
    df = pd.read_csv('./files/submissions.csv')
