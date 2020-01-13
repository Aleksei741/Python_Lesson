import json
import pickle

my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]
}

print(my_favourite_group)

print('pickle:')
mfg_pickle = pickle.dumps(my_favourite_group)
print(mfg_pickle)
print('\njson:')
mfg_json = json.dumps(my_favourite_group)
print(mfg_json)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

f = open('group.pickle', 'wb')
pickle.dump(my_favourite_group, f)
f.close()

input('Нажмите Enter для завершения')