"""https://edu.tbank.ru/my-activities/courses/stream/5ef661c0-9ded-4914-afa2-13a1d7b91f9a/practice/012fa3a0-860a-4a08-a6c4-ce2045799d6c/task/1"""


# 2
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(z)) and (y or (not(w))) or (z and w) or (not(x))
#                 if F == 0:
#                     print(x, y, z, w, int(F))
# # wyxz


# 5
# def ans(n):
#     s = bin(n)[2:]
#     if len(s) % 2 != 0:
#         i = len(s)//2
#         s += s[i-1] + s[i] + s[i+1]
#     else:
#         i = len(s)//2
#         s += s[i-1] + s[i]
#
#     return int(s, 2)
#
# a = set()
# for n in range(4, 10000):
#     r = ans(n)
#     if r > 145:
#         a.add(r)
# print(min(a))
# # 149


# 6
# from turtle import *
# lt(90)
# tracer(0)
# m = 20
# screensize(4000, 4000)
#
# for _ in range(4):
#     fd(10*m)
#     back(10*m)
#     rt(90)
# goto(0, 0)
# goto(0*m, 10*m)
# goto(10*m, 10*m)
# goto(10*m, 0*m)
# goto(-10*m, 0*m)
#
# up()
# # for x in range(-10, 10):
# #     for y in range(-5, 11):
# #         if (x)**2 + (y - 5)**2 == 25:
# #             goto(x*m, y*m)
# #             dot(7, 'blue')
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'green')
#
# goto(0, 0)
# done()
# # 147


# 8
# def good(par):
#     fdig = int(par[0])
#     secdig = int(par[1])
#     if fdig + secdig % 2 == 0 and secdig > fdig:
#         return True
#     if fdig + secdig % 2 != 0 and secdig < fdig:
#         return True
#
#     return False
#
# def nine(n):
#     r = ''
#
#     while n != 0:
#         r += str(n % 9)
#         n //= 9
#
#     return r[::-1]
#
# for x in range(31_000_000_000, 33_000_000_000):
#     if len(nine(x)) == 12:
#         print(x)
#
# # print(len(nine(40_000_000_000)))


# 12
# a = {
#     'q0.': ['.', 'R', 'q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q13': ['7', 'R', 'q1'],
#     'q16': ['8', 'R', 'q1'],
#     'q19': ['3', 'R', 'q1']
# }
# s1 = '369'
# s = list('..' + s1 + '..')
# i = 1
# c = 0
# p = 'q0'
#
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i += 1
# print(''.join(s))
# все тройки - 142860


# 13
# from ipaddress import *
#
# ans = 0
# net = ip_network('236.219.208.0/255.255.240.0', 0)
# for ip in net:
#     i = bin(int(ip))[2:].zfill(32)
#     if i.count('1') % 6 != 0:
#         ans += 1
# print(ans)
# # 3535


# 14
# F = 6 * (27**9) + 63 * (81**8) + 7 * (3**8) + 2 * (27**7) - 3 * (9**7) - 2000
#
# def nine(n):
#     r = ''
#     while n != 0:
#         r += str(n % 9)
#         n //= 9
#     return r[::-1]
#
# a = nine(F)
# print(a.count('0'))
# # 7


# 15
# def f(x, A):
#     return (x & 51 != 0) <= ((x & A == 0) <= (x & 25 != 0))
#
# for A in range(1, 1000):
#     t = (f(x, A) for x in range(0, 1000))
#     if all(t):
#         print(A)
#         break
# # 34


# 16
# from sys import *
#
# setrecursionlimit(10**9)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n - 1)
#
# print((f(87654) - 87650 * f(87653))/f(87652))
# # 350612


# 17
# f = open("Файлы для пробников/17214526374857.txt")
# n = [int(i) for i in f]
#
# count = 0
# ans2 = set()
# for i in range(len(n) - 3):
#     t = n[i:i+4]
#     fournine = sum(1 for el in t if abs(el) % 10 == 4 or abs(el) % 10 == 9)
#     sfns = sum(el for el in t if abs(el) % 10 == 4 or abs(el) % 10 == 9)
#     if (fournine == 2) or (fournine == 3):
#         if sfns > (sum(t) - sfns):
#             count += 1
#             ans2.add(sum(t))
# print(count, max(ans2))
# # 667 31843



# 19
# 1 решение:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 81:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 72):
#     p = (9, s)
#     if play(p, 2) and (not(play(p, 1))):
#         print(s)
# # 18


# 2 решение:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 81:
#         return False
#
#     steps = [f(a + 1, b), f(a, b + 1), f(a * 2, b), f(a, b * 2)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for b in range(1, 72):
#     if f(9 + 1, b) == 1 or f(9, b + 1) == 1 or f(9 *2, b) == 1 or f(9, b * 2) == 1:
#         print(b)
# # 18


# 20
# 1 решение:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 81:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 72):
#     p = (9, s)
#     if play(p, 3) and (not(play(p, 1))):
#         print(s)
# # 3135


# 2 решение:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 81:
#         return False
#
#     steps = [f(a + 1, b), f(a, b + 1), f(a * 2, b), f(a, b * 2)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for b in range(1, 72):
#     if f(9, b) == 2:
#         print(b)
# # 3135


# 21
# 1 решение:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 81:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 72):
#     p = (9, s)
#     if play(p, 4) and (not(play(p, 2))):
#         print(s)
# # 30


# 2 решение:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 81:
#         return False
#
#     steps = [f(a + 1, b), f(a, b + 1), f(a * 2, b), f(a, b * 2)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for b in range(1, 72):
#     if f(9, b) == -2:
#         print(b)
# # 30


# 23
# def f(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     return f(start + 3, end) + f(start ** 2, end) + f(start + 5, end)
#
# print(f(10, 26)*f(26, 41)*f(41, 52))
# # 36


# 24
# from re import *
#
# f = open("Файлы для пробников/2412345678.txt")


# 25
# from fnmatch import *
# for n in range(0, 10**9 + 1, 23):
#     if fnmatch(str(n), '12345?7?8'):
#         print(n, n // 23)
# # 123450798 5367426
# # 123451718 5367466
# # 123453788 5367556
# # 123454708 5367596
# # 123456778 5367686
# # 123459768 5367816


# 27A
# from math import *
#
# f = open("Файлы для пробников/1111123456.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f]
# n_clusters = []
# r = 0.1
# print(len(data))
#
# while data:
#     n_clusters.append([data.pop(0)])
#     for i in n_clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 n_clusters[-1].append(j)
#                 data.remove(j)
#
# clusters = []
# for c in n_clusters:
#     if len(c) > 50:
#         clusters.append(c)
#         print(len(c))
#
# print(len(clusters))
#
#
# centers = []
# for k in range(len(clusters)):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#
# px = (centers[0][0] + centers[1][0])/2
# py = (centers[0][1] + centers[1][1])/2
#
# print(int(abs(px*10_000)), int(abs(py*10_000)))
# # 4113 2021
#
# # from turtle import *
# # tracer(0)
# # m = 30
# # lt(90)
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(10*m)
# #     back(10*m)
# #     rt(90)
# #
# # up()
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for x in range(100):
# #     goto(x*m, (2 - x**2)*m)
# #     dot(3, 'green')
# #
# # for x in range(-100, 100):
# #     goto(x*m, x*m)
# #     dot(3, 'purple')
# #
# # for k in range(len(centers)):
# #     x, y = centers[k]
# #     goto(x*m, y*m)
# #     dot(3, 'red')
# #
# # done()


# 27B
# from math import *
#
# f = open("Файлы для пробников/1234567890.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f]
# n_clusters = []
# r = 0.05
# print(len(data))
#
# while data:
#     n_clusters.append([data.pop(0)])
#     for i in n_clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 n_clusters[-1].append(j)
#                 data.remove(j)
#
# clusters = []
# for c in n_clusters:
#     if len(c) > 50:
#         clusters.append(c)
#         print(len(c))
#
# print(len(clusters))
#
# centers = []
# for k in range(len(clusters)):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#
# px = (centers[0][0] + centers[1][0] + centers[2][0] + centers[3][0])/4
# py = (centers[0][1] + centers[1][1] + centers[2][1] + centers[3][1])/4
#
# print(int(abs(px*10_000)), int(abs(py*10_000)))
# # 181 1351
#
# # from turtle import *
# # tracer(0)
# # m = 30
# # lt(90)
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(10*m)
# #     back(10*m)
# #     rt(90)
# #
# # up()
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for x in range(-100, 100):
# #     goto(x*m, (2 - x**2)*m)
# #     dot(3, 'green')
# #
# # for x in range(-100, 100):
# #     for y in range(-100, 100):
# #         if x**2 + y**2 == 1:
# #             dot(3, 'purple')
# #         if y == 1:
# #             dot(3, 'pink')
# #         goto(x*m, (x-1)*m)
# #         dot(3, 'orange')
# #
# #
# # # for k in range(len(centers)):
# # #     x, y = centers[k]
# # #     goto(x*m, y*m)
# # #     dot(3, 'red')
# #
# # done()

