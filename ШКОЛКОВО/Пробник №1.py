'''Пробник №1'''

# 2
'''
print('w y z x')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((x <= z) and (z <= w)) or (y ==(x or z)))
                if F == 0:
                    print(w, y, z, x)

# yzwx
'''

# 5
'''
def third(n: int) -> str:
    s = ''
    while n != 0:
        s += str(n%3)
        n //= 3
    return s[::-1]

def ans(n: int) -> int:
    s = third(n)

    if n % 5 == 0:
        s += '02'
    else:
        k = (n % 5) * 3
        m = third(k)
        s += str(m[-2:])

    return int(s, 3)

for n in range(1000):
    if ans(n) == 192:
        print(n)
        print(third(3))
        break
'''

# 6
'''
from turtle import *

tracer(0)
screensize(200*200)
lt(90)

k = 20

for _ in range(2):
    fd(21*k)
    rt(90)
    fd(27*k)
    rt(90)

up()

fd(9*k)
rt(90)
fd(10*k)
lt(90)

down()

for _ in range(2):
    fd(86*k)
    rt(90)
    fd(47*k)
    rt(90)

up()

for x in range(-20, 60):
    for y in range(-20, 60):
        goto(x*k, y*k)
        dot(3, 'red')

done()

# 234
'''

# 8
'''
from itertools import *

s = "АПРСУ"

num = 0
for m in product(s, repeat=5):
    s = ''.join(m)
    num += 1
    if s.count('У') <= 1 and "АА" not in s:
        print(s, num)

# 2969
'''

# 14
'''
def th(n: int) -> int:
    s = ''
    while n != 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]

ml = 0
a = []
for x in range(2, 2026):
    F = 5**2025 + 5**200 - x
    f = th(F)
    if f.count("4") >= ml:
        a.append(x)
        ml = max(ml, f.count("4"))
print(max(a))
# 1876
'''

# 16
'''
import sys
sys.setrecursionlimit(4000)
def f(n: int):
    if n == 1:
        return 1
    return n * f(n-1)

print((f(2024) - f(2023))/f(2022))

# 4092529
'''

# 23
'''
def f(start: int, end: int) -> int:
    d = {}

    for num in range(start, end - 1, -1):
        d[num] = 0


    d[start] = 1

    for key in d.keys():
        if key - 3 in d:
            d[key - 3] += d[key]
        if key - 5 in d:
            d[key - 5] += d[key]
        if key // 3 in d:
            d[key // 3] += d[key]

    return d[end]

print(f(68, 35) * f(35, 14) * f(14, 4))

# 2024
'''

# 24
'''
import re

pattern = r"[ABCDEF]{0,600}"

with open("24__7h6y9.txt") as file:
    text = file.readline()

max_len = 0
for match in re.finditer(pattern, text):
    max_len = max(max_len, match.end() - match.start())

print(max_len)

# 10
'''

# 25
'''
Назовём нетривиальным делителем натурального числа его делитель,
не равный единице и самому числу. Напишите программу, которая
ищет среди целых чисел, принадлежащих числовому отрезку [316312; 451234],
числа, у которых произведение нетривиальных делителей кратно 14.
В ответ укажите количество таких чисел и через пробел сумму цифр
максимального произведения нетривиальных делителей подходящего числа.


import math
def divs(x): # Функция, которая возвращает отсортированный список делителей числа
    d = set() # Множество для хранения делителей
    # Перебираем возможные делители от 2 до корня числа включительно
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: # Если i делитель числа x
            # Добавляем делитель и парный ему в множество
            d |= {i, x//i}
    return sorted(d) # Возвращаем отсортированный список делителей числа x
ans = [] # Список для подходящих чисел
# Перебираем все числа в диапазоне от 316312 до 451234 включительно
for x in range(316312, 451235):
    m = divs(x) # Получим все делители числа
    if len(m) > 0: # Если есть как минимум 1 делитель
        d = math.prod(m)  # Воспользуемся модулем math и функцией prod,
        # которая вычисляет произведение всех элементов списка
        if d % 14 == 0: # Если произведение кратно 14
            ans += [d] # Добавим произведение делителей числа в ответ
# Вывод количества чисел и суммы цифр максимального произведения
# map позволяет перевести max(ans) (максимальное произведение)
# В формат int() (числовой) и найти сумму (с помощью sum())
print(len(ans), sum(map(int,str(max(ans)))))
'''


