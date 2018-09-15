# -*-coding:utf-8 -*-

import scrapy
from scrapy import log
from scrapy_splash import SplashRequest
from game_news.items import GameNewsItem


class SSXKSpider(scrapy.spiders.Spider):
    name = "SSXK"
    allowed_domains = ["gamersky.com/"]
    start_urls = [
        "https://www.gamersky.com/ent/201809/1098158.shtml",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                args={'wait': 0.5},
                                endpoint='render.html',
                                )

    def parse(self, response):
        item = GameNewsItem()
        item['title'] = response.xpath('//*[@id="jcjbContentData"]/@title').extract_first()

        temp = response.xpath('/html/body/div[10]/div[2]/div[1]/div[1]/div[2]/div/text()').extract_first()

        item['time'] = response.xpath('/html/body/div[10]/div[2]/div[1]/div[1]/div[2]/div/text()').extract()
        item['source'] = []

        item['body'] = []

        log.msg(item)

        yield item
