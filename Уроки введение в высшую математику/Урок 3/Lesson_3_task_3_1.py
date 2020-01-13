import math
import random

R = random.randint(0,5)
alfa = math.pi / random.randint(1,4)

print(f'Полярные координаты (R,a): ({R},{alfa})')

print(f'Декартовые координаты (x,y): ({R * math.cos(alfa)},{R * math.sin(alfa)})')

