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

```
pipenv python main.py -s bbc-news -q top
```

A list of sources can be found at https://newsapi.org/sources
