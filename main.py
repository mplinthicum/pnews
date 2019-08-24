import argparse
import configparser
import json
from newsapi import NewsApiClient

# read api key from config file
config = configparser.ConfigParser()
config.read('api.config')
api_key = config['api']['api_key']

# command line parser
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query')
parser.add_argument('-s', '--site')
parser.add_argument('-t', '--titles', action='store_true')

args = parser.parse_args()

site = args.site
query = args.query
show_titles = args.titles


# call api
news = NewsApiClient(api_key=api_key)

if query == 'top':
    headlines = news.get_top_headlines(sources=site, language='en')
else:
    headlines = news.get_everything(q=query, sources=site, language='en')

if show_titles:
    for article in headlines['articles']:
        print(article['title'])
else:
    print(json.dumps(headlines, sort_keys=True, indent=2))
