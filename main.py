import argparse
import configparser
from newsapi import NewsApiClient

# read api key from config file
config = configparser.ConfigParser()
config.read('api.config')
api_key = config['api']['api_key']

# command line parser
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query')
parser.add_argument('-s', '--site')

args = parser.parse_args()

site = args.site
query = args.query

# call api
news = NewsApiClient(api_key=api_key)

if query == 'top':
    headlines = news.get_top_headlines(sources=site, language='en')
else:
    headlines = news.get_everything(q=query, sources=site, language='en')

print(headlines)