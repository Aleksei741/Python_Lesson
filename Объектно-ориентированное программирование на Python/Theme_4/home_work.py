from wiki_requests import get_topic_page
import requests
import re
from bs4 import BeautifulSoup as BS


def get_all_link_wiki(topic):
    html_data = get_topic_page(topic)
    data = BS(html_data, 'html.parser')
    result = []
    print(type(result))
    pattern = re.compile('((https://ru.wikipedia.org/)|(/))wiki/[\S:]*')
    for link in data.find_all('a'):
        if pattern.match(link.get('href', '')):
            result.append(link.get('href', ''))
    return result


def get_link(link):
    if re.match('/wiki/', link):
        return 'https://ru.wikipedia.org' + link
    else:
        return link

def get_topic_words(topic):
    link = 'https://ru.wikipedia.org/wiki/' + topic.capitalize()
    html_content = requests.get(link).text
    words = re.findall('[а-яА-Я-\']{3,}', html_content)

    wiki_link_list = get_all_link_wiki(topic)  # Получаем список ссылок на сайт википедии

    for link in wiki_link_list:  # Перебираем список и получаем слова
        print(get_link(link))
        html_content = requests.get(get_link(link))
        if html_content.status_code == 200:
            words_this_Link = re.findall('[а-яА-Я-\']{3,}', html_content.text)
            print(words_this_Link)
            print(len(words_this_Link))
            words.extend(words_this_Link)
            print('Длина общего списка слов ', len(words))
    return words

def visualize_common_words(words_list):
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list

if __name__ == '__main__':

    topic = input('Введите топик: ')
    words = get_topic_words(topic)
    rate_list = visualize_common_words(words)
    print(rate_list[50:100])





