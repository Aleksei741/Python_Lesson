# 1. Создайте класс Word. (Вспомните, какое зарезервированное слово используется для создания класса).
class Word:
    # 2. Добавьте свойства text (класс будет хранить слово) и part (часть речи, которой является слово. Например, существительное, прилагательное и т.п.). Для добавления свойств воспользуйтесь методом __init__.
    text = ''
    part = ''

    def __init__(self, text, part):
        self.text = text
        self.part = part


# 4. Создайте класс Sentence. (по аналогии с п. 1).
class Sentence:
    # 5. Добавьте свойство content. (по аналогии с п. 2).
    content = []

    def __init__(self, content):
        self.content = content

    # 7. Добавьте в класс Sentence метод show, составляющий предложение.
    # Метод должен перебирать числа из свойства content и подставлять соответствующие слова,
    # которые хранятся в свойстве text экземпляров класса Word.
    # Данные извлекаем из списка words, который получили на прошлом шаге.
    # При соединении слов в предложение не забудьте добавить пробел между словами.
    def show(self, list_words):
        text = ''
        for i in self.content:
            text = '{} {}'.format(text, list_words[i].text)
        text = text.strip(' ')
        text = text.capitalize()
        return text

    # 8. Добавьте в класс Sentence метод show_parts, отображающий, какие части речи входят в предложение.
    # По аналогии с п. 7 перебирайте в цикле числа из свойства content и сохраняйте результат в отдельный список.
    # Учтите, что части речи могут повторяться, но список не должен содержать дубликаты.
    def show_parts(self, list_words):
        data_list = []
        for i in self.content:
            data_list.append(list_words[i].part)
        data_list = list(set(data_list))
        return data_list


if __name__ == '__main__':
    # 3. Создайте экземпляр класса Word, передав в качестве параметров любое слово и указав его часть речи.
    wrd = Word('Идет', 'глагол')
    print(wrd.text, wrd.part)

    # Примечание: список list (назовём его words) — отдельная переменная, не относящаяся к классам Word и Sentence.
    words = [["собака", "сущ"],
             ["ела", "глагол"],
             ["колбасу", "сущ"],
             ["вечером", "наречие"]]

    # 6. Создайте из массива (можете взять приведённый выше или придумать свой) список,
    # каждый элемент которого является экземпляром класса Word.
    list_words = []
    for word in words:
        list_words.append(Word(word[0], word[1]))

    Sntnc = Sentence([0, 1, 2])
    print(Sntnc.show(list_words))
    print(Sntnc.show_parts(list_words))
