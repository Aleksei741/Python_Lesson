#1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

op_and = 5 & 6
print(f'and: {op_and}')
op_or = 5 | 6
print(f'or: {op_or}')
op_xor = 5 ^ 6
print(f'xor: {op_xor}')
op1 = 5 << 2
print(f'5 << 2: {op1}')
op2 = 5 >> 2
print(f'5 >> 2: {op2}')