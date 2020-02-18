from selenium import webdriver
import time
from pymongo import MongoClient

client  = MongoClient('localhost',27017)
db = client['news']
news_db = db.lentaru

driver = webdriver.Firefox()
driver_more = webdriver.Firefox()

driver.get('https://lenta.ru/parts/news/')
assert 'Новости: Lenta.ru' in driver.title

chek_button = 20   # Иначе он опрашивает до бесконечности
while chek_button:
    try:
        button = driver.find_element_by_class_name('b-more-button')
        button.click()
        chek_button = chek_button - 1
    except Exception as e:
        print(e)
        chek_button = 0

links = driver.find_elements_by_xpath("//div[contains(@class, 'item news')]/div/h3/a")
# links = list()
# for link_essence in links_essence:
#     links.append(link_essence.get_attribute('href'))

for i in range(len(links)):
    print(links[i].get_attribute('href'))

result = list()

for i in range(0, len(links)):
    dict_ = dict()
    try:
        link = links[i].get_attribute('href')
    except:
        print(links[i])
        link = 'https://lenta.ru/parts/news/'

    print(link)
    driver_more.get(link)
    #time.sleep(1)
    assert 'Lenta.ru' in driver_more.title
    dict_['link'] = link
    dict_['name'] = driver_more.find_element_by_xpath("//h1[@class='b-topic__title']").text
    dict_['date'] = driver_more.find_element_by_xpath("//time[contains(@class, 'g-date')]").get_attribute('datetime')
    dict_['content'] = driver_more.find_element_by_xpath("//div[@class='b-text clearfix js-topic__text']").text
    print(dict_)

    result.append(dict_)

    try:
        news_db.insert_one(dict_)
    except:
        print('DataBases Error')

driver.quit()
driver_more.quit()