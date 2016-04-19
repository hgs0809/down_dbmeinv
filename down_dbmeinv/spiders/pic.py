# -*- coding: utf-8 -*-
import scrapy
from down_dbmeinv.items import DownDbmeinvItem


class PicSpider(scrapy.Spider):
    name = "pic"
    allowed_domains = ["dbmeinv.com"]
    start_urls = (
        'http://www.dbmeinv.com/',
    )

    def parse(self, response):
	item = DownDbmeinvItem();
	for url in response.xpath("//div/a/img/@src"):
		item['url'] = url.extract();
		yield item;
	next_page = response.xpath("//li[@class='next next_page']/a/@href").extract()[0]
	all_url = "http://www.dbmeinv.com%s"%next_page
	if next_page[-1] != '4':
		print next_page[-1]
		print all_url
		yield scrapy.Request(all_url)
