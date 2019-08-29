import argparse
import configparser
import json
import newsapi
import sys

def read_file(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()

    contents = []
    for line in lines:
        contents.append(line.strip('\n'))
    return contents

def get_cmd_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', default='top')
    parser.add_argument('-s', '--site', default=None)
    parser.add_argument('-p', '--page', default=5, type=int)

    return parser.parse_args()

def get_separator(len):
    separator = ''
    for i in range(len):
        separator += '-'
    return separator

def print_header(page, query=None, site=None):
    page_str = str(page)
    header = 'Top ' + page_str + ' articles '
    if query is None and site is None:
        header += 'from all sources'
    elif query is None and site is not None:
        header += 'from ' + site
    elif query is not None and site is None:
        header += 'about ' + query + ' from all sources'
    else:
        header += 'about ' + query + ' from ' + site
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
    page = args.page
    site = args.site
    query = args.query

    if site is not None and site not in sources:
        sys.exit('Source ' + site + ' is not supported\n' +
            'Please see list of supported sources at https://newsapi.org/sources')

    # call api
    news = newsapi.NewsApiClient(api_key=api_key)

    if query == 'top':
        headlines = news.get_top_headlines(sources=site, language='en', page_size=page)
        print_header(page, site=site, )
    else:
        headlines = news.get_everything(q=query, sources=site, language='en', page_size=page)
        print_header(page, site=site, query=query)

    for article in headlines['articles']:
        print_output(article)

main()
