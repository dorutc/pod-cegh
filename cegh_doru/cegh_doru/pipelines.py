# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from datetime import date


class HelpDoruPipeline:
    def process_item(self, item, spider):
        return item


class DownfilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name = 'default'
        today = date.today()
        str = today.strftime("%d%m%Y")
        if 'day-ahead' in request.url:
            file_name = 'AT_day-ahead_' + str
        if 'trades' in request.url:
            file_name = 'AT_Within_Day_' + str

        if 'settlement' in request.url and 'Month' in request.url and 'front=1' in request.url:
            file_name = 'AT_futures_Month_front-period_1_' + str
        if 'settlement' in request.url and 'Month' in request.url and 'front=2' in request.url:
            file_name = 'AT_futures_Month_front-period_2_' + str
        if 'settlement' in request.url and 'Month' in request.url and 'front=3' in request.url:
            file_name = 'AT_futures_Month_front-period_3_' + str
        if 'settlement' in request.url and 'Quarter' in request.url and 'front=1' in request.url:
            file_name = 'AT_futures_Quarter_front-period_1_' + str
        if 'settlement' in request.url and 'Quarter' in request.url and 'front=2' in request.url:
            file_name = 'AT_futures_Quarter_front-period_2_' + str
        if 'settlement' in request.url and 'Quarter' in request.url and 'front=3' in request.url:
            file_name = 'AT_futures_Quarter_front-period_3_' + str
        if 'settlement' in request.url and 'Quarter' in request.url and 'front=4' in request.url:
            file_name = 'AT_futures_Quarter_front-period_4_' + str
        if 'settlement' in request.url and 'Season' in request.url and 'front=1' in request.url:
            file_name = 'AT_futures_Season_front-period_1_' + str
        if 'settlement' in request.url and 'Season' in request.url and 'front=2' in request.url:
            file_name = 'AT_futures_Season_front-period_2_' + str
        if 'settlement' in request.url and 'Season' in request.url and 'front=3' in request.url:
            file_name = 'AT_futures_Season_front-period_3_' + str
        if 'settlement' in request.url and 'Year' in request.url and 'front=1' in request.url:
            file_name = 'AT_futures_Year_front-period_1_' + str
        if 'settlement' in request.url and 'Year' in request.url and 'front=2' in request.url:
            file_name = 'AT_futures_Year_front-period_2_' + str
        if 'settlement' in request.url and 'Year' in request.url and 'front=3' in request.url:
            file_name = 'AT_futures_Year_front-period_3_' + str
        return file_name