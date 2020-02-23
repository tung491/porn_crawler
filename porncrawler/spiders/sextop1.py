import scrapy
from scrapy.http import Request


class SexTop1(scrapy.Spider):
    name = 'sextop1'
    start_urls = ['http://sextop1.net/phim-sex-viet-sub/page/{}']
    page_numb = 19

    def start_requests(self):
        for url in self.start_urls:
            for page in range(1, self.page_numb + 1):
                request = Request(url.format(page))
                yield request

    def parse(self):
        pass