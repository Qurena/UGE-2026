"""Решение ДЗ к вебу https://3.shkolkovo.online/my/course/7259/materials/lesson/34222"""

# 1-3
'''
from functools import *

@lru_cache(None)
def f(a:int) -> int:
    if a >= 39:
        return 0

    t = [f(a+1), f(a+2), f(a*2)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    return -max(t)

for i in range(1, 39):
    if (f(i) == -1 or f(i) == -2) and f(i) != -1:
        print(i)
'''

# 4-6
'''
from functools import *


@lru_cache(None)
def f(a: int, b: int) -> int:
    if a + b >= 43:
        return 0

    t = [f(a + 2, b), f(a * 3, b), f(a, b + 2), f(a, b * 3)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    return -max(t)


for i in range(1, 37):
    if (f(6, i) == -1 or f(6, i) == -2) and f(6, i) != -1:
        print(i)
'''

#7-9
'''
from functools import lru_cache
@lru_cache(None)
def game(a, b, c): # Функция игры.
    # c - счётчик ходов в партии, его мы добавили для того,
    # чтобы избежать ошибки превышения лимита рекурсии.
    # Это работает следующим образом: если в партии больше 6 ходов, а партия не завершена,
    # то такая партия нам не подходит, поскольку в задачах у нас просят значения,
    # при которых Ваня или Петя побеждают максимум третьим ходом.
    if a + b >= 2048: # Если произведение камней в кучах стало больше 2047
        return 0 # Прекращаем игру
    if c > 6: # Если в игре больше 6 ходов
        return 10**10 # Прерываем игру
    # Генерация всех возможных ходов
    moves = [game(a, b + 1, c+1), game(a, b * 2, c+1),
             game(a + 1, b, c+1),game(a * 2, b, c+1)]
    petya_win = [i for i in moves if i <= 0]
    if petya_win: # Если в данной позиции есть выигрыш Пети
        return -max(petya_win) + 1
    else: # Если в данной позиции выигрыш Вани
        return -max(moves)


for i in range(1,187):
    # Если в данной позиции возможен выигрыш Вани первым ходом
    if game(11, i, 0) == -1:
        print(i)
        break
'''
