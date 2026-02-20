"""https://kompege.ru/variant?kim=25124397 | 3 вариант от Байта"""
# 2
# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 F = not(y <= (z == x)) and (w <= z)
#                 if F == 1:
#                     print(x, y, w, z)
# # ywzx


# 5
# def tw(n):
#     s = ''
#     a = 'ABC'
#     while n != 0:
#         if n % 12 < 10:
#             s += str(n % 12)
#         else:
#             s += a[(n % 12) - 10]
#         n //= 12
#     return s[::-1]
#
# def ans(n):
#     r = tw(n)
#     if n % 4 == 0:
#         r = 'A' + r + 'B'
#     else:
#         r = '1' + r + '0'
#     return int(r, 12)
#
# a = []
# for n in range(10000):
#     if ans(n) > 2025:
#         a.append(ans(n))
# print(min(a))
# # 2028


# 6
# from turtle import *
# m = 8
# tracer(0)
# screensize(200*200)
#
# for _ in range(4):
#     fd(20*m)
#     rt(90)
#     fd(120*m)
#     rt(90)
# up()
# fd(12*m)
# rt(90)
# fd(3*m)
# lt(90)
# down()
#
# for _ in range(3):
#     fd(25*m)
#     rt(90)
#     fd(23*m)
#     rt(90)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 62


# 8
# from itertools import *
# s = 'РПОГА'
# bad = 'ГГ'
#
# n = 0
# for i in product(s, repeat=5):
#     n += 1
#     s = ''.join(i)
#     if s[0] != 'Р' and s.count('Г') == 2 and (bad not in s) and ('О' not in s) and ('А' not in s):
#         print(n)
#         break
# # 704


#


