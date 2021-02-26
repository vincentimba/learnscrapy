import scrapy
from ..luntanconfig import *
import re

class LuntanSpider(scrapy.Spider):
    name = 'luntan'
    # allowed_domains = ['www.xxx.com']
    luntan_headers = luntan_headers
    raw_url = luntan_url

    def start_requests(self):
        for i in range(1, 16):
            start_urls = self.raw_url + str(i)
            yield scrapy.Request(start_urls,
                                 callback=self.parse,
                                 headers=self.luntan_headers)

    def parse(self, response):
        raw_html = response.body.decode('gbk')
        page_urls_list = re.findall('<a href="(read\.php\?tid=\d+)" name', raw_html, re.S)
        for st_url in [page_urls_list[2]]:
            # for st_url in page_urls_list:
            page_url = self.root_url + st_url
            yield scrapy.Request(page_url, callback=self.page_parse, headers=self.raw_headers)
