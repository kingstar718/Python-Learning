# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  #它是每个项目唯一的名字，用来区分不同的 Spider。
    allowed_domains = ['quotes.toscrape.com']   #允许爬取的域名
    start_urls = ['http://quotes.toscrape.com/']    #包含了 Spider 在启动时爬取的 url 列表，初始请求是由它来定义的 。

    def parse(self, response):
        
        pass
