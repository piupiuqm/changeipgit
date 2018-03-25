# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo


class ChangeipPipeline(object):
    def __init__(self):
        mongo_host = settings['MONGO_HOST']
        mongo_port = settings['MONGO_PORT']
        mongo_db = settings['MONGO_DB']
        mongo_doc = settings['MONGO_DOC']
        client = pymongo.MongoClient(host=mongo_host,port=mongo_port)
        tdb = client[mongo_db]
        self.post = tdb[mongo_doc]
    
    def process_item(self, item, spider):
        video_info = dict(item)
        self.post.insert(video_info)
        return item
