import json
import pickle

with open('group.json', 'r', encoding='utf-8') as f:
    data_json = json.load(f)

print('\njson:')
print(type(data_json))
print(data_json)

with open('group.pickle', 'rb') as f:
    data_pickle = pickle.load(f)

print('\npickle:')
print(type(data_pickle))
print(data_pickle)

input('Нажмите Enter для завершения')