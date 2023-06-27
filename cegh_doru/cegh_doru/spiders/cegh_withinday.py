import scrapy

from ..items import TradingItem


class CeghWithinDaySpider(scrapy.Spider):
    name = "cegh_withinday"
    
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
        table_of_interest = response.css('table[data-product="dayMarket"]')
        headers_container = table_of_interest.xpath("./thead/tr")[0]
        for header_th in headers_container.xpath('//th'):
            header = header_th.xpath("./text()").get().strip()
            unit = header_th.css('span::Text').get() if header_th.css('span::Text').get() is not None else 'N/A'
            print(f'Header is "{header}" with a unit of "{unit}"')
        for row in table_of_interest.xpath('./tr'):
            trading_item = TradingItem()
            trading_day, price, product, trading_phase, best_bid, best_ask, volume_acc = row.xpath('./td/text()').getall()
            trading_item["trading_day"] = trading_day.strip()
            trading_item["price"] = price.strip()
            trading_item["product"]= product.strip() 
            trading_item["trading_phase"]= trading_phase.strip()
            trading_item["best_bid"]= best_bid.strip() 
            trading_item["best_ask"]= best_ask.strip() 
            trading_item["volume_acc"]= volume_acc.strip() 
            yield trading_item
