# -*- coding: utf-8 -*-

import scrapy

from lianjia.items import OverViewItem, DetailItem


class DemoSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["sh.fang.lianjia.com"]
    start_urls = ("http://sh.fang.lianjia.com/loupan/pg%d" % i for i in range(1, 35))

    def parse(self, response):
        for sel in response.xpath('//li[@class="block-item"]'):
            item = OverViewItem()
            item['href'] = 'http://sh.fang.lianjia.com/'+sel.xpath('div[1]/a/@href').extract()[0].strip()
            item['name'] = sel.xpath('div[2]/div[1]/div[1]/h2/a/text()').extract()[0].strip()
            item['type'] = sel.xpath('div[2]/div[1]/div[1]/span[1]/text()').extract()[0].strip()
            item['status'] = sel.xpath('div[2]/div[1]/div[1]/span[2]/text()').extract()[0].strip()
            item['region'] = sel.xpath('div[2]/div[1]/div[2]/a/text()').extract()[0].strip()
            item['area'] = sel.xpath('div[2]/div[1]/div[3]/a/text()').extract()[0].strip()
            item['price'] = ''.join([ele.strip() for ele in sel.xpath('div[2]/div[2]/div/div/descendant-or-self::text()').extract()])
            yield item
            # 追踪detail页
            yield scrapy.Request(item['href'], callback=self.parse_detail_contents)

    def parse_detail_contents(self, response):
            item = DetailItem()
            item['href'] = response.url
            item['name'] = response.xpath('//div[5]/div[4]/div[2]/div[1]/h1/text()').extract()[0].strip()
            item['type'] = response.xpath('//div[5]/div[4]/div[2]/div[1]/span[1]/text()').extract()[0].strip()
            item['status'] = response.xpath('//div[5]/div[4]/div[2]/div[1]/span[2]/text()').extract()[0].strip()
            alias = response.xpath('//div[5]/div[4]/div[2]/div[2]/span/text()').extract()

            # 部分楼盘没有alias，页面少了一个div，这里加一个tag就是为了解决该问题
            tag = 4
            if len(alias) > 0:
                item['alias'] = alias[0]
            else:
                item['alias'] = ''
                tag = 3

            # 有的楼盘是总价在上，均价在下，有的相反，所以需要加一个判断
            row1 = ''.join(response.xpath('//div[5]/div[4]/div[2]/div[3]/div[1]/span[1]/*/text()').extract())
            row2 = ''.join(response.xpath('//div[5]/div[4]/div[2]/div[3]/div[1]/span[2]/*/text()').extract())
            if row2.startswith('总价'):
                item['price'] = row1
                item['total_price'] = row2
            elif row2.startswith('均价'):
                item['price'] = row2
                item['total_price'] = row1
            else:
                # 这里的逻辑看着比较混乱，主要是处理部分的特殊情况
                try:
                    if response.xpath('//div[5]/div[4]/div[2]/div[2]/div[1]/span/span[1]/text()').extract()[0] == '已售完':
                        item['price'] = '已售完'
                        item['total_price'] = '已售完'
                except IndexError:
                    if response.xpath('//div[5]/div[4]/div[2]/div[3]/div[1]/span/span[1]/text()').extract()[0] == '已售完':
                        item['price'] = '已售完'
                        item['total_price'] = '已售完'

            item['area'] = ''.join(response.xpath('//div[5]/div[4]/div[2]/div[3]/div[2]/span[1]/*/text()').extract())
            houseModel = response.xpath('//div[5]/div[4]/div[2]/div[3]/div[2]/span[2]/span/a/text()').extract()
            if len(houseModel) > 0:
                item['houseModel'] = houseModel
            else:
                item['houseModel'] = ''

            item['address'] = ''.join([ele.strip() for ele in response.xpath('//div[5]/div[4]/div[2]/div[4]/table/tr[1]/td[2]/descendant-or-self::text()').extract()])
            item['saleTime'] = response.xpath('//div[5]/div[4]/div[2]/div[%d]/table/tr[3]/td[2]/text()' % tag).extract()[0].strip()
            item['submitTime'] = response.xpath('//div[5]/div[4]/div[2]/div[%d]/table/tr[4]/td[2]/text()' % tag).extract()[0].strip()
            item['decoType'] = response.xpath('//*[@id="house-details"]/div/ul/li[3]/p/span[2]/text()').extract()[0].strip()
            item['tel'] = response.xpath('//*[@id="house-details"]/div/ul/li[1]/p/span[2]/text()').extract()[0].strip()
            item['salesOfficeAddr'] = response.xpath('//*[@id="house-details"]/div/p[2]/span[2]/text()').extract()[0].strip()
            item['developer'] = response.xpath('//*[@id="house-details"]/div/p[3]/span[2]/text()').extract()[0].strip()
            item['property'] = response.xpath('//*[@id="house-details"]/div/p[4]/span[2]/text()').extract()[0].strip()
            item['propertyanagementFee'] = response.xpath('//*[@id="house-details"]/div/ul/li[9]/p/span[2]/text()').extract()[0].strip()
            item['waterAndElec'] = response.xpath('//*[@id="house-details"]/div/ul/li[11]/p/span[2]/text()').extract()[0].strip()
            item['houseNum'] = response.xpath('//*[@id="house-details"]/div/ul/li[2]/p/span[2]/text()').extract()[0].strip()
            item['housePropertyRight'] = response.xpath('//*[@id="house-details"]/div/ul/li[4]/p/span[2]/text()').extract()[0].strip()
            item['far'] = response.xpath('//*[@id="house-details"]/div/ul/li[6]/p/span[2]/text()').extract()[0].strip()
            item['greenRatio'] = response.xpath('//*[@id="house-details"]/div/ul/li[8]/p/span[2]/text()').extract()[0].strip()
            item['parkingSpace'] = response.xpath('//*[@id="house-details"]/div/ul/li[10]/p/span[2]/text()').extract()[0].strip()
            yield item
