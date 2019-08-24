import argparse
from newsapi import NewsApiClient

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query')
parser.add_argument('-s', '--site')

args = parser.parse_args()

site = args.site
query = args.query

news = NewsApiClient(api_key='apikey')

if query == 'top':
    headlines = news.get_top_headlines(sources=site, language='en')
else:
    headlines = news.get_everything(q=query, sources=site, language='en')

print(headlines)