# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HelpDoruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TradingItem(scrapy.Item):
    # define the fields for your item here like:
    trading_day = scrapy.Field()
    contract = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    volume_acc = scrapy.Field()
    trades = scrapy.Field()
    ceghedi = scrapy.Field()
    vwap_ceghix = scrapy.Field()
    price = scrapy.Field()
    product = scrapy.Field()
    trading_phase = scrapy.Field()
    best_bid = scrapy.Field()
    best_ask = scrapy.Field()

class DownfilesItem(scrapy.Item):
    
    # define the fields for your item here like:
    file_urls = scrapy.Field()
    original_file_name = scrapy.Field()
    files = scrapy.Field