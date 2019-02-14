import urllib3 as plib
import scrapy as sp
from scrapy.spiders import CrawlSpider


class WebScrap(CrawlSpider):
    name = 'playerstatbot'
    allowed_domains = ['https://www.pro-football-reference.com/years/2018/index.htm/']
    start_urls = ['https://www.pro-football-reference.com/years/2018/index.htm//']

    def start_requests(self):
        urls = ['https://www.pro-football-reference.com/years/2018/index.htm/']
        for url in urls:
            yield sp.Request(url=url, callback=self.parse)

    def parse(self, response):
        response.css('trbody::text()').get()
        for row in response.xpath('//*[@class = "table table-stripped"]//tbody/tr'):
            name = {
                'wins': row.xpath('td[0]//text()').extract_first(),
                'losses': row.xpath('td[1]//text()').extract_first(),
                'ties': row.xpath('td[2]//text()').extract_first(),
            }
            print(name)

            yield name