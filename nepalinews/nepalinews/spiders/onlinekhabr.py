# -*- coding: utf-8 -*-
#while dumping data use diffrent names according to the categories in the link
import scrapy
from scrapy import Selector
from scrapy import Request
from os import system,chdir



class OnlinekhabrSpider(scrapy.Spider):
    name = "onlinekhabr"
    #make changes to link here
    allowed_domains = ["onlinekhabar.com/content/news"]
    #start_urls = ('https://onlinekhabar.com/content/news/',)

    def __init__(self,category,address):
        names = category
        system ('mkdir '+names )
        chdir (names)
        self.start_urls = [address]

    def parse(self, response):
        links=response.xpath('//*[@class="news_loop"]/h2/a/@href').extract()
        for link in links:
            print(link)
            yield Request(link,callback= self.parse_article,dont_filter=True)


        nextpageurl = response.xpath('//*[@class="next page-numbers"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(nextpageurl)    
        yield scrapy.Request(absolute_next_page_url,dont_filter=True)

    def parse_article(self,response):
        title = response.xpath('//h1[@class="inside_head"]/text()').extract()
        title = title[0]+'.txt'
        article = response.xpath('//div[@class="ok-single-content"]/p/text()').extract()
        article = ''.join(article)
        #remove comment if you want to save every single news in a text file seperately
        #write_article  = open(title,'w')
        #write_article.write(article)
        #write_article.close()

        yield{

            "article":article
            }