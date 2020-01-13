import requests


def get_link(topic):
    link = 'https://ru.wikipedia.org/wiki/' + topic.capitalize()
    return link


def get_topic_page(topic):
    link = get_link(topic)
    html_content = requests.get(link).text
    #with open('new.html', 'w', encoding='utf-8') as f:
        #f.write(html_content)
    return html_content
