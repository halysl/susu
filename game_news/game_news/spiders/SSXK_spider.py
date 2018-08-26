# -*-coding:utf-8 -*-

import scrapy
from game_news.items import GameNewsItem


class SSXKSpider(scrapy.spiders.Spider):
    name = "SSXK"
    allowed_domains = ["gamersky.com/"]
    start_urls = [
        "http://www.gamersky.com/news/201808/\d+.shtml",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = GameNewsItem()
        item['title'] = response.xpath('/html/body/div[10]/div/div[2]/div[1]/div[1]/div[2]/h1/text()').extract_first()

        temp = response.xpath('/html/body/div[10]/div/div[2]/div[1]/div[1]/div[2]/div/text()').extract_first()

        item['time'] = "-".join([temp.strip().split(' ')[0], temp.strip().split(' ')[1]])
        item['source'] = temp.strip().split('来源：')[1]

        item['body'] = response.xpath('/html/body/div[10]/div/div[2]/div[1]/div[1]/div[3]')

        yield item