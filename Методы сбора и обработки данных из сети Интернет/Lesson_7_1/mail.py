from selenium import webdriver
#import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
#driver_content = webdriver.Firefox()
#driver = webdriver.Chrome()

my_email = 'study.ai_172@mail.ru'
my_password = 'NewPassword172'

driver.get('https://mail.ru/')
assert 'Mail.ru: почта' in driver.title

driver.find_element_by_id('mailbox:login').send_keys(my_email)
button = driver.find_element_by_xpath("//div[contains(@class, 'mailbox__row mailbox__row_ i-clearfix')]")
time.sleep(1)
button.click()
time.sleep(1)
driver.find_element_by_id('mailbox:password').send_keys(my_password)
button = driver.find_element_by_xpath("//div[contains(@class, 'mailbox__row mailbox__row_ i-clearfix')]/label")
time.sleep(1)
button.click()
#time.sleep(30)
WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, 'dataset__items')))
#items = driver.find_elements_by_xpath("//a[contains(@class, 'llct js-letter-list-item llct_pony-mode')]")
#links = list()
mails = []

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@id, 'app-loader')]")))
item = driver.find_element_by_xpath("//div[contains(@id, 'app-loader')]")
time.sleep(1)
item.click()
#item.send_keys(Keys.ENTER)

num = 200
while num:
    mail = dict()
    num -= 1

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id, '_BODY')]")))
    mail['author'] = item.find_element_by_class_name('ll-crpt').get_attribute('title')
    mail['subject'] = item.find_element_by_class_name('ll-sj__normal').text
    mail['date'] = item.find_element_by_class_name('llct__date').get_attribute('title')
    mail['text'] = driver.find_element_by_xpath("//*[contains(@id, '_BODY')]").text
    print(mail)
    mails.append(mail)
    item.send_keys(Keys.ARROW_DOWN)
    item.click()

# for item in items:
#     mail = dict()
#     link = item.get_attribute('href')
#     links.append(link)
#     print(link)
#     mail['author'] = item.find_element_by_class_name('ll-crpt').get_attribute('title')
#     mail['subject'] = item.find_element_by_class_name('ll-sj__normal').text
#     mail['date'] = item.find_element_by_class_name('llct__date').get_attribute('title')
#     mails.append(mail)
#
# for i in range(len(mails)):
#     driver.get(links[i])
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id, '_BODY')]")))
#     mails[i]['text'] = driver.find_element_by_xpath("//*[contains(@id, '_BODY')]").text
#     driver.back()
#
#     print(mails[i])
driver.quit()