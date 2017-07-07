# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from lianjia.items import OverViewItem, DetailItem


class LianjiaPipeline(object):

    def __init__(self):
        self.overview = open('overview.json', 'w')
        self.detail = open('detail.json', 'w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        if isinstance(item, OverViewItem):
            self.overview.write(line)
        elif isinstance(item, DetailItem):
            self.detail.write(line)
        return item

