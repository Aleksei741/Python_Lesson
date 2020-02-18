from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
#driver = webdriver.Chrome()

my_email = 'aleksandersurinov@mail.ru'
my_password = 'qwertyasdfgh741'

driver.get('https://mail.ru/')
assert 'Mail.ru: почта' in driver.title

driver.find_element_by_id('mailbox:login').send_keys(my_email)
button = driver.find_element_by_xpath("//div[contains(@class, 'mailbox__row mailbox__row_ i-clearfix')]")
time.sleep(1)
button.click()
time.sleep(2)
driver.find_element_by_id('mailbox:password').send_keys(my_password)
button = driver.find_element_by_xpath("//div[contains(@class, 'mailbox__row mailbox__row_ i-clearfix')]/label")
time.sleep(5)
button.click()
time.sleep(20)
items = driver.find_elements_by_partial_link_text("inbox")
driver.
mails = []
for item in items:
    link = item.get_attribute('href')
    info = item.find_element_by_class_name('llc__content')
    author = info.find_element_by_class_name('ll-crpt').get_attribute('title')
    subject = info.find_element_by_class_name('ll-sj__normal').text
    date = item.find_element_by_class_name('llc__item_date').get_attribute('title')
    mail = {'author': author, 'date': date, 'subject': subject, 'link': link}
    mails.append(mail)

for mail in mails:
    driver.get(mail['link'])
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id, '_BODY')]")))
    mail['text'] = driver.find_element_by_xpath("//*[contains(@id, '_BODY')]").text
    driver.back()
    WebDriverWait(driver, 5).until(EC.title_contains('Входящие'))

print(mails)

#driver.quit()