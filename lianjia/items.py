# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OverViewItem(scrapy.Item):
    # define the fields for your item here like:
    href = scrapy.Field()  # 楼盘详情页链接
    name = scrapy.Field()  # 楼盘名称
    type = scrapy.Field()  # 楼盘类型
    status = scrapy.Field()  # 在售状态
    region = scrapy.Field()  # 地区
    area = scrapy.Field()   # 面积
    price = scrapy.Field()  # 价格


class DetailItem(scrapy.Item):
    href = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    alias = scrapy.Field()  # 别名
    price = scrapy.Field()  # 均价
    total_price = scrapy.Field()  # 总价
    area = scrapy.Field()
    houseModel = scrapy.Field()  # 户型
    address = scrapy.Field()
    saleTime = scrapy.Field()  # 开盘时间
    submitTime = scrapy.Field()  # 交房时间
    decoType = scrapy.Field()   # 装修
    tel = scrapy.Field()    # 电话
    salesOfficeAddr = scrapy.Field()    # 售楼处地址
    developer = scrapy.Field()  # 开发商
    property = scrapy.Field()   # 物业
    propertyanagementFee = scrapy.Field()   # 物业费
    waterAndElec = scrapy.Field()   # 水电类型
    houseNum = scrapy.Field()   # 户数
    housePropertyRight = scrapy.Field()     # 产权
    far = scrapy.Field()    # 容积率
    greenRatio = scrapy.Field()  # 绿化率
    parkingSpace = scrapy.Field()   # 车位比

