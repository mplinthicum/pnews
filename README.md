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

### Script parameters
|Full Parameter|Shorthand|Description|Default|
|--------------|---------|-----------|-------|
|--query|-q|Topic to search for|Stories for all topics|
|--site|-s|News site to query from|Stories for all sites|
|--page|-p|Number of stories to display|5|

### Example

Command:

```
pipenv run python pnews.py -s bbc-news -q climate -p 3
```

Sample Output:

```
Top 3 articles about climate from bbc-news
------------------------------------------

Greta Thunberg: Why are young climate activists facing so much hate?
--------------------------------------------------------------------
URL: https://www.bbc.co.uk/news/world-49291464
Author: https://www.facebook.com/bbcnews
Publish Date: 2019-08-28T13:48:59Z
Description: In the fractious climate debate, criticism of young activists has sometimes spiralled into abuse.

Climate change: Should you fly, drive or take the train?
--------------------------------------------------------
URL: https://www.bbc.co.uk/news/science-environment-49349566
Author: https://www.facebook.com/bbcnews
Publish Date: 2019-08-23T23:37:03Z
Description: How should you travel to reduce your carbon footprint?

Pacific forum turns into row with Australia over climate goals
--------------------------------------------------------------
URL: https://www.bbc.co.uk/news/world-australia-49365918
Author: https://www.facebook.com/bbcnews
Publish Date: 2019-08-16T03:29:40Z
Description: Small Pacific nations tell the region's biggest emitter it should be more focused on "saving" people.
```

A list of sources can be found at https://newsapi.org/sources
