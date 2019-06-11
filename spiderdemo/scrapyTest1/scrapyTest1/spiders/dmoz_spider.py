# -*- coding: utf-8 -*-
import scrapy


class DmozSpider(scrapy.Spider):
    name = 'dmoz'  #它是每个项目唯一的名字，用来区分不同的 Spider。
    allowed_domains = ["xiaoshuo240.cn"]   #允许爬取的域名
    start_urls = [
        "http://www.xiaoshuo240.cn/"
    ]    #包含了 Spider 在启动时爬取的 url 列表，初始请求是由它来定义的 。

    def parse(self, response):
        for sel in response.xpath('//div/ul/li'):
            print(sel.extract())
