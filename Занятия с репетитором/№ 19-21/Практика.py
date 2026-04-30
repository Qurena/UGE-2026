"""ДЗ по номерам 19-21"""

# 1
'''Задача 19 #76979
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по оче-
реди, первый ход делает Петя. За один ход игрок может добавить в кучу три камня или увеличить количество
камней в 4 раза. Игра завершается в тот момент, когда количество камней куче становится не менее 100. Игрок,
который получил 120 и более камней, считается проигравшим. В начальный момент в куче было S камней;
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах против-
ника. Укажите минимальное значение S, при котором Петя выигрывает, совершив всего лишь один ход.

Задача 20 #76980
Для игры, описанной в задании 19, найдите такое значение S, при котором у Вани есть выигрышная стратегия,
причём одновременно выполняются два условия:
— Ваня не может гарантированно выиграть, совершив один ход;
— Ваня может выиграть, совершив не более двух ходов, независимо от того, как будет ходить Петя.

Задача 21 #76981
Найдите два значения S, при которых одновременно выполняются два условия:
– у Пети есть выигрышная стратегия, позволяющая ему выиграть первым, вторым или третьим ходом при лю-
бой игре Вани;
– у Пети нет стратегии, которая позволит ему гарантированно выиграть первым или вторым ходом.
Ответы укажите в порядке возрастания.'''
# 19
# def steps(p):
#     return p + 3, p * 4
#
# def play(p, r):
#     if 120 > p >= 100:
#         return r % 2 == 0
#
#     if p >= 120 and r % 2 == 0: # наш победитель не может перейти через границу (он проиграет)
#         return False
#
#     if p >= 120 and r % 2 == 1: # его соперник может перейти через границу (если Ваня проиграл, то Петя выиграл)
#         return True
#
#     if r == 0: # окончание игры
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else all(next_plays)
#
# for s in range(1, 61):
#     if play(s, 1):
#         print(s)
#         break
# # 25


# 20
# def steps(p):
#     return p + 3, p * 4
#
# def play(p, r):
#     if 120 > p >= 100:
#         return r % 2 == 0
#
#     if p >= 120 and r % 2 == 0: # наш победитель не может перейти через границу (он проиграет)
#         return False
#
#     if p >= 120 and r % 2 == 1: # его соперник может перейти через границу (если Ваня проиграл, то Петя выиграл)
#         return True
#
#     if r == 0: # окончание игры
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else all(next_plays)
#
# for s in range(1, 61):
#     if play(s, 4) and not play(s, 2):
#         print(s)
# # 23


# 21
# def steps(p):
#     return p + 3, p * 4
#
# def play(p, r):
#     if 120 > p >= 100:
#         return r % 2 == 0
#
#     if p >= 120 and r % 2 == 0: # наш победитель не может перейти через границу (он проиграет)
#         return False
#
#     if p >= 120 and r % 2 == 1: # его соперник может перейти через границу (если Ваня проиграл, то Петя выиграл)
#         return True
#
#     if r == 0: # окончание игры
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else all(next_plays)
#
# for s in range(1, 61):
#     if play(s, 5) and not play(s, 1) and not play(s, 3):
#         print(s)
# # 2022


'''----------------------------------------------------------------------------------------------------------------------------------'''

'''https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=8939'''

# 19
# решение 1:
# from math import prod
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 3, h2), (h1, h2 + 3), (h1 + 13, h2), (h1, h2 + 13)]
#
# def play(p, r):
#     if prod(p) >= 516:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else any(next_plays)
#
# ans = 0
# for s in range(1, 74):
#     p = (7, s)
#     if play(p, 2):
#         ans += 1
# print(ans)
# # 58

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a*b >= 516:
#         return 0
#
#     next_steps = [f(a + 3, b), f(a, b + 3), f(a + 13, b), f(a, b + 13)]
#     win_check = [i for i in next_steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(next_steps)
#
# ans = 0
# for s in range(1, 74):
#     if f(7 + 3, s) == 1 or f(7, s + 3) == 1 or f(7 + 13, s) == 1 or f(7, s + 13) == 1:
#         ans += 1
# print(ans)
# # 58


# 20
# решение 1:
# from math import prod
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 3, h2), (h1, h2 + 3), (h1 + 13, h2), (h1, h2 + 13)]
#
# def play(p, r):
#     if prod(p) >= 516:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 74):
#     p = (7, s)
#     if (not(play(p, 1))) and play(p, 3):
#         print(s)
# # 10 11

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a*b >= 516:
#         return 0
#
#     next_steps = [f(a + 3, b), f(a, b + 3), f(a + 13, b), f(a, b + 13)]
#     win_check = [i for i in next_steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(next_steps)
#
# for s in range(1, 74):
#     if f(7, s) == 2:
#         print(s)
# # 10 11


# 21
# решение 1:
# from math import prod
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 3, h2), (h1, h2 + 3), (h1 + 13, h2), (h1, h2 + 13)]
#
# def play(p, r):
#     if prod(p) >= 516:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 74):
#     p = (7, s)
#     if (not(play(p, 2))) and play(p, 4):
#         print(s)
# # 19

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a*b >= 516:
#         return 0
#
#     next_steps = [f(a + 3, b), f(a, b + 3), f(a + 13, b), f(a, b + 13)]
#     win_check = [i for i in next_steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(next_steps)
#
# for s in range(1, 74):
#     if f(7, s) == -2:
#         print(s)
# # 19


'''----------------------------------------------------------------------------------------------------------------------------------'''

'''https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=8671'''


# 19
# решение 1:
# def steps(p):
#     return [(p + 234), (p + 411), (p * 2)]
#
# def play(p, r):
#     if p >= 1500:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# ans = 0
# for p in range(1, 1500):
#     if play(p, 2) and (not(play(p, 1))):
#         ans += p
# print(ans)
# # 148005


# решение 2:
# def f(a):
#     if a >= 1500:
#         return 0
#
#     next_steps = [f(a + 234), f(a + 411), f(a * 2)]
#
#     win_check = [i for i in next_steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(next_steps)
#
# ans = 0
# for s in range(1, 1500):
#     if f(s) == -1:
#        ans += s
# print(ans)
# # 148005


# 20
# решение 1:
# def steps(p):
#     return [(p + 234), (p + 411), (p * 2)]
#
# def play(p, r):
#     if p >= 1500:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(1, 1500):
#     if play(p, 3) and (not(play(p, 1))):
#         print(p)
# # 105 515


# решение 2:
# def f(a):
#     if a >= 1500:
#         return 0
#
#     next_steps = [f(a + 234), f(a + 411), f(a * 2)]
#
#     win_check = [i for i in next_steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(next_steps)
#
# for s in range(1, 1500):
#     if f(s) == 2:
#        print(s)
# # 105 515


# 21
# решение 1:
# def steps(p):
#     return [(p + 234), (p + 411), (p * 2)]
#
# def play(p, r):
#     if p >= 1500:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# ans = 0
# for p in range(1, 1500):
#     if play(p, 4) and (not(play(p, 2))):
#         ans += p
# print(ans)
# # 4082


# решение 2:
# def f(a):
#     if a >= 1500:
#         return 0
#
#     next_steps = [f(a + 234), f(a + 411), f(a * 2)]
#
#     win_check = [i for i in next_steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(next_steps)
#
# ans = 0
# for s in range(1, 1500):
#     if f(s) == -2:
#        ans += s
# print(ans)
# # 4082


'''----------------------------------------------------------------------------------------------------------------------------------'''

'''https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=8462'''


#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 19
# решение 1:
# def steps(p):
#     black, white = p
#     return [(black, white + 1), (black, white + 2), (black + 1, white), (black + 2, white)]
#
# def play(p, r):
#     if sum(p) > 7:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else any(next_plays)
#
# ans = set()
# for black in range(0, 7):
#     for white in range(0, 7):
#         p = (white, black)
#         if play(p, 2) and (not(play(p, 1))) and sum(p) <= 7:
#             ans.add(p)
# print(len(ans))
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


'''----------------------------------------------------------------------------------------------------------------------------------'''

'''https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=8433'''

# 19
# def steps(p):
#     next_steps = [(p // 2)]
#     if p - 2 > 0:
#         next_steps.append((p - 2))
#     if p - 4 > 0:
#         next_steps.append((p - 2))
#     return next_steps
#
# def play(p, r):
#     if 0 <= p <= 3:
#         if p % 2 == 0:
#             return p % 2 == 0
#         if p % 2 != 0:
#             return p % 2 != 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(3, 100):
#     if play(p, 3) and not(play(p, 1)):
#         print(p)
# # 19


# 20
# def steps(p):
#     next_steps = [(p // 2)]
#     if p - 2 > 0:
#         next_steps.append((p - 2))
#     if p - 4 > 0:
#         next_steps.append((p - 2))
#     return next_steps
#
# def play(p, r):
#     if 0 <= p <= 3:
#         if p % 2 == 0:
#             return p % 2 == 0
#         if p % 2 != 0:
#             return p % 2 != 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(3, 100):
#     if play(p, 4) and not(play(p, 2)):
#         print(p)
# # 10 11