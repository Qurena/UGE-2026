"""Решение различных типов № 19-21"""

# Задача на уменьшение кол-ва камней
# 19
'''
https://education.yandex.ru/ege/inf/training/19/task/1?examTaskId=3eb8fd9c-ff99-41d4-9483-f69a66513406&examTaskNumber=19&taskId=9f0ed060-711a-4b44-b245-0d7095166662&categoryId=897bdd8e-5fde-4fc9-b6e9-7ae1810b7099
---------------------------------------------------------------------------
Два игрока, Петя и Ваня, играют в следующую игру.
Перед игроками лежит куча камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может убрать из кучи 5 камней
или уменьшить количество камней в 3 раза. Если количество камней некратно 3,
то в результате хода "уменьшить в 3 раза" остается количество камней равное
результату целочисленного деления текущего количества на 3.

Например, из кучи из 19 камней можно получить кучу из 14 камней или кучу
из 6 камней. Ход разрешается делать только в том случае, если количества
камней в куче достаточно для его совершения.

Игра завершается в тот момент, когда из кучи убирается последний камень.
Победителем считается игрок, сделавший последний ход, т.е. убравший из кучи 
последний камень.

В начальный момент в куче было S камней; S > 0.
Будем говорить, что игрок имеет выигрышную стратегию, если он может
выиграть при любых ходах противника.

Укажите максимальное значение S, при котором Петя не может выиграть
за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
---------------------------------------------------------------------------

from functools import *
def steps(p):
  next_steps = [p // 3]
  if p >= 5:
    next_steps.append(p - 5)
  return next_steps

@lru_cache(None)
def play(p, r):
  if p <= 0:
    return r % 2 == 0
    
  if p <= 0:
    return False
    
  if r == 0:
    return False

  next_plays = []
  for step in steps(p):
      next_plays.append(play(step, r - 1))

  if r - 1 == 1:
    return all(next_plays)
  if r - 1 == 0:
    return any(next_plays)

for s in range(1000, 2, -1):
  if play(s, 2):
    print(s)
# 7
'''

# 20
'''
https://education.yandex.ru/ege/inf/training/20/task/1?examTaskId=02eb39f3-94db-42bc-acc9-4b869c078324&examTaskNumber=20&taskId=effe4fb0-c66b-490a-969e-8dd4a8b71a08&categoryId=6d3a096a-3390-426a-b738-b291cbd85f1d
---------------------------------------------------------------------------
Найдите наименьшее и наибольшее значения S,
при которых у Пети есть выигрышная стратегия,
причём одновременно выполняются два условия:

- Петя не может выиграть за один ход;
- Петя может выиграть своим вторым ходом независимо от того,
как будет ходить Ваня.
---------------------------------------------------------------------------

from functools import *
def steps(p):
  next_steps = [p // 3]
  if p >= 5:
    next_steps.append(p - 5)
  return next_steps

@lru_cache(None)
def play(p, r):
  if p <= 0:
    return r % 2 == 0
  
  if p <= 0:
    return False
    
  if r == 0:
    return False

  next_plays = []
  for step in steps(p):
      next_plays.append(play(step, r - 1))

  if r - 1 == 2:
    return any(next_plays)
  if r - 1 == 1:
    return all(next_plays)
  if r - 1 == 0:
    return any(next_plays)

for s in range(1000, 2, -1):
  if play(s, 3) and (not play(s, 1)):
    print(s)
# 8, 23
'''

# 21
'''
https://education.yandex.ru/ege/inf/training/20/task/1?examTaskId=02eb39f3-94db-42bc-acc9-4b869c078324&examTaskNumber=20&taskId=effe4fb0-c66b-490a-969e-8dd4a8b71a08&categoryId=6d3a096a-3390-426a-b738-b291cbd85f1d
---------------------------------------------------------------------------
Найдите максимальное значение S,
при котором одновременно выполняются два условия:

- у Вани есть выигрышная стратегия,
позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
- у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
---------------------------------------------------------------------------

from functools import *
def steps(p):
  next_steps = [p // 3]
  if p >= 5:
    next_steps.append(p - 5)
  return next_steps

@lru_cache(None)
def play(p, r):
  if p <= 0 and r in (0, 2):
    return True
    
  if p <= 0:
    return False
    
  if r == 0:
    return False

  next_plays = []
  for step in steps(p):
      next_plays.append(play(step, r - 1))

  # if r - 1 == 3:
  #   return all(next_plays)
  # if r - 1 == 2:
  #   return any(next_plays)
  # if r - 1 == 1:
  #   return all(next_plays)
  # if r - 1 == 0:
  #   return any(next_plays)
  
  return any(next_plays) if (r-1) % 2 == 0 else all(next_plays)

for s in range(0, 1000):
  if play(s, 4) and not play(s, 2): # not play(s, 2): у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
    print(s)                             # play(s, 4) и сверху r in (0, 2) - у Вани есть выигрышная стратегия,
                                         # (4 - потому что Ваня выигрывает своим вторым ходом
                                         # 0 - первый ход, а 2 - предпоследний ход выигравшего игрока.)
                                         # позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# 28
'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Alexmath
'''
# https://alex-math.ru/gia/zadaniya-19-21-informatika-yege-2026-statgrad-23102025#

from sys import *

def steps(p):
    return p - 3, p // 5


setrecursionlimit(10000)
def play(p, r):
    if p <= 505:
        return r % 2 == 0

    if p <= 505:
        return False

    if r == 0:
        return False

    next_plays = []
    for step in steps(p):
        next_plays.append(play(step, r - 1))
    if r - 1 == 3:
        return all(next_plays)
    if r - 1 == 2:
        return any(next_plays)
    if r - 1 == 1:
        return all(next_plays)
    if r - 1 == 0:
        return any(next_plays)


for s in range(506, 10000):
    if play(s, 3):
        if not play(s, 1):
            print(s)
# 2533 2534
'''


# 2 КУЧКИ И МУДРЕНЫЕ ХОДЫ (задача 1):
"""
Задача 19-21 (множество команд)
https://education.yandex.ru/ege/inf/task/77aab5b2-72a5-4702-9766-b0630ebb8c11
Ответ: 38
https://education.yandex.ru/ege/inf/task/1d76f57f-5e17-46ba-92bc-37adc56980d7
Ответ: 22, 35
https://education.yandex.ru/ege/inf/task/b021f83e-ca24-4822-aea3-5fcb4969cea4
Ответ: 16
"""
# def steps(p):
#     a, b = p
#     next_steps = []
#     if b > a:  # делаем так, что куча a всегда больше
#         a, b = b, a
#
#     f = lambda x: (x + 1, x + 2, x + 3)  # если мы вызовем функцию f, то она вернет три значения
#
#     next_steps.extend(zip(f(a), [b] * 3))  # zip создает все пары аргументов
#     if a == b:  # extend добавляет несколько значений в список
#         next_steps.extend(zip([a] * 3, f(b)))
#     else:
#         next_steps.append((a, b * 2))
#     return next_steps
#
#
# def play(p, r):
#   if max(p) >= 40 and r in (0, 2):
#     return True
#
#   if max(p) >= 40 or r == 0:
#     return False
#
#   next_plays = [play(p1, r - 1) for p1 in steps(p)]
#
#   return all(next_plays) if r % 2 == 0 else any(next_plays)
#
#
# for s in range(1, 40):
#   p = (s, 31)
#   if play(p, 4) and not play(p, 2):
#     print(s)


# 2 КУЧКИ И МУДРЕНЫЕ ХОДЫ (задача 2):
'''https://education.yandex.ru/ege/inf/task/04a951bf-d429-45bf-ae09-5321c1ac8e73'''
# def steps(p):
#     a, b = p
#     next_steps = [(a, b + 2), (a + 2, b), (a + b, b), (a, b + a)]
#     return next_steps
#
# def play(p, r):
#     if sum(p) >= 180 and r in (0, 2):
#         return True
#
#     if sum(p) >= 180 or r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     if r - 2 == 0:
#         return all(next_plays)
#     if r - 1 == 0:
#         return any(next_plays)
#
# for s in range(1, 161):
#     p = (s, 18)
#     if play(p, 2):
#         print(s)
# # 80

'''https://education.yandex.ru/ege/inf/training/20/task/1?examTaskId=02eb39f3-94db-42bc-acc9-4b869c078324&examTaskNumber=20&taskId=86cf75fa-bb1e-4967-b6b6-beccf119211c&categoryId=d113c406-3195-4315-888c-e40c9e97e5a6'''
# def steps(p):
#   a, b = p
#   next_steps = [(a, b+2), (a+2,b), (a+b, b), (a, b+a)]
#   return next_steps
#
# def play(p, r):
#   if sum(p) >= 180 and r in (0, 2):
#     return True
#
#   if sum(p) >= 180 or r == 0:
#     return False
#
#   next_plays = [play(step, r - 1) for step in steps(p)]
#
#   return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for s in range(1, 161):
#   p = (18, s)
#   if not(play(p, 1)) and play(p, 3):
#     print(s)
# # 62 3

'''https://education.yandex.ru/ege/inf/training/21/task/1?examTaskId=f8058cf8-b8da-4f7a-8c3b-ee63b30347ee&examTaskNumber=21&taskId=35e457ca-93a2-4f56-92ba-17755c68463a&categoryId=3a7d0f4e-32ce-499a-a65d-420f87a288cd'''
# def steps(p):
#   a, b = p
#   next_steps = [(a, b+2), (a+2,b), (a+b, b), (a, b+a)]
#   return next_steps
#
# def play(p, r):
#   if sum(p) >= 180 and r in (0, 2):
#     return True
#
#   if sum(p) >= 180 or r == 0:
#     return False
#
#   next_plays = [play(step, r - 1) for step in steps(p)]
#
#   return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for s in range(1, 161):
#   p = (18, s)
#   # if play(p, 4) and not play(p, 2):
#   #    print(s)
#   if not(play(p, 2)) and (play(p, 2) or play(p, 4)):
#       print(s)
# # 77