# -*- coding: utf-8 -*-
import scrapy
from quotes_bot.items import Quote


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    # When you add start urls make sure to remove 'www.' part from the url otherwise you will get some errors.
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quotes = response.xpath("//*[@class='quote']")

        for quote in quotes:
            # when using a custom selector we put . like below to make sure we only get the content from the selector itself
            author = quote.xpath(".//*[@class='author']/text()").get()
            text = quote.xpath(".//*[@class='text']/text()").get()
            tags = quote.xpath(".//*[@class='tag']/text()").getall()

            quote = Quote(author=author, text=text, tags=tags)

            yield quote

        # /page/1/
        next_page_url = response.xpath("//*[@class='next']/a/@href").get()

        # http://quotes.toscrape.com/page/1/
        absolute_next_page_url = response.urljoin(
            next_page_url)

        # If there is a next page follow that link and REPEAT!
        if next_page_url:
            yield scrapy.Request(absolute_next_page_url)
