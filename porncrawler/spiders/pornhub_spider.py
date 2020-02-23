import scrapy
from scrapy.http import Request
from porncrawler.items import PornhubPornStarCrawlerItem


class PornHubSpider(scrapy.Spider):
    name = 'pornhub'

    start_urls = ['https://www.pornhub.com/pornstars?page={}']
    base_url = 'https://www.pornhub.com'
    page_numb = 1474

    def start_requests(self):
        for url in self.start_urls:
            for page in range(1, self.page_numb + 1):
                request = Request(url.format(page))
                yield request

    def parse(self, response):
        hrefs = response.xpath('//ul[@class="videos row-5-thumbs popular-pornstar"]/li[not (contains(@class, "sniperModeEngaged"))]/div/div/a/@href').getall()
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
        model = PornhubPornStarCrawlerItem()
        name = response.xpath('//div[@class="name"]/h1/text()').get()
        if name:
            model['name'] = name.strip()
        else:
            model['name'] = ''
        gender = response.xpath('//span[contains(@itemprop, "gender")]/text()').get()
        if gender:
            gender = gender.strip()
        model['gender'] = gender
        born_date = response.xpath('//span[contains(@itemprop, "birthDate")]/text()').get()
        if born_date:
            model['born_date'] = born_date.strip()
        else:
            model['born_date'] = ''
        birth_place = response.xpath('//span[contains(@itemprop, "birthPlace")]/text()').get()
        if birth_place:
            model['birth_place'] = birth_place.strip()
        else:
            model['birth_place'] = ''
        model['img_src'] = response.xpath('//img[@id="getAvatar"]/@src').get()
        height = response.xpath('//span[contains(@itemprop, "height")]/text()').re_first('\((\d+)cm\)')
        if height:
            height = int(height)
        else:
            height = 0
        model['height'] = height

        return model







