import re

with open('test.sql', 'r', encoding = 'utf-8') as f:
    data = f.read()
print (data)

print()

pattern = re.compile('[\.!?]\s')
proposal = re.split(pattern, data)
#proposal = re.findall(pattern, data)
print('Предложения:')
for i in proposal:
    print(i)

print()

pattern2 = re.compile('[а-яА-Я]{4,}')
word_data = pattern2.findall(data)
word_all = list(set(word_data))
word = []
for i in range(len(word_all)):
    word.append([word_all[i], word_data.count(word_all[i])])
word.sort(key = lambda n: n[1], reverse=True)
word10 = word[:10]
print('10 самых часто используемых слов: ',end='')
print(word10)

print()

pattern_link = re.compile('\s{1}([0-9a-zA-Z\.]*\.ru\/*\w*)')
link = pattern_link.findall(data)
print('Используемые ссылки: ', end='')
print(link)

print()

pattern_domane_name = re.compile('\s{1}([0-9a-zA-Z\.]*\.ru)')
domane_name_data = pattern_domane_name.findall(data)
domane_name_all = list(set(domane_name_data))
domane_name = []
for i in domane_name_all:
    domane_name.append([i, domane_name_data.count(i)])
domane_name.sort(key = lambda n: n[1], reverse=True)
print('Самый частый домен: ', end='')
print(domane_name[0])

print()

data_out = re.sub(pattern_link, '«Ссылка отобразится после регистрации»', data)
print(data_out)
