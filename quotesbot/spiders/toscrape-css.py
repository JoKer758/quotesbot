# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuotesbotItem


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
    def parse(self, response):
        # items = []
        for quote in response.css("div.quote"):
            item = QuotesbotItem()
            item['text'] = quote.css("span.text::text").extract_first()
            item['author'] = quote.css("small.author::text").extract_first()
            item['tags'] = quote.css("div.tags > a.tag::text").extract()
            yield item
        #     items.append(item)
        # return items

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
            # yield scrapy.Request(response.urljoin(next_page_url))

