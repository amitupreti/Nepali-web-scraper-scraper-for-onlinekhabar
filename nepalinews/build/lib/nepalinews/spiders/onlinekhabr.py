# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request


class OnlinekhabrSpider(scrapy.Spider):
    name = "onlinekhabr"
    allowed_domains = ["onlinekhabar.com/content/news"]
    start_urls = ('https://onlinekhabar.com/content/news/',)


    def parse(self, response):
        links=response.xpath('//*[@class="news_loop"]/h2/a/@href').extract()
        for link in links:
        	yield{"link":link}
            
        nextpageurl = response.xpath('//*[@class="next page-numbers"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(nextpageurl)    
        yield scrapy.Request(absolute_next_page_url,dont_filter=True)

