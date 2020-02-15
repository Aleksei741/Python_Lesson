# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
import os
import shutil
from leroymerlin.settings import IMAGES_STORE

class LeroymerlinPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.leroymerlin

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]

        #print(item)
        try:
            #collection.insert_one(item)
            #object_count = collection.count_documents({'name': })
            collection.update_one(
                {'name' : item['name']},
                {'$set': item},
                upsert=True
            )
        except Exception as e:
            print(e)

        return item


class LeroymerlinPhotoPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['photo_link']:
            for photo_link in item['photo_link']:
                try:
                    yield scrapy.Request(photo_link)
                except Exception as e:
                    print(e)
        pass

    def item_completed(self, results, item, info):
        if results:
            self_path = os.getcwd()

            new_path = os.path.abspath(f'D:\DataBases\Photos\{item["name"]}')

            shutil.rmtree(new_path, ignore_errors=True)
            #os.rmdir(new_path)

            try:
                os.makedirs(new_path)
            except Exception as e:
                print(e)

            num_item = 0
            list_path = list()
            for itm in results:
                if itm[0]:
                    try:
                        self_path_file = os.path.abspath(f"{self_path}\{IMAGES_STORE}\{itm[1]['path']}")
                        new_path_file = os.path.abspath(f"{new_path}\{num_item}.jpg")
                        shutil.copyfile(self_path_file, new_path_file)
                        os.remove(self_path_file)
                    except Exception as e:
                        print(e)
                num_item = num_item + 1
                list_path.append(new_path_file)

        item['photo_path'] = list_path

        return item