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

Create a config file named `secret.cfg` in the root directory in the following format:

```
[api]
api_key = API_KEY
```

Don't check your API key into github please.

### Run the script

Command:

```
pipenv run python pnews.py -s bbc-news -q top
```

Sample Output:

```
Top news articles from bbc-news
-------------------------------

Australian writer faces spying charges in China
-----------------------------------------------
URL: http://www.bbc.co.uk/news/world-australia-49479020
Author: BBC News
Publish Date: 2019-08-27T00:33:33Z
Description: Australia says it has serious concerns for Yang Hengjun who has been detained in Beijing since January.

Dutch doctor on trial in euthanasia case
----------------------------------------
URL: http://www.bbc.co.uk/news/world-europe-49478304
Author: BBC News
Publish Date: 2019-08-27T00:08:58Z
Description: It is the first euthanasia case in the Netherlands involving a patient suffering from Alzheimer's.

The village surviving a drought on cave water
---------------------------------------------
URL: http://www.bbc.co.uk/news/49436917
Author: BBC News
Publish Date: 2019-08-26T23:08:53Z
Description: In Indonesia's East Java province, government water trucks only deliver once or twice a month.

.
.
.
```

A list of sources can be found at https://newsapi.org/sources
