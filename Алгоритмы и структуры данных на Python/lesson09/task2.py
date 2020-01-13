# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def huffman_code_symbol(s):
    mas = []
    for ch, freq in Counter(s).items():
        mas.append((freq, Leaf(ch)))
    mas.sort(key=lambda x: x[0], reverse=True)

    while len(mas) > 1:
        freq1, left = mas.pop()
        freq2, right = mas.pop()
        mas.append((freq1 + freq2, Node(left, right)))
        mas.sort(key=lambda x: x[0], reverse=True)

    code = {}
    if mas:
        root = mas[0][1]
        root.walk(code, "")
    return code


def huffman_code(s, code):
    code_str = ''
    for ch in s:
        code_str += ''.join(code[ch])

    return code_str


def huffman_decode(data, table):
    result = ''
    ch = ""
    for i in data:
        ch += i
        if ch in table.values():
            result += ''.join(get_key(table, ch))
            ch = ''
    return result


if __name__ == "__main__":
    s = input('Введите строку ')
    # s = 'ghjf hfshag ;lsdkjgfhd;ls hdslghs lh[aigrio ghafck gf'
    table = huffman_code_symbol(s)

    code_str = huffman_code(s, table)

    print(f'Исходная строка {s}')
    print(f'Закодированная {code_str}')
    print(f'Таблица')
    for ch in table:
        print(f"Cимвол: {ch} Код: {table[ch]}")

    print(f'Раскодированная строка {huffman_decode(code_str, table)}')
