import argparse
import configparser
import json
import sys
from newsapi import NewsApiClient

def read_file(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    contents = []
    for line in lines:
        contents.append(line.strip('\n'))
    return contents

def get_cmd_input():
    # command line parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query')
    parser.add_argument('-s', '--site')

    return parser.parse_args()

def main():
    # read api key from config file
    config = configparser.ConfigParser()
    config.read('secret.cfg')
    api_key = config['api']['api_key']

    # read supported sources and countries from config
    config.read('pnews.cfg')
    sources_file = config['paths']['sources']
    countries_file = config['paths']['countries']

    sources = read_file(sources_file)
    countries = read_file(countries_file)

    args = get_cmd_input()

    if args.site not in sources:
        sys.exit('Source ' + args.site + ' is not supported\nPlease see list of supported sources at https://newsapi.org/sources')

    # call api
    news = NewsApiClient(api_key=api_key)

    if args.query == 'top':
        headlines = news.get_top_headlines(sources=args.site, language='en')
        print('Top articles from ' + args.site)
        print('--------------------------')
    else:
        headlines = news.get_everything(q=args.query, sources=args.site, language='en')

    for article in headlines['articles']:
        print(article['title'])
        print(article['url'])
        print('\n')

main()
