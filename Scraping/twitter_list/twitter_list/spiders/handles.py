# -*- coding: utf-8 -*-
import scrapy


class HandlesSpider(scrapy.Spider):
    name = 'handles'
    allowed_domains = ['http://www.socialsamosa.com/']
    start_urls = ['http://www.socialsamosa.com/2014/05/indian-celebrities-twitter/']

    def parse(self, response):
    	table=response.xpath('//*[@class="td-post-text-content"]/h2')
    	for t in table:
    		name=t.xpath('text()').extract_first().split()
    		string=''
    		for n in name[:-2]:
    			string+=n+' '
    		string+=name[-2]
    		handle=t.xpath('a/@href').extract_first()
    		handle=handle[20:]
    		details={
    		'Name': string, 'Twitter Handle': handle
    		}
    		yield details

        
