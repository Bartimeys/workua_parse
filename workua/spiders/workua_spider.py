import re
import scrapy

from workua.items import WorkuaItem


class WorkuaSpider(scrapy.Spider):
    name = "workua"

    start_urls = ['https://www.work.ua/jobs-kyiv-python/?advs=1&days=125']

    def parse(self, response):
        # follow links to author pages
        for item in response.css('.card.card-hover.card-visited.job-link.card-logotype'):
            item_url = item.css('h2>a::attr(href)').extract_first()
            basic_url ='https://www.work.ua/'

            yield scrapy.Request(basic_url+item_url, callback=self.parse_workua)

            next_page = response.css('#center > div > div.row > div.col-md-8.col-left > nav > ul.pagination.hidden-xs a::attr(href)').extract_first()

            if next_page is not None:
                next_page = response.urljoin(next_page)

                yield scrapy.Request(next_page, callback=self.parse)

    def parse_workua(self, response):
        item = WorkuaItem()
        res = response.css('div.card')
        item['vacancy'] = res.css('#h1-name::text').extract_first()
        item['company'] = response.css('title::text').extract_first()
        item['time'] = res.css('span.text-muted::text').extract_first()
        item['description'] = res.css('div.overflow.wordwrap>p::text').extract_first()

        yield item