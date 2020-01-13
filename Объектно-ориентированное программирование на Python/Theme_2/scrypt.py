from bs4 import BeautifulSoup as BS
import re

with open('data.htm', 'r', encoding='utf-8') as f:
    data_file = f.read()

print('Модуль re:')
str = re.findall('<span class="total-users">([^\"]*)</span>', data_file)
print('Надпись: {}'.format(str))
str = re.findall('<span class="total-users">[а-яА-Я ]+([0-9 ]+)[а-яА-Я ]+</span>', data_file)
print('Надпись только цифры: {}'.format(str))
str = re.sub(' ', '', str[0])
str_int = int(str)
print('Цифры: {} в формате {}'.format(str_int, type(str_int)))

print('\nМодуль BeautifulSoup:')
data = BS(data_file, 'html.parser')
#print( data.prettify() )
str = data.span.text
print('Надпись: {}'.format(str))
str_list = str.split(' ')
print('Надпись только цифры: {}'.format(str_list[2] + str_list[3] + str_list[4]))
str_int = int(format(str_list[2] + str_list[3] + str_list[4]))
print('Цифры: {} в формате {}'.format(str_int, type(str_int)))