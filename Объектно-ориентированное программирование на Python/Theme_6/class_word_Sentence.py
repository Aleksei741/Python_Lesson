# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
class Word:
    text = ''

    def __init__(self, text):
        self.text = text


class Sentence:
    content = []

    def __init__(self, content):
        self.content = content

    def show(self, list_words):
        text = ''
        for i in self.content:
            text = '{} {}'.format(text, list_words[i].text)
        text = text.strip(' ')
        text = text.capitalize()
        return text

    def show_parts(self, list_words):
        data_list = []
        for i in self.content:
            data_list.append(list_words[i].part())
        data_list = list(set(data_list))
        return data_list
