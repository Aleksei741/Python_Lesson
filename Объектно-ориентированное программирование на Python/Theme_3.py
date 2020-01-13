import requests
import json

str = input('Название города: ')

print('Получение данных')
url = 'http://api.travelpayouts.com/data/ru/cities.json'
req = requests.get(url)

if req.status_code == 200:
    print('Обработка данных')
    data = json.loads(req.text)

    print('Обработка параметра')
    result = ''
    for dict_data in data:
        if str == dict_data['name']:
            result = dict_data['code']
            break

    print('IATA код города '+str+ ' - ' + result)
else:
    print('Не удалось получить данные')