# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QuotesbotPipeline(object):
    def __init__(self):
        self.fo = open('items.json', 'w')
    def process_item(self, item, spider):
        self.fo.writelines(json.dumps(dict(item))+'\n')
        return item