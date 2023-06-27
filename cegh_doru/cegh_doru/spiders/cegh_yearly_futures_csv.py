import scrapy

from ..items import DownfilesItem
from datetime import date


class CeghCSVYearlyFuturesSpider(scrapy.Spider):
    name = "cegh_yearly_futures_csv"
	
    def start_requests(self):
        url = 'https://www.cegh.at/wp-admin/admin-ajax.php'
        form_data={
            'action': 'get_YearlyFutures',
            'period': 'Year',
            'product': 'yearly',
            'market': 'AT'
        }
        
        yield scrapy.FormRequest(url,
                                 formdata=form_data)

    def parse(self, response):
        file_url = response.css('a[data-front="1"]::attr(href)').get()
        file_url = response.urljoin(file_url)
        item = DownfilesItem()
        item['file_urls'] = [file_url]
        today = date.today()
        str = today.strftime("%d%m%Y")
        item['original_file_name'] = 'AT_futures_Year_front-period_1_' + str
        yield item
        file_url = response.css('a[data-front="2"]::attr(href)').get()
        file_url = response.urljoin(file_url)
        item = DownfilesItem()
        item['file_urls'] = [file_url]
        today = date.today()
        str = today.strftime("%d%m%Y")
        item['original_file_name'] = 'AT_futures_Year_front-period_2_' + str
        yield item
        file_url = response.css('a[data-front="3"]::attr(href)').get()
        file_url = response.urljoin(file_url)
        item = DownfilesItem()
        item['file_urls'] = [file_url]
        today = date.today()
        str = today.strftime("%d%m%Y")
        item['original_file_name'] = 'AT_futures_Year_front-period_3_' + str
        yield item