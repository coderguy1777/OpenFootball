# -*- coding: utf-8 -*-
import scrapy


class PlayerscraperSpider(scrapy.Spider):
    name = 'playerscraper'
    start_urls = ['https://www.giants.com/team/players-roster/']

    def parse(self, response):
        print(response.url)
        print(response.css('a::text'))
        print(response.css('data::text').decode('utf-8'))