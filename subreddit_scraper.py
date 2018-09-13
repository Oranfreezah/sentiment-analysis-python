from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.redditmetrics.com/top')

soup = BeautifulSoup(url.text, 'html.parser')


def sublist():
    with open('./files/subreddits.txt', 'w') as f:
        for subreddit in soup.find_all('a'):
            try:
                if '/r' in subreddit.string:
                    f.write(subreddit.string[3:] + '\n')
            except:
                TypeError
