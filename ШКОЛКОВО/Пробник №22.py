"""https://3.shkolkovo.online/my/course/7259/dz/31137"""

# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((not(x)) <= y) and (y == (not(z))) and (not(w))
#                 if F == 1:
#                     print(x, y, w, z, int(F))
# # yxzw


# 5
# def ans(n):
#     s = bin(n)[2:]
#     r = s[:-1] + s[1] + s[1]
#     return int(r, 2)
#
# for n in range(10, 100):
#     if ans(n) > 48:
#         print(n, ans(n))
# # 24


# 6
# from turtle import *
# lt(90)
# tracer(0)
# screensize(4000, 4000)
# m = 35
#
# for _ in range(4):
#     fd(5*m)
#     rt(60)
#     fd(8*m)
#     rt(120)
#
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 30


# 8
# from itertools import *
# s = 'ГРОЗА'
#
# c = 0
# for i in product(s, repeat=7):
#     s = ''.join(i)
#     if s.count('З') >= 2:
#         c += 1
# print(c)
# # 33069


# 9
# f = open("Файлы для пробников/012120101.txt")
# c = 0
# for s in f:
#     q = ''
#     for el in s.split():
#         q += el
#
#     if (int(q, 2) % 4 == 0) and (int(q[:3], 2) < int(q[-3:], 2)):
#         c += 1
# print(c)
# # 49


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q00': ['0', 'R', 'q0'],
#     'q01': ['1', 'R', 'q0'],
#     'q1.': ['1', 'S', 'q1'],
#     'q10': ['1', 'S', 'q1'],
#     'q11': ['0', 'L', 'q1']
# }
#
# s1 = '111111111111'
# s = list('..' + s1 + '..')
# i = 2
# c = 0
# p = 'q0'
#
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     if c == 'L':
#         i -= 1
#     if c == 'R':
#         i += 1
# print(''.join(s))
# # 111111111111


# 13
# from ipaddress import *
#
# # ip = ip_address('142.111.21.158')
# # net0 = ip_network('142.111.21.144')
# # for i in range(32):
# #     net = ip_network('142.111.21.158/' + str(i), 0)
# #     if net.network_address == net0.network_address:
# #         print(i)
# # # i = 28
#
# net = ip_network('142.111.21.158/28', 0)
# c = 0
# for p in net:
#     c += 1
# print(c)
# # 16


# 14
# def f(n):
#     s = ''
#     while n != 0:
#         s += str(n % 4)
#         n //= 4
#     return s[::-1]
#
# t = 4**2023 + 4**115 - 3*4**523 - 2378
# print(f(t).count('3'))
# # 1609


# 15
# def f(a, x):
#     return not( (x & a == 0) and (x & 58 != 0) and (x & 22 == 0) )
#
# for a in range(1, 1000):
#     t = (f(a, x) for x in range(1, 1000))
#     if all(t):
#         print(a)
# # 40


# 16
# def f(n):
#     if n > 4_000:
#         return n
#     else:
#         return f(n + 2) * 3 + 5 * n
#
# print(int(f(3988)/f(3998)))
# # 263


# 17
f = open("Файлы для пробников/10__1vf5g.txt")
n = [int(i) for i in f]

c = 0
mns = 10**10
for i1 in range(len(n)):
    for i2 in range(i1 + 1, len(n)):
        # if n[i1] != n[i2]: # по усл. эл-ты различны
        t = [n[i1], n[i2]]
        if abs(t[0] - t[1]) % 2 == 0:
            if t[0] % 11 == 0 or t[1] % 11 == 0:
                c += 1
                mns = min(mns, sum(t))
print(c, mns)
# 4182668 18


# 19
# 1 решение:
# from math import ceil
# def steps(p):
#     h1, h2 = p
#     return [(h1 - 1, h2), (h1, h2 - 1), (ceil(h1 / 2), h2), (h1, ceil(h2 / 2))]
#
# def play(p, r):
#     if sum(p) <= 40:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r -1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(21, 100):
#     p = (20, s)
#     if play(p, 1):
#         print(s)
# # 40

# 2 решение:
# # from functools import lru_cache
# from math import ceil
# from sys import setrecursionlimit
#
# setrecursionlimit(10**9)
#
# # @lru_cache(None)
# def f(a, b):
#     if a + b <= 40:
#         return False
#
#     steps = []
#     if a - 1 > 0:
#         steps.append(f(a-1, b))
#     if b - 1 > 0:
#         steps.append(f(a, b-1))
#     if ceil(a / 2) > 0:
#         steps.append(f(ceil(a / 2), b))
#     if ceil(b / 2) > 0:
#         steps.append(f(a, ceil(a / 2)))
#
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
#
# for s in range(21, 100):
#     if f(20, s) == 1:
#         print(s)
# # почему код не выводит 40...


# 20
# 1 решение:
# from math import ceil
# def steps(p):
#     h1, h2 = p
#     return [(h1 - 1, h2), (h1, h2 - 1), (ceil(h1 / 2), h2), (h1, ceil(h2 / 2))]
#
# def play(p, r):
#     if sum(p) <= 40:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r -1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(21, 200):
#     p = (20, s)
#     if play(p, 3) and (not(play(p, 1))):
#         print(s)
# # 42 82

# 2 решение:
# # from functools import lru_cache
# from math import ceil
# from sys import setrecursionlimit
#
# setrecursionlimit(10**9)
#
# # @lru_cache(None)
# def f(a, b):
#     if a + b <= 40:
#         return False
#
#     steps = []
#     if a - 1 > 0:
#         steps.append(f(a-1, b))
#     if b - 1 > 0:
#         steps.append(f(a, b-1))
#     if ceil(a / 2) > 0:
#         steps.append(f(ceil(a / 2), b))
#     if ceil(b / 2) > 0:
#         steps.append(f(a, ceil(a / 2)))
#
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
#
# for s in range(21, 100):
#     if f(20, s) == 2:
#         print(s)
# # вообще не хочет работать((


# 21
# 1 решение:
# from math import ceil
# def steps(p):
#     h1, h2 = p
#     return [(h1 - 1, h2), (h1, h2 - 1), (ceil(h1 / 2), h2), (h1, ceil(h2 / 2))]
#
# def play(p, r):
#     if sum(p) <= 40:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r -1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(21, 100):
#     p = (20, s)
#     if play(p, 4) and (not(play(p, 2))):
#         print(s)
# # 44

# 2 решение:
# # from functools import lru_cache
# from math import ceil
# from sys import setrecursionlimit
#
# setrecursionlimit(10**9)
#
# # @lru_cache(None)
# def f(a, b):
#     if a + b <= 40:
#         return False
#
#     steps = []
#     if a - 1 > 0:
#         steps.append(f(a-1, b))
#     if b - 1 > 0:
#         steps.append(f(a, b-1))
#     if ceil(a / 2) > 0:
#         steps.append(f(ceil(a / 2), b))
#     if ceil(b / 2) > 0:
#         steps.append(f(a, ceil(a / 2)))
#
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
#
# for s in range(21, 100):
#     if f(20, s) == -2:
#         print(s)
# # такая же история


# 23
# def f(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#
#     return f(start - 1, end) + f(start - 4, end) + f(start // 2, end)
#
# print(f(60, 56)*f(56, 30)*f(30, 18)*f(18, 10))
# # 868140


# 24
# 1 решение:
# from re import *
# f = open("Файлы для пробников/24-280__6eq3c.txt")
# s = f.readline()
#
# pattern = r'(?=(C[^CD]+D))'
#
# mx = 0
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mx = max(mx, len(g))
#
# print(mx)
# # 115

# 2 решение:
# f = open("Файлы для пробников/24-280__6eq3c.txt")
# s = f.readline()
#
# mx = 0
# for i in range(len(s)):
#     for j in range(mx + i, len(s)):
#         t = s[i:j + 1]
#         if t[0] == 'C' and t[-1] == 'D' and t.count('C') == 1 and t.count('D') == 1:
#                     mx = max(mx, len(t))
#         if t[0] != 'C' or t[-1] != 'D' or t.count('C') != 1 or t.count('D') != 1:
#             break
# print(mx) # подскажите пожалуйста, почему код не сработал?


# 25
# def divs(n):
#     div = set()
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             div.add(i)
#             div.add(n//i)
#
#     return sorted(div)
#
# c = 0
# for n in range(3, 30_002):
#     d = divs(n)
#     q = sum(1 for el in d if el % 2 == 0 or el % 3 == 0)
#     if q == 6:
#         c += 1
#
# print(c)
# # 4


# 26
# f = open("Файлы для пробников/26_meteo__6jap6.txt")
# # f = open('test.txt')
# n = int(f.readline())
# data = [int(i) for i in f]
# data.sort()
#
# def met(place, data):
#     meteo = [data[place - 1]]
#     for el in data[place:]:
#         if el - meteo[-1] >= 12:
#             meteo.append(el)
#     return [len(meteo), meteo[0]]
#
# mxcount = 0
# mxstart = 0
# pos = []
#
# for k in range(1, len(data) + 1):
#     pos.append(met(k, data))
#
# mxcount = pos[0][0]
# for el in pos:
#     if el[0] == mxcount:
#         mxstart = max(mxstart, el[1])
# print(mxcount, mxstart)
# # 775 13


# 27A
# from math import dist
#
# f = open("Файлы для пробников/5A__5am9k.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# actual_data = []
# r = 3
# old_clusters = []
# clusters = []
# trash = []
#
# for el in data:
#     if 9 < el[-1] < 13:
#         actual_data.append(el)
#
# while actual_data:
#     old_clusters.append([actual_data.pop(0)])
#     for i in old_clusters[-1]:
#         for j in actual_data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 old_clusters[-1].append(j)
#                 actual_data.remove(j)
# for cl in old_clusters:
#     if len(cl) > 50:
#         clusters.append(cl)
#     else:
#         trash.append(cl)
# # print(len(clusters), len(trash))
#
# centers = []
# px = 0
# py = 0
# for k in range(len(clusters)):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#     px += mn_star[0]
#     py += mn_star[1]
#
# px /= len(centers)
# py /= len(centers)
#
# print(int(abs(px)*500), int(abs(py)*500))
# # 11822 15475
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # screensize(4000, 4000)
# # m = 1
# #
# # up()
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y, s = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(trash)):
# #     for star in trash[k]:
# #         x, y, s = star
# #         goto(x*m, y*m)
# #         dot(6, 'red')
# #
# # for k in range(len(centers)):
# #     x, y, s = centers[k]
# #     goto(x*m, y*m)
# #     dot(6, 'green')
# #
# # done()


# 27B
# from math import dist
#
# f = open("Файлы для пробников/5B__5am9n.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# actual_data = []
# r = 3
# old_clusters = []
# clusters = []
# trash = []
#
# for el in data:
#     if 3 < el[-1] < 8:
#         actual_data.append(el)
#
# while actual_data:
#     old_clusters.append([actual_data.pop(0)])
#     for i in old_clusters[-1]:
#         for j in actual_data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 old_clusters[-1].append(j)
#                 actual_data.remove(j)
# for cl in old_clusters:
#     if len(cl) > 50:
#         clusters.append(cl)
#     else:
#         trash.append(cl)
# print(len(clusters), len(trash))
#
# centers = []
# px = 0
# py = 0
# for k in range(len(clusters)):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#     px += mn_star[0]
#     py += mn_star[1]
#
# px /= len(centers)
# py /= len(centers)
#
# print(int(abs(px)*500), int(abs(py)*500))
# # 22510 12618
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # screensize(4000, 4000)
# # m = 1
# #
# # up()
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y, s = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(trash)):
# #     for star in trash[k]:
# #         x, y, s = star
# #         goto(x*m, y*m)
# #         dot(6, 'red')
# #
# # for k in range(len(centers)):
# #     x, y, s = centers[k]
# #     goto(x*m, y*m)
# #     dot(6, 'green')
# #
# # done()