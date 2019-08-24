# pnews
I don't know python and this is how I'm learning.

## Quick start

### Install dependencies

```
pipenv install
```

### Generate an api key

Generate an API key from https://newsapi.org/

### Create your config file

Create a config file named `api.config` in the root directory in the following format:

```
[api]
api_key = API_KEY
```

Don't check your API key into github please.

### Run the script

Command:

```
pipenv run python main.py -s bbc-news -q top
```

Sample Output:

```
Top articles from bbc-news
--------------------------
Prince Andrew defends Epstein relationship
http://www.bbc.co.uk/news/uk-49460263


Hong Kong police fire tear gas in fresh clashes
http://www.bbc.co.uk/news/world-asia-china-49457920


Why is the Amazon rainforest so important?
http://www.bbc.co.uk/news/science-environment-49452736


EU 'willing to listen' to Johnson's Brexit ideas
http://www.bbc.co.uk/news/uk-politics-49458293


Ashes: Australia aim to put Ashes beyond England - in-play clips, radio & text
http://www.bbc.co.uk/sport/live/cricket/47325093


BA strike sparks five days of flight cancellations
http://www.bbc.co.uk/news/uk-49458342


Nasa 'probing first allegation of space crime'
http://www.bbc.co.uk/news/world-49457912


Trump escalates China trade war with tariff hikes
http://www.bbc.co.uk/news/business-49455503


'First vape death in the US' recorded in Illinois
http://www.bbc.co.uk/news/world-us-canada-49452256


Brazil sends army to tackle Amazon fires
http://www.bbc.co.uk/news/world-latin-america-49452789
```

A list of sources can be found at https://newsapi.org/sources
