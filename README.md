# Craig's List Apartment Crawler
This is a simple tool to collect information on Craig's List apartment listings. I built this after wanting some additional control beyond what sites like Padmapper could give me.

## Installation
This is a django app, but it's not really designed to live in the wild where multiple people would access it. Ideally, you'd put this on the web somewhere, but either obfuscated or otherwise protected from malicious eyes.

1. Install dependencies
2. Tweak settings.py
3. Schedule the crawler to run. You can do this by putting `python manage.py crawl` in cron or putting `http://PATH_TO_SITE/start_crawler.json` in a feed reader. For the most immediate results, run this every 5 minutes.

### Dependencies
- Tested with Python 2.7
- Django 1.3
- BeautifulSoup 3.2.1

## Running
1. Install
2. Add your crawlers. Right now, this is a manual process. You have to input `http://PATH_TO_SITE/new_crawler.json?url=CL_URL` into your browser, where `CL_URL` is the url of a Craig's List apartment list, like `http://losangeles.craigslist.org/lac/apa/`
-- You can also pass `email=your@emailaddress.com` to get emailed whenever a match is found
3. Access the UI (or query the database directly)

### Setting up your filter
The whole purpose of this tool is to be able to write your own custom filters using the power of python. To do this, you'll want to edit `common/filters.py` using whatever criteria you like. Feel free to go nuts here. Import NLTK or whatever it takes.



