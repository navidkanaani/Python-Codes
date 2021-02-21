import requests
from bs4 import BeautifulSoup
import pprint

rss = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(rss.text, "html.parser")
links = soup.select(".storylink")
subtext = soup.select(".subtext")

def sorted_news(news_list):
    return sorted(news_list, key = lambda k : k['votes'], reverse=True)

def custom_news(links, subtext):
    news = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': href, 'votes': points})
    return sorted_news(news)

pprint.pprint(custom_news(links, subtext))