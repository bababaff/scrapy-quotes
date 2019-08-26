# Scrapy Quotes Bot
This is a Scrapy project to scrape quotes from famous people from http://quotes.toscrape.com.

## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:

    {
        'author': 'Douglas Adams',
        'text': '“I may not have gone where I intended to go, but I think I ...”',
        'tags': ['life', 'navigation']
    }


## Spiders

This project contains a spider and you can list them using the `list`
command:

    $ scrapy list
    quotes

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl quotes

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl quotes -o quotes.json
