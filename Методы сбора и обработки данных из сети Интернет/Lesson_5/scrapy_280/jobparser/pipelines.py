# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re

class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongobase = client.vacansy_280

    def process_item(self, item, spider):
        test = item['salary']
        #print(test)
        #Если ххру
        item['salary'] = item['salary'].replace('\xa0', ' ')
        if spider.name == 'hhru':
            if item['salary'] == 'з/п не указана':
                finance_min = None
                finance_max = None
                valuta  = None
            else:
                pattern_number = re.compile('[0-9]{1,3}\s{1}[0-9]{3}')
                pattren_valuta = re.compile('руб\.|USD|EUR|KZT|грн.')
                pattren_ot = re.compile('от')
                pattren_do = re.compile('до')

                number = re.findall(pattern_number, item['salary'])
                valuta = re.findall(pattren_valuta, item['salary'])
                if valuta:
                    valuta = valuta[0]
                if len(number) == 2:
                    finance_min = int(number[0].replace(' ', ''))
                    finance_max = int(number[1].replace(' ', ''))
                    #valuta = valuta
                elif len(number) == 1:
                    ot = re.findall(pattren_ot, item['salary'])
                    do = re.findall(pattren_do, item['salary'])
                    if not do:
                        finance_min = int(number[0].replace(' ', ''))
                        finance_max = None
                        #valuta = valuta
                    elif not ot:
                        finance_min = None
                        finance_max = int(number[0].replace(' ', ''))
                        #valuta = valuta

        # Если сджру
        if spider.name == 'sjru':
            if item['salary'] == 'По договорённости':
                dict_['finance_min'] = None
                dict_['finance_max'] = None
                dict_['valuta'] = None
            else:
                pattern_number = re.compile('[0-9]{1,3}\s{1}[0-9]{3}')
                pattren_valuta = re.compile('₽')
                pattren_ot = re.compile('от')
                pattren_do = re.compile('до')

                number = re.findall(pattern_number, item.item['salary'])
                valuta = re.findall(pattren_valuta, item.item['salary'])
                if valuta:
                    valuta = valuta[0]
                if len(number) == 2:
                    finance_min = int(number[0].replace(' ', ''))
                    finance_max = int(number[1].replace(' ', ''))
                    #dict_['valuta'] = valuta
                elif len(number) == 1:
                    ot = re.findall(pattren_ot, item['salary'])
                    do = re.findall(pattren_do, item['salary'])
                    if not do:
                        finance_min = int(number[0].replace(' ', ''))
                        finance_max = None
                        #dict_['valuta'] = valuta
                    elif not ot:
                        finance_min = None
                        finance_max = int(number[0].replace(' ', ''))
                        #dict_['valuta'] = valuta

        dict_ = {'name': item['name'],
                 'finance_min': finance_min,
                 'finance_max': finance_max,
                 'link': item['link'],
                 'source': item['source']}

        collection = self.mongobase['Python']
        collection.insert_one(dict_)


        return item
