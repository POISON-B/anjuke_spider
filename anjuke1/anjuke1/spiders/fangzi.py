# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from anjuke1.items import Anjuke1Item


class FangziSpider(CrawlSpider):
    name = 'fangzi'
    allowed_domains = []
    start_urls = ['http://bj.fang.anjuke.com/loupan/all/p1/']

    rules = (
        Rule(LinkExtractor(allow=r'\w+.fang.anjuke.com$')),
        Rule(LinkExtractor(allow=r'loupan/all/p\d+'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

        for i in response.xpath('//div[@rel="nofollow"]'):
            item = Anjuke1Item()

            item['name'] = i.xpath("./div/a/h3/span/text()").extract()
            item['url'] = i.xpath("./a[1]/@href").extract()
            item['address'] = i.xpath("./div/a[2]/span/text()").extract()
            item['info'] = i.xpath("./div/a[3]/span/text()").extract()
            item['types'] = i.xpath("./div/a[4]/div/i/text()").extract()
            item['price'] = i.xpath("./a[2]/p[1]/span/text()").extract()
            item['city'] = response.xpath('//div[@class="sel-city"]/a/span/text()').extract()[0]
            yield item