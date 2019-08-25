import argparse
import configparser
import json
import sys
from newsapi import NewsApiClient

# read contents of a file
# newline delimited
# strip newline and store in array
def read_file(file_path):
    f = open(sources_file, 'r')
    lines = f.readlines()
    contents = []
    for line in lines:
        contents.append(line.strip('\n'))
    return contents

# read api key from config file
config = configparser.ConfigParser()
config.read('conf/api.config')
api_key = config['api']['api_key']

# read supported sources and countries from config
config.read('conf/sources.config')
sources_file = config['paths']['sources']
countries_file = config['paths']['countries']

sources = read_file(sources_file)
countries = read_file(countries_file)

# command line parser
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query')
parser.add_argument('-s', '--site')

args = parser.parse_args()

site = args.site
query = args.query

if site not in sources:
    sys.exit('Source ' + site + ' is not supported\nPlease see list of supported sources at https://newsapi.org/sources')

# call api
news = NewsApiClient(api_key=api_key)

if query == 'top':
    headlines = news.get_top_headlines(sources=site, language='en')
    print('Top articles from ' + site)
    print('--------------------------')
else:
    headlines = news.get_everything(q=query, sources=site, language='en')

for article in headlines['articles']:
    print(article['title'])
    print(article['url'])
    print('\n')
