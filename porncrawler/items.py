# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join


class JAVPornStarCrawlerItem(scrapy.Item):
    name = scrapy.Field()
    img_src = scrapy.Field()
    born_date = scrapy.Field()
    blood = scrapy.Field()
    breast = scrapy.Field()
    hips = scrapy.Field()
    waist = scrapy.Field()
    height = scrapy.Field()
    model_style = scrapy.Field()
    video_classes = scrapy.Field()
    video_count = scrapy.Field()


class PornhubPornStarCrawlerItem(scrapy.Item):
    name = scrapy.Field()
    img_src = scrapy.Field()
    born_date = scrapy.Field()
    height = scrapy.Field()
    gender = scrapy.Field()
    birth_place = scrapy.Field()
