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
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query')
    parser.add_argument('-s', '--site')

    return parser.parse_args()

def get_separator(len):
    separator = ''
    for i in range(len):
        separator += '-'
    return separator

def print_header(header):
    print(header)
    print(get_separator(len(header)))
    print()

def print_output(article):
    print(article['title'])
    print(get_separator(len(article['title'])))
    print('URL: ' + article['url'])
    if article['author'] is not None:
        print('Author: ' + article['author'])
    print('Publish Date: ' + article['publishedAt'])
    print('Description: ' + article['description'])
    print()

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
        sys.exit('Source ' + args.site + ' is not supported\n' +
            'Please see list of supported sources at https://newsapi.org/sources')

    # call api
    news = NewsApiClient(api_key=api_key)

    if args.query == 'top':
        headlines = news.get_top_headlines(sources=args.site, language='en')
        print_header('Top news articles from ' + args.site)
    else:
        headlines = news.get_everything(q=args.query, sources=args.site, language='en', page_size=10)
        print_header('News articles about ' + args.query + ' from ' + args.site)

    for article in headlines['articles']:
        print_output(article)

main()
