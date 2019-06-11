# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# Item 是保存爬取到的数据的容器；其使用方法和python字典类似， 并且提供了额外保护机制来避免拼写错误导致的未定义字段错误。
'''
类似在ORM中做的一样，您可以通过创建一个 scrapy.Item 类， 
并且定义类型为 scrapy.Field 的类属性来定义一个Item。 (如果不了解ORM, 不用担心，您会发现这个步骤非常简单)
首先根据需要从dmoz.org获取到的数据对item进行建模。 
我们需要从dmoz中获取名字，url，以及网站的描述。 对此，在item中定义相应的字段。编辑 tutorial 目录中的 items.py 文件:'''
class Scrapytest1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
