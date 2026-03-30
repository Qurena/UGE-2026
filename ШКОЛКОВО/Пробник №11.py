"""https://3.shkolkovo.online/my/course/7259/dz/28538"""

# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (w and z or (not(w))) and x or y
#                 print(x, y, w, z, int(F))
# # zwyx


# 5
# def t(n):
#     s = ''
#     while n != 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# ans = set()
# for n in range(10000):
#     s = t(n)
#     if n % 3 == 0:
#         s = '1' + s + '02'
#     else:
#         s += t(4*(n % 3))
#     r = int(s, 3)
#     if r <= 350:
#         ans.add(n)
# print(max(ans))
# # 38


# 6
# from turtle import *
# tracer(0)
# lt(90)
# m = 2
# screensize(2000*2000)
# dot(5, 'red')
# for _ in range(11):
#     fd(24*m)
#     lt(90)
#     fd(19*m)
#     lt(90)
# dot(5, 'green')
# up()
# fd(9*m)
# lt(90)
# dot(5, 'green')
# fd(9*m)
# rt(90)
# dot(5, 'green')
# down()
# for _ in range(50):
#     fd(90*m)
#     rt(90)
#     fd(210*m)
#     rt(90)
#
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 638


# 8
# from itertools import *
# s = '123456789ABCDE0'
# ans = 0
# for i in product(s, repeat=8):
#     g = ''.join(i)
#     if g[0] != '0':
#         if g.count('0') == 2:
#             s = sum(1 for i in g if i in 'ABCDE')
#             if s <= 4:
#                 ans += 1
# print(ans)
# # 154248381


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q14': ['0', 'L', 'q1'],
#     'q16': ['0', 'L', 'q1'],
#     'q18': ['1', 'L', 'q1']
# }
#
# s1 = '486'
# s = list('..' + s1 + '..')
# i = -2
# c = 0
# p = 'q0'
#
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(''.join(s))
# # 5992


# 14
# from math import *
# for x in range(40):
#     for y in range(40):
#         F = 5*40**8 + 7*40**7 + x*40**6 + 6*40**5 + 9*40**4 + 2*40**3 + y*40**2 + 1*40**1 + 9*40**0
#         Q = y*40**1 + x*40**0
#         if F % 39 == 0 and sqrt(Q) - int(sqrt(Q)) == 0.0:
#             print(Q)
# # 1521 (0 тоже подходит)


# 15
# def f(a, x, y):
#     return not((3*x + y > 48) or (x > y) or (4*x + y < a))
#
# for a in range(5000):
#     t = [f(a, x, y) for x in range(1000) for y in range(1000)]
#     if all(t):
#         print(a)
# # не знаю, почему не работает

# ans = set()
# for x in range(10000):
#     for y in range(1000):
#         if 3 * x + y <= 48 and x <= y:
#             for a in range(1000):
#                 if 4*x + y >= a:
#                     ans.add(a)
# print(max(ans))
# # 60


# 16
# from functools import *
# @lru_cache(None)
# def f(n):
#     if n <= 5:
#         return 1000
#     return n + 3 + f(n-2)
#
# for n in range(60000):
#     f(n)
#
# print(3 * f(53079) - (f(53077) + f(53075) + f(53073)))
# # 318484


# 17
# f = open("Файлы для пробников/17__8l7b1.txt")
# n = [int(i) for i in f.readlines()]
#
# m = min(i for i in n if len(str(abs(i))) == 4 and i > 0)
#
# mx = count = 0
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     s = sum(1 for p in t if len(str(abs(p))) == 4)
#     if s >= 2 and sum(t) <= m:
#         count += 1
#         mx = max(mx, sum(t))
#         print(t, s, sum(t))
# print(count, mx)
# 2627 1005


# 19
# def steps(p):
#     return [p + 2, p * 3]
#
# def play(p, r):
#     if p >= 27:
#         return r == 0
#
#     if p >= 27 or r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else all(next_steps)
#
# for s in range(1, 27):
#     if play(s, 1):
#         print(s)
# # 9


# 20
# def steps(p):
#     return [p + 2, p * 3]
#
# def play(p, r):
#     if p >= 27:
#         return r == 0
#
#     if p >= 27 or r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else all(next_steps)
#
# for s in range(1, 27):
#     if (not play(s, 1)) and play(s, 3):
#         print(s)
# # 6


# 21
# def steps(p):
#     return [p + 2, p * 3]
#
# def play(p, r):
#     if p >= 27:
#         return r % 2 == 0
#
#     if p >= 27 or r % 2 == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else all(next_steps)
#
# for s in range(1, 27):
#     if not(play(s, 2)) and play(s, 4):
#         print(s)
# # почему код не работает...


# 23
# def sqrt(x):
#     if int(x**0.5)**2 == x:
#         return int(x**0.5)
#     return None
#
# def f(start, end):
#     d = {}
#
#     for i in range(start, end - 1, -1):
#         d[i] = 0
#
#     d[start] = 1
#
#     for key in d.keys():
#         if key - 2 in d:
#             d[key - 2] += d[key]
#         if key - 3 in d:
#             d[key - 3] += d[key]
#         if sqrt(key) in d:
#             d[sqrt(key)] += d[key]
#
#     return d[end]
#
# print(f(25, 3))
# # 238


# 24
# from re import *
# f = open("Файлы для пробников/24__8wpa1.txt")
# s = f.readline()
# pattern = r"(?=(((0|[1-7]+[0-7]*)[*])+(0|[1-7]+[0-7]*)([-](0|[1-7]+[0-7]*))+))"
# mx = 0
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mx = max(mx, len(g))
# print(mx)
# # 71


# 25
# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             return False
#     return True
#
# def m(x):
#     m = 0
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             if prime(i):
#                 m = max(m, i)
#             if prime(x//i):
#                 m = max(m, x//i)
#     return m
#
# ans = set()
# for x in range(1_750_001, 2_000_000):
#     q = m(x)
#     if q <= 15_000 and q % 10 == 7:
#         print(x)
# # 1750001
# # 1750006
# # 1750023
# # 1750041
# # 1750044


# 26
# f = open("Файлы для пробников/1_26__1___8t04v.txt")
# k = int(f.readline())
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# data.sort(key=lambda x: (x[0], x[1]))
#
# cells = [[] for _ in range(k)]
#
# count_goods = 0
# l = []
# for i in range(n):
#     for j in range(k):
#         if cells[j] == [] or cells[j][-1][-1] + 1 <= data[i][0]:
#             cells[j].append(data[i])
#             count_goods += 1
#             if data[i][0] == 999:
#                 l.append(j+1)
#             break
# print(count_goods, min(l))
# # 344 53


# 27
# A:
# from math import dist
# f = open("Файлы для пробников/1_A__5qgt4.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
# r = 0.2
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
# for k in clusters:
#     if len(k) < 200:
#         clusters.remove(k)
#
# # from turtle import *
# # tracer(0)
# # lt(90)
# # m = 10
# # screensize(2000*2000)
# # up()
# # for k in range(3):
# #     for star in clusters[k]:
# #         x, y = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# px = py = 0
# for k in range(3):
#     mx = 0
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if mx < s:
#             mx = s
#             max_star = star
#     px += max_star[0]
#     py += max_star[1]
# px = px/3
# py = py/3
# print(int(px*100), int(py*100))
# # 147 313

# B:
# from math import dist
# f = open("Файлы для пробников/1_B__5qgt7.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
# r = 0.2
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
# for k in clusters:
#     if len(k) < 10:
#         clusters.remove(k)
#
# # from turtle import *
# # tracer(0)
# # lt(90)
# # m = 10
# # up()
# # for k in range(5):
# #     for star in clusters[k]:
# #         x, y = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# px = py = 0
# for k in range(5):
#     mx = 0
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if mx < s:
#             mx = s
#             max_star = star
#     px += max_star[0]
#     py += max_star[1]
# px = px/5
# py = py/5
# print(int(px*100), int(py*100))
# # 1179 946