from wiki_requests import get_topic_page
import re


def get_topic_words(topic):
    html_content = requests.get(link).text
    # with open('new.html', 'w', encoding='utf-8') as f:
    # f.write(html_content)
    return html_content
    words = re.findall('[а-яА-Я-\']{3,}', html_content)
    return words


def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[0:50]:
        print(w[0])


def main():
    topic = input('Topic: ')
    visualize_common_words(topic)
