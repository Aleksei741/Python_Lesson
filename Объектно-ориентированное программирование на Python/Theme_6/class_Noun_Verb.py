from class_word_Sentence import Word, Sentence


# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
# Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное),
# а для Verb — «гл» (сокращение от глагол). Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.
class Noun(Word):
    __grammar = 'сущ'

    # 6. Допишите в класс Noun метод part. Данный метод должен возвращать строку с полным названием части речи.
    def part(self):
        return self.__grammar


class Verb(Word):
    __grammar = 'гл'

    # 6. Допишите в класс Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
    def part(self):
        return self.__grammar

    
if __name__ == '__main__':
    words = []
    words.append(Noun("собака"))
    words.append(Verb("ела"))
    words.append(Noun("колбасу"))
    words.append(Noun("кот"))

    Sntnc = Sentence([0, 1, 2])
    # 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
    print(Sntnc.show(words))
    # 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
    print(Sntnc.show_parts(words))
