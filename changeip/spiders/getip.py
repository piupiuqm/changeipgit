# -*- coding: utf-8 -*-
import scrapy
import json

class GetipSpider(scrapy.Spider):
    name = 'getip'
    allowed_domains = ['xdaili.cn']
    start_urls = ['http://www.xdaili.cn/ipagent//freeip/getFreeIps?page=1&rows=10']

    def parse(self, response):
        html = json.loads(response.body.decode('utf-8'))
        for eve in html['RESULT']['rows']:
            yield eve
