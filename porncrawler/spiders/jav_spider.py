import re

import scrapy
from scrapy.http import Request
from porncrawler.items import JAVPornStarCrawlerItem


class JAVSpider(scrapy.Spider):
    name = "jav"
    start_urls = ['https://javmodel.com/jav/homepages.php?page={}']
    base_url = 'https://javmodel.com'
    page_num = 41

    def start_requests(self):
        for url in self.start_urls:
            for page in range(1, self.page_num + 1):
                request = Request(url.format(page))
                yield request

    def parse(self, response):
        hrefs = response.xpath('//div[@class="portfolio columns-4"]/div//a[@class="mask"]/@href').extract()
        urls = map(lambda x: self.base_url + x, hrefs)

        for url in urls:
            yield response.follow(url, self.parse_item)

    @staticmethod
    def clean_data(data, datatype):
        if data:
            r_data = data
            if datatype is int:
                r_data = int(r_data)
        elif datatype is int:
            r_data = 0
        else:
            r_data = ''
        return r_data

    def parse_item(self, response):
        pornstar = JAVPornStarCrawlerItem()

        info_element = response.xpath('//div[contains(@class, "col-sm-9")]')[0]
        personal_info, video_info = info_element.xpath('//ul[@class="unstyled-list list-medium"]')
        born_date, blood, breast, waist, hips, height = personal_info.xpath('li')
        model_style, video_classes, video_count = video_info.xpath('li')

        name = info_element.xpath('//h2/text()')[0].get()
        img_src = response.xpath('//img[@class="img-rounded"]/@src').get()
        born_date = born_date.xpath('text()').re_first('\d+/\d+/\d+')
        blood = blood.xpath('text()').re_first('\w+$')
        breast = breast.xpath('text()').re_first('\d+')
        hips = hips.xpath('text()').re_first('\d+')
        waist = waist.xpath('text()').re_first('\d+')
        height = height.xpath('text()').re_first('\d+')
        model_style = model_style.xpath('a/text()').getall()
        video_classes = video_classes.xpath('a/text()').getall()
        video_count = int(video_count.xpath('text()').re_first('\d+'))

        born_date = self.clean_data(born_date, str)
        blood = self.clean_data(blood, str)
        breast = self.clean_data(breast, int)
        hips = self.clean_data(hips, int)
        waist = self.clean_data(waist, int)
        height = self.clean_data(height, int)
        video_count = self.clean_data(video_count, int)
        img_src = self.clean_data(img_src, str)

        pornstar['name'] = name
        pornstar['img_src'] = img_src
        pornstar['born_date'] = born_date
        pornstar['blood'] = blood
        pornstar['breast'] = breast
        pornstar['hips'] = hips
        pornstar['waist'] = waist
        pornstar['height'] = height
        pornstar['video_count'] = video_count
        pornstar['model_style'] = model_style
        pornstar['video_classes'] = video_classes

        return pornstar
