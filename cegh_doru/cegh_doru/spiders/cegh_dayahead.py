import scrapy

from ..items import TradingItem


class CeghDayAheadSpider(scrapy.Spider):
    name = "cegh_dayahead"
    
    def start_requests(self):
        url = 'https://www.cegh.at/wp-admin/admin-ajax.php'
        form_data={
            'action': 'get_DayAheadMarket',
            'product': 'aheadMarket',
            'market': 'AT'
        }
        
        yield scrapy.FormRequest(url,
                                 formdata=form_data)

    def parse(self, response):
        table_of_interest = response.css('table[data-product="aheadMarket"]')
        headers_container = table_of_interest.xpath("./thead/tr")[0]
        for header_th in headers_container.xpath('//th'):
            header = header_th.xpath("./text()").get().strip()
            unit = header_th.css('span::Text').get() if header_th.css('span::Text').get() is not None else 'N/A'
            print(f'Header is "{header}" with a unit of "{unit}"')
        for row in table_of_interest.xpath('./tr'):
            trading_item = TradingItem()
            trading_day, contract, open, high, low, close, volume_acc, trades, ceghedi, vwap_ceghix, _, _, _, _ = row.xpath(
                './td/text()').getall()
            trading_item["trading_day"] = trading_day.strip()
            trading_item["contract"] = contract.strip()
            trading_item["open"]= open.strip() 
            trading_item["high"]= high.strip()
            trading_item["low"]= low.strip() 
            trading_item["close"]= close.strip() 
            trading_item["volume_acc"]= volume_acc.strip() 
            trading_item["trades"]= trades.strip() 
            trading_item["ceghedi"]= ceghedi.strip() 
            trading_item["vwap_ceghix"]= vwap_ceghix.strip() 
            yield trading_item
