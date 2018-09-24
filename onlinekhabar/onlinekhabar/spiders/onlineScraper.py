# -*- coding: utf-8 -*-
import scrapy


class OnlinescraperSpider(scrapy.Spider):
    name = 'onlineScraper'
    allowed_domains = ['www.onlinekhabar.com/content/news']
    start_urls = ['https://www.onlinekhabar.com/content/news/']

    def parse(self, response):
        links =  response.xpath('//div[@class="item"]/div[@class="item__wrap"]/a/@href').extract()
        next_page   = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]
        
        for link in links:
        	yield scrapy.Request(link,self.parse_article, dont_filter=True)


        yield scrapy.Request(next_page,dont_filter=True)

    def parse_article(self,response):
    	title  = response.xpath('//div[@class="nws__title--card"]/h2/text()').extract()[0]
    	article = article = response.xpath('//div[@class="col colspan3 main__read--content ok18-single-post-content-wrap"]/p/text()').extract()

    	article_final  = ''.join(article)

    	yield{

    		"News title":title,
    		"News article":article_final
    	}
