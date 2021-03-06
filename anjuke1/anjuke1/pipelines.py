# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class Anjuke1Pipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname = settings['SHEETNAME']

        client = pymongo.MongoClient(host=host, port=port)

        mydb = client['fangzi']
        # 存放数据的表
        self.mydata = mydb['data']

    def process_item(self, item, spider):
        data = dict(item)

        self.mydata.insert(data)

        return item


