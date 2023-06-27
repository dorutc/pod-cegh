import scrapy

from ..items import DownfilesItem
from datetime import date


class CeghCSVWithinDaySpider(scrapy.Spider):
    name = "cegh_withinday_csv"
	
    def start_requests(self):
        url = 'https://www.cegh.at/wp-admin/admin-ajax.php'
        form_data={
            'action': 'get_WithinDayMarket',
            'product': 'dayMarket',
            'market': 'AT'
        }
        
        yield scrapy.FormRequest(url,
                                 formdata=form_data)

    def parse(self, response):
        file_url = response.css('a[class="ce-table__button btn btn--secondary btn--icon btn--icon--download exportButton"]::attr(href)').get()
        file_url = response.urljoin(file_url)
        item = DownfilesItem()
        item['file_urls'] = [file_url]
        today = date.today()
        str = today.strftime("%d%m%Y")
        item['original_file_name'] = 'AT_Within_Day_' + str
        yield item