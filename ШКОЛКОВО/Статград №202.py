"""https://3.shkolkovo.online/my/course/7259/dz/30727"""


# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (w <= y) <= (z <= x) or (not(z))
#                 if y == 1:
#                     print(x, y, w, z, int(F))
# # zywx


# 5
# def t(n):
#     s = ''
#     a = '012'
#     while n != 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# def ans(n):
#     s = t(n)
#     if n % 3 == 0:
#         s = '1' + s + '02'
#     else:
#         k = n % 3
#         s += t(k*4)
#     r = int(s, 3)
#     return r
#
# a = set()
# for n in range(1, 1000):
#     r = ans(n)
#     if r <= 350:
#         a.add(n)
# print(max(a))
# # 38


# 6
# from turtle import *
# tracer(0)
# lt(90)
# m = 0.5
# screensize(2000*2000)
#
# rt(180)
# for _ in range(9):
#     fd(66*m)
#     lt(90)
#     fd(100*m)
#     lt(90)
# up()
# fd(27*m)
# lt(90)
# fd(41*m)
# rt(90)
# down()
# for _ in range(9):
#     fd(120*m)
#     rt(90)
#     fd(99*m)
#     rt(90)
#
# up()
# # for x in range(-30, 30):
# #     for y in range(-30, 30):
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# done()
# # 160


# 8
# def t(n):
#     s = ''
#     a = '0123456789ABCD'
#     while n != 0:
#         s += a[n % 14]
#         n //= 14
#     return s[::-1]
#
# ans = 0
# for x in range(100000, 10000000):
#     s = t(x)
#     g = ['BB', 'CC', 'DD', 'BC', 'CB', 'BD', 'DB', 'DC', 'CD']
#     if len(s) == 6:
#         if s.count('4') >= 1:
#             q = sum(1 for i in s if i in 'BCD')
#             if q == 2:
#                 for el in g:
#                     if el in s:
#                         ans += 1
# print(ans)
# # 196929


# 12
# a = {
#     'q0.': ['.','L','q1'],
#     'q1.': ['.','S','q1'],
#     'q14': ['0', 'L', 'q1'],
#     'q16': ['0', 'L', 'q1'],
#     'q18': ['1', 'L', 'q1']
# }
#
# s1 = '468486848'
# s = list('..' + s1 + '..')
# i = -2
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(''.join(s))
# # 5992


# 13
# from ipaddress import *
#
# net = ip_network('212.184.197.210/255.255.224.0', 0)
#
# for i in net.hosts():
#     ip = bin(int(i))[2:].zfill(32)
#     if ip.count('1') % 5 == 0:
#         print(i)
# # 21218419231


# 14
# from string import *
# for x in digits + ascii_uppercase[:9]:
#     f = int(f'CD{x}34', 19) + int(f'7F{x}2E', 19)
#     if f % 18 == 0:
#         print(x, f//9)
# # 297276


# 16
# def f(n):
#     if n < 4_000:
#         return n
#     if n >= 4_000 and n % 7 == 0:
#         return n + f(n/7)
#     if n >= 4_000 and n % 7 != 0:
#         return 567 + f(n - 3)
#
# for n in range(100_000):
#     if f(n) > 80_000:
#         print(n)
# # 62962


# 17
# f = open("Файлы для пробников/17__8l7b1 (1).txt")
# n = [int(i) for i in f]
# mn = min(i for i in n if i > 0 and len(str(abs(i))) == 4)
#
# ans1 = 0
# ans2 = set()
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     c4 = sum(1 for el in t if len(str(abs(el))) == 4)
#     if c4 >= 2 and sum(t) <= mn:
#         ans1 += 1
#         ans2.add(sum(t))
#
# print(ans1, max(ans2))
# # 2627 1005


# 19
# def steps(p):
#     return [p + 2, p + 3, p * 2]
#
# def play(p, r):
#     if p >= 313:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(1, 313):
#     if (not(play(p, 1))) and play(p, 2):
#         print(p)
# # 311


# 20
# def steps(p):
#     return [p + 2, p + 3, p * 2]
#
# def play(p, r):
#     if p >= 313:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(1, 313):
#     if (not(play(p, 1))) and play(p, 3):
#         print(p)
# # 78 154


# 21
# def steps(p):
#     return [p + 2, p + 3, p * 2]
#
# def play(p, r):
#     if p >= 313:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(1, 313):
#     if (play(p, 2) or play(p, 4)) and (not(play(p, 2))):
#         print(p)
# # 301


# 23
# from math import *
# def f(start, end):
#     if start == end:
#         return True
#     if start < end or start == 61 or start == 122:
#         return False
#     return f(start - 7, end) + f(ceil(start/2), end)
# print(f(300, 40))
# # 12


# 24 (ЖДАТЬ МИНУТ 10)
# from re import *
# from math import inf
#
# f = open("../../ШКОЛКОВО/Практика/Файлы к задачам/24__8l7.txt")
# s = f.readline()
# pattern = '[A-Z](?=(([0-9]+[A-Z]+){9999}[0-9]+[A-Z]))'
#
# mn = inf
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mn = min(mn, len(g)+1)
#     print(mn)
# # 68613


# 25
# from fnmatch import *
#
# ans = []
# for t in range(0, 10**10+1, 2026):
#     x = str(t)
#     if fnmatch(x, '5?34?71*2') and int(x[1]) % 2 != 0 and int(x[4])% 2 != 0:
#         ans.append(t)
# print(*ans)
# # 553497122 5134171692 5134971962 5734171592 5734971862


# 26
# f = open("Файлы для пробников/26__8lb2q.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# data.sort(key=lambda x: x[0])
#
# intervals = []
# cend = data[0][1]
# cstart = data[0][0]
#
# for start, end in data[1:]:
#     if start <= cend:
#         cend = max(end, cend)
#     else:
#         intervals.append([cstart, cend])
#         cstart, cend = start, end
# intervals.append([cstart, cend])
#
# sm = 0
# for k in intervals:
#     sm += k[1] - k[0]
# print(len(intervals), sm)
# # 359 86023641


# 27
# Файл A:
# from math import dist
# f = open('Файлы для пробников/27A__8xikf.txt')
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# print(f'stars amount:{len(a)}')
# clusters = []
# nclusters = []
# r = 0.6
#
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# for c in clusters:
#     if len(c) > 100:
#         print(f'len(c):{len(c)}')
#         nclusters.append(c)
# print(f'clusters amount:{len(nclusters)}')
#
# diam = []
# px1 = px2 = 0
# py1 = py2 = 0
# for k in range(len(nclusters)):
#     mx = 0
#     for star in nclusters[k]:
#         for i in nclusters[k]:
#             if dist(star, i) > mx:
#                 mx = dist(star, i)
#                 d1 = star
#                 d2 = i
#     diam.append([d1, d2, mx])
#     if k == 0:
#         px1 += d1[0] + d2[0]
#         py1 += d1[1] + d2[1]
#     if k == 1:
#         px2 += d1[0] + d2[0]
#         py2 += d1[1] + d2[1]
# print(int(abs(max(px1, px2)*10_000)), int(abs(max(py1, py2)*10_000)))
# # 442426 428913


# Файл B:
# from math import dist
# f = open('Файлы для пробников/27B__8xiki.txt')
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# print(f'stars amount:{len(a)}')
# clusters = []
# nclusters = []
# trash = []
# r = 0.6
#
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# for c in clusters:
#     if len(c) > 100:
#         print(f'len(c):{len(c)}')
#         nclusters.append(c)
#     else:
#         trash.append(c)
# print(f'clusters amount:{len(nclusters)}')
# print(f'trash amount:{len(trash)}')
#
# # from turtle import *
# # tracer(0)
# # m = 15
# # lt(90)
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# # screensize(4000, 4000)
# #
# # up()
# # for k in range(len(nclusters)):
# #     for i in nclusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # for k in range(len(trash)):
# #     for i in trash[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(7, 'green')
# # done()
#
#
# diam = []
# dots = []
# for k in range(len(nclusters)):
#     mx = 0
#     for star in nclusters[k]:
#         for i in nclusters[k]:
#             if dist(star, i) > mx:
#                 mx = dist(star, i)
#                 d1 = star
#                 d2 = i
#     diam.append([d1, d2, mx])
#     dots.append(d1)
#     dots.append(d2)
#
# q1 = diam[2][-1]
# q2 = 0
# for dot1 in dots:
#     for dot2 in dots:
#         q2 = max(q2, dist(dot1, dot2))
#
# print(int(q1*10_000), int(q2*10_000))
# # 30588 488624

