# -*- coding: utf-8 -*-
import scrapy


class PlayerscraperSpider(scrapy.Spider):
    name = 'playerscraper'
    allowed_domains = ['pro-football-reference.com/years/2018/index.htm/']
    start_urls = ['http://pro-football-reference.com/years/2018/index.htm/']

    def parse(self, response):
        pass
