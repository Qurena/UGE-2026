"""Решение пробника №9: https://3.shkolkovo.online/my/course/7259/dz/27821"""

# 2
# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 F = ((x <= (not(y))) and (x or w)) <= (not(z))
#                 if F == 0:
#                     print(x, y, w, z)
# # wyzx


# 5
# def f(n):
#     s = ''
#     while n != 0:
#         s += str(n % 8)
#         n//=8
#     return s[::-1]
#
# def ans(n):
#     k = f(n)
#     if n % 7 == 0:
#         l = k[-2:]
#         k += l
#     else:
#         t = f((n % 7) * 7)
#         k = t + k
#     return int(k, 8)
#
# mn = 10**10
# for n in range(1, 1000):
#     if ans(n) > 500:
#         if ans(n) < mn:
#             mn = ans(n)
#             min_n = n
# print(mn, min_n)
# # 57


# 6
# from turtle import *
#
# m = 15
# tracer(0)
# screensize(200*200)
#
# for _ in range(8):
#     fd(3*m)
#     rt(90)
#     fd(4*m)
#     rt(45)
#     fd(5*m)
#     rt(45)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 30


# 8
# from itertools import *
# s = 'АКОР'
#
# num = 0
# for i in product(s, repeat=5):
#     num += 1
#     s = ''.join(i)
#     print(s, num)
# # КАРРК


# 12
# a = {
#     'q0.': ['.','R','q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q10': ['1', 'R', 'q1'],
#     'q11': ['0', 'R', 'q1']
# }
#
# s1 = '110010'
# s = list('..' + s1 + '..')
# i = 1
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i += 1
# print(''.join(s))
# # 270 (= 1100 - 830)


# 13
# from ipaddress import *
# net = ip_network('127.204.113.250/255.255.254.0', 0)
#
# mn = 10**10
# for ip in net.hosts():
#     mn = min(mn, sum(int(i) for i in str(ip).split('.')))
# print(mn)
# # 444


# 14
# def f(n):
#     s = ''
#     while n != 0:
#         s += str(n % 5)
#         n //= 5
#     return s[::-1]
#
# mx = -1
# for x in range(1, 4001):
#     F = 5**194 + 5**99 - x
#     G = f(F)
#     if G.count('0') == G.count('4'):
#         mx = max(mx, x)
# print(mx)
# # 3951


# 16
# from sys import *
# from functools import *
# setrecursionlimit(10**7)
#
# @lru_cache(None)
# def f(n):
#     if n < 3:
#         return n
#     else:
#         return f(n-2) + f(n-1)
#
# for i in range(5556):
#     f(i)
# print(f(5555)//(f(999)*f(4444)))
# # 352462623835445629070569


# 17
# f = open("Файлы для пробников/17_11__89i2f.txt")
# n = [int(i) for i in f]
# mn = 10**10
# count = 0
# for i in range(len(n)-2):
#     t = [n[i], n[i+1], n[i+2]]
#     if sum(t) % 4 == 0:
#         if (t[0] % 6 == 0 and t[1] % 6 == 0 and t[2] % 6 != 0) or (t[0] % 6 == 0 and t[2] % 6 == 0 and t[1] % 6 != 0) or (t[1] % 6 == 0 and t[2] % 6 == 0 and t[0] % 6 != 0):
#             count += 1
#             mn = min(mn, sum(t))
# print(count, mn)
# # 98 -2240


# 19
# # Первое решение
# def steps(p):
#     return [p + 4, p * 2]
#
# def play(p, r):
#     if p >= 55 and r % 2 == 0:
#         return True
#     if p >= 55 or r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for s in range(1, 55):
#     if play(s, 2):
#         print(s)
# # 27
#
# # Второе решение
# def f(a):
#     if a >= 55:
#         return False
#     t = [f(a+4), f(a*2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 55):
#     if f(s) == -1:
#         print(s)
# # 24


# 20
# Первое решение
# def steps(p):
#     return [p + 4, p * 2]
#
# def play(p, r):
#     if p >= 55 and r % 2 == 0:
#         return True
#     if p >= 55 or r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for s in range(1, 55):
#     if not(play(s, 1)) and play(s, 3):
#         print(s)
# # 1223

# Второе решение
# def f(a):
#     if a >= 55:
#         return False
#     t = [f(a+4), f(a*2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 55):
#     if f(s) != 1 and f(s) == 2:
#         print(s)
# # 1223


# 21
# Первое решение
# def steps(p):
#     return [p + 4, p * 2]
#
# def play(p, r):
#     if p >= 55 and r % 2 == 0:
#         return True
#     if p >= 55 or r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for s in range(1, 55):
#     if (play(s, 4) or play(s, 2)) and not(play(s, 2)):
#         print(s)
# # 16

# Второе решение
# def f(a):
#     if a >= 55:
#         return False
#     t = [f(a+4), f(a*2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 55):
#     if f(s) != -1 and (f(s) == -1 or f(s) == -2):
#         print(s)
# # 16


# 23
# def count(start, end, k1, k2):
#     if start == end and k1 <= 3 and k2 <= 3:
#         return 1
#     if k1 > 3 or k2 > 3:
#         return 0
#     if start > end:
#         return 0
#
#     return count(start + 1, end, k1 + 1, 0) + count(start * 2, end, 0, k2 + 1)
#
# print(count(5, 299, 0, 0))
# # 26


# 24
# f = open("Файлы для пробников/24-1__8ag0n.txt")
# s = f.readline()
# nums = '0123456789'
# cA = cn = start = mx = 0
#
# for end in range(len(s)):
#     if s[end] in nums:
#         cn += 1
#     if s[end] == 'A':
#         cA += 1
#     while cn > 30:
#         if s[start] in nums:
#             cn -= 1
#         if s[start] == 'A':
#             cA -= 1
#         start += 1
#     if cA == 1 and cn == 30 and s[start] == 'A':
#         mx = max(mx, end - start + 1)
# print(mx)
# # 117


# 25
# from fnmatch import *
#
# t = 0
# s = 0
# for n in range(0, 10**10 + 1, 3798):
#     if fnmatch(str(n), '1?57*22'):
#         t += 1
#         s += n
# print(t, s//t)
# # 58 1360526239


# 26
# f = open("Файлы для пробников/26_1__7rls7.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
#
# ndata = []
# for per in data:
#     id = per[0]
#     mid = (sum(per[1:])/4)
#     count = sum(1 for grade in per[1:] if grade == 2)
#     ndata.append([count, mid, id])
#
# datawithouttwo = []
# badsdata = []
# for el in ndata:
#     if el[0] == 0:
#         datawithouttwo.append(el)
#     else:
#         badsdata.append(el)
#
# datawithouttwo.sort(key=lambda x: [x[0], -x[1], x[2]])
# badsdata.sort(key=lambda x: [x[0], x[2]])
# alldata = datawithouttwo + badsdata
# scrudges = alldata[:n//4]
# print(scrudges[-1][-1])
#
# for el in badsdata:
#     if el[0] >= 2:
#         print(el[-1])
#         break
# # 8433 5


# 27
# Файл А
# from math import dist
# f = open('Файлы для пробников/2_A__5kcr9.txt')
# a = [list(map(float, i.replace(',','.').split()))for i in f if 'X' not in i]
# clusters = [[], [], []]
#
# for i in a:
#     x, y = i
#     if y < 0 and x < 0:
#         clusters[0].append(i)
#     if x < 0 and y > 0:
#         clusters[1].append(i)
#     if x > 0:
#         clusters[2].append(i)
# # from turtle import *
# # m = 10
# # tracer(0)
# # up()
# # for k in range(3):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
#
#
# px = py = 0
# for k in range(3):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#             if s < mn:
#                 mn = s
#                 mn_star = star
#     # goto(mn_star[0] * m, mn_star[1] * m)
#     # dot(3, 'red')
#     px += mn_star[0]
#     py += mn_star[1]
# print(int(abs(px/3)*100), int(abs(py/3)*100))
# # done()
# # 240 219


# Файл Б
# from math import dist
# f = open('Файлы для пробников/2_B__5kcra.txt')
# a = [list(map(float, i.replace(',','.').split()))for i in f if 'X' not in i]
# clusters = [[], [], [], [], [], []]
#
# for i in a:
#     x, y = i
#     if x < -6 and y < -11:
#         clusters[0].append(i)
#     if -16 < x < 1 and -11 < y < 4:
#         clusters[1].append(i)
#     if x < -15:
#         clusters[2].append(i)
#     if -6 < x < 8.1 and 10 < y < 24:
#         clusters[3].append(i)
#     if x > 9 and y > 16:
#         clusters[4].append(i)
#     if x > 12 and -8 < y < 8:
#         clusters[5].append(i)
#
# # from turtle import *
# # m = 5
# # tracer(0)
# # up()
# # for k in range(6):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
#
# px = py = 0
# for k in range(6):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#             if s < mn:
#                 mn = s
#                 mn_star = star
#     # goto(mn_star[0] * m, mn_star[1] * m)
#     # dot(3, 'red')
#     px += mn_star[0]
#     py += mn_star[1]
# print(int(abs(px/6)*100), int(abs(py/6)*100))
# # done()
# # 309 347

# Ответ: 240 219 309 347

