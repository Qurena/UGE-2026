"""Решение ДЗ к вебу https://3.shkolkovo.online/my/course/7259/materials/lesson/34222
+ ДЗ: https://3.shkolkovo.online/my/course/7259/dz/28539
"""

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

# ----------------------------------------------------------------------------------------------------------------------
# https://3.shkolkovo.online/my/course/7259/dz/28539
# 1 (19.1) | Странные ходы
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 132:
#         return 0
#
#     steps = [f(p + 1)]
#     if p % 2 == 0:
#         steps.append(f(p + p // 2))
#     if p % 3 == 0:
#         steps.append(f(p + p // 3))
#     if p % 2 != 0 and p % 3 != 0:
#         steps.append(f(p * 2))
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p in range(1, 132):
#     if f(p) == -1:
#         print(p)
# # 66


# 2 (20.1)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 132:
#         return 0
#
#     steps = [f(p + 1)]
#     if p % 2 == 0:
#         steps.append(f(p + p // 2))
#     if p % 3 == 0:
#         steps.append(f(p + p // 3))
#     if p % 2 != 0 and p % 3 != 0:
#         steps.append(f(p * 2))
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p in range(1, 132):
#     if f(p) == 2:
#         print(p)
# # 81 86


# 3 (21.1)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 132:
#         return 0
#
#     steps = [f(p + 1)]
#     if p % 2 == 0:
#         steps.append(f(p + p // 2))
#     if p % 3 == 0:
#         steps.append(f(p + p // 3))
#     if p % 2 != 0 and p % 3 != 0:
#         steps.append(f(p * 2))
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p in range(1, 132):
#     if f(p) == -2:
#         print(p)
# # 80

# ----------------------------------------------------------------------------------------------------------------------

# 4 (19.2)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 313:
#         return 0
#
#     steps = [f(p + 2), f(p + 3), f(p * 2)]
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# ans = 0
# for p in range(1, 313):
#     if f(p) == -1:
#         ans += p
# print(ans)
# # 311


# 5 (20.2)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 313:
#         return 0
#
#     steps = [f(p + 2), f(p + 3), f(p * 2)]
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p in range(1, 313):
#     if f(p) == 2:
#         print(p)
# # 78 154


# 6 (21.2)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 313:
#         return 0
#
#     steps = [f(p + 2), f(p + 3), f(p * 2)]
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# ans = 0
# for p in range(1, 313):
#     if f(p) == -2:
#         ans += p
# print(ans)
# # 301

# ----------------------------------------------------------------------------------------------------------------------

# 7 (19.3)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 47:
#         return 0
#
#     steps = [f(p + 2), f(p + 5), f(p * 2)]
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p in range(1, 47):
#     if f(p) == -1:
#         print(p)
# # 22


# 8 (20.3)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 47:
#         return 0
#
#     steps = [f(p + 2), f(p + 5), f(p * 2)]
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p in range(1, 47):
#     if f(p) == 2:
#         print(p)
# # 11 21


# 9 (21.3)
# from functools import *
#
# @lru_cache(None)
# def f(p):
#     if p >= 47:
#         return 0
#
#     steps = [f(p + 2), f(p + 5), f(p * 2)]
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# ans = 0
# for p in range(1, 47):
#     if f(p) == -2:
#         ans += 1
# print(ans)
# # 3

# ----------------------------------------------------------------------------------------------------------------------

# 10 (19.4) | 2 кучки + убывание
'''
Перебираем все p2 от 150 до 2000.
После этого, мы вместо Пети делаем все возможные первые ходы.
Это меняет порядок ходов внутри функции, теперь для функции F первым ходит Ваня,
и положительное число k - победа Вани его k-м ходом.
Если game(17, p2 - 2) == 1 или game(17, p2 // 3) == 1 или game(17 - 2, p2) == 1
или game(17 // 3, p2) == 1, это значит: Петя сделает неудачный ход,
а Ваня выигрывает первым своим ходом. Такие p2 выводим.
'''
# from functools import *
#
# @lru_cache(None)
# def f(p1, p2):
#     if p1 + p2 <= 165:
#         return 0
#
#     steps = [f(p1 - 2, p2)]
#     # if p1 - 2 > 165:
#     #     steps.append(f(p1 - 2, p2))
#     if p2 >= 2:
#         steps.append(f(p1, p2 - 2))
#     if p1 >= 3:
#         steps.append(f(p1 // 3, p2))
#     if p2 >= 3:
#         steps.append(f(p1, p2 // 3))
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p2 in range(150, 2000):
#     p1 = 17
#     if f(p1, p2 - 2) == 1 or f(p1, p2 // 3) == 1 or f(p1 - 2, p2) == 1 or (p1 // 3, p2) == 1:
#         print(p2)
# # 1340


# 11 (20.4)
# from functools import *
#
# @lru_cache(None)
# def f(p1, p2):
#     if p1 + p2 <= 165:
#         return 0
#
#     steps = [f(p1 - 2, p2)]
#     # if p1 - 2 > 165:
#     #     steps.append(f(p1 - 2, p2))
#     if p2 >= 2:
#         steps.append(f(p1, p2 - 2))
#     if p1 >= 3:
#         steps.append(f(p1 // 3, p2))
#     if p2 >= 3:
#         steps.append(f(p1, p2 // 3))
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p2 in range(150, 2000):
#     p1 = 17
#     if f(p1, p2) == 2:
#         print(p2)
# # 449 450


# 12 (21.4)
# from functools import *
#
# @lru_cache(None)
# def f(p1, p2):
#     if p1 + p2 <= 165:
#         return 0
#
#     steps = [f(p1 - 2, p2)]
#     # if p1 - 2 > 165:
#     #     steps.append(f(p1 - 2, p2))
#     if p2 >= 2:
#         steps.append(f(p1, p2 - 2))
#     if p1 >= 3:
#         steps.append(f(p1 // 3, p2))
#     if p2 >= 3:
#         steps.append(f(p1, p2 // 3))
#
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for p2 in range(150, 2000):
#     p1 = 17
#     if f(p1, p2) == -2:
#         print(p2)
# # 451