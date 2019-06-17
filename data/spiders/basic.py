# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['sec.gov']
    start_urls = ['http://sec.gov/']

    def parse(self, response):
        pass
