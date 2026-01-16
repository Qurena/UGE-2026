"""Решение пробника №6: https://3.shkolkovo.online/my/course/7259/dz/27114"""


# 2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(w)) <= ((y or (not(z))) == (x <= (not(y))))
#                 if F == 0:
#                     print(x, y, z, w)
# # yzwx


# 5
# def f(n:int) -> int:
#     s = str(n)
#     k1 = int(s[0]) + int(s[1])
#     k2 = int(s[1]) + int(s[2])
#     if k1 >= k2:
#         return int(str(k2) + str(k1))
#     return int(str(k1) + str(k2))
#
# a = []
# for n in range(100, 1000):
#     if f(n) == 814:
#         a.append(n)
# print(max(a))
# # 953


# 6
# from turtle import *
# m = 20
# tracer(0)
# screensize(200*200)
# lt(90)
#
# for _ in range(3):
#     fd(7*m)
#     rt(120)
#
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(1.5, 'blue')
# done()
# # 18


# 8
# from itertools import product
# s = 'МИРАЖ'
#
# ans = 0
# for i in product(s, repeat=5):
#     k = ''.join(i)
#     g1 = k.count('И')
#     g2 = k.count('А')
#     if g1 <= 1 and g2 <= 1:
#         ans += 1
#         print(k)
# print(ans)
# # 1593


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q11': ['0', 'S', 'q1'],
#     'q10': ['1', 'L', 'q1']
# }
#
# s1 = '11011'
# s = list('..' + s1 + '..')
# i = -2
# c = 0
# q = 'q0'
# while c != 'S':
#     s[i], c, q = a[q + s[i]]
#     i -= 1
# print(''.join(s))
# # 505


# 13
# from ipaddress import *
#
# net = ip_network('112.208.0.0/255.255.224.0', 0)
# ans = 0
# for ip in net:
#     s = bin(int(ip))[2:].zfill(32)
#     if int(s[-3]) == int(s[-2]) == int(s[-1]):
#         ans += 1
#         print(ip, s)
# print(ans)
# # 2048


# 14
# def sev(n: int) -> str:
#     s = ''
#     while n != 0:
#         s += str(n % 7)
#         n //= 7
#     return s[::-1]
#
# ans = []
# for x in range(1, 2031):
#     n = 7**170 + 7**100 - x
#     if sev(n).count('0') == 71:
#         ans.append(x)
# print(max(ans))
# # 2029


# 16
# from sys import *
# setrecursionlimit(10**6)
# def f(n:int) -> int:
#     if n >= 50_000:
#         return 2
#     elif n % 2 == 0 and n < 50_000:
#         return f(n+2) - n
#     return f(n+2) + 7
# print(f(12) - f(4))
# # 28


# 17
# f = open("Файлы для пробников/17-2__7byhg.txt")
# a = f.readlines()
# s = []
# for el in a:
#     s.append(int(el))
#
# mn = -555
# ans = []
# for i in range(len(s) - 2):
#     if (abs(s[i])%10 == 4) + (abs(s[i+1])%10 == 4) + (abs(s[i+2])%10 == 4) == 1:
#         if (s[i] + s[i+1] + s[i+2]) % mn != 0:
#             ans.append(s[i] + s[i+1] + s[i+2])
# print(len(ans), max(ans))
# # 2444 269722


# 19
# from functools import *
# @lru_cache(None)
# def f(a1, a2):
#     if a1 + a2 >= 169:
#         return 0
#     t = [f(a1+4, a2), f(a1*2, a2), f(a1*3, a2), f(a1, a2+4), f(a1, a2*2), f(a1, a2*3)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 153):
#     if f(15, s) == -1:
#         print(s)
# # 50


# 20
# from functools import *
# @lru_cache(None)
# def f(a1, a2):
#     if a1 + a2 >= 169:
#         return 0
#     t = [f(a1+4, a2), f(a1*2, a2), f(a1*3, a2), f(a1, a2+4), f(a1, a2*2), f(a1, a2*3)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# c = 0
# for s in range(1, 153):
#     if f(15, s) != 1 and f(15, s) == 2:
#         c += 1
# print(c)
# # 10


# 21
# from functools import *
# @lru_cache(None)
# def f(a1, a2):
#     if a1 + a2 >= 169:
#         return 0
#     t = [f(a1+4, a2), f(a1*2, a2), f(a1*3, a2), f(a1, a2+4), f(a1, a2*2), f(a1, a2*3)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 153):
#     if (f(15, s) == -1 or f(15, s) == -2 or f(15, s) == -3) and (f(15, s) != -1 and f(15, s) != -2):
#         print(s)
# #3642


# 23
# def f(start, end):
#     d = {}
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
#         if key**0.5 in d:
#             d[key**0.5] += d[key]
#     return d[end]
#
# print(f(25, 3))
# # 238


# 24
# from re import *
# f = open('Файлы для пробников/Задание_24__7ajcf.txt')
# s = f.readline()
#
# pattern = r'(?=(([C,D,F][A,O])+))'
#
# mx = 0
# for i in finditer(pattern, s):
#     t = i.group(1)
#     mx = max(mx, len(t))
# print(mx//2)
# # 95

# 25
# def d(n:int) -> list[int]:
#     for div in range(1, int(n**0.5)+1):
#         if n % div == 0:
#             if len(str(div)) > 1:
#                 if str(div) == str(div)[::-1]:
#                     return True
#             if len(str(n//div)) > 1:
#                 if str(n//div) == str(n//div)[::-1]:
#                     return True
#     return False
#
#
# ans = 0
# for x in range(11111, 22223):
#     if d(x):
#         ans += 1
# print(ans)
# # 2503

# 27
# Для файла А
# from math import dist
# from turtle import *
# f = open('Файлы для пробников/1_A__5wyzi.txt')
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[], [], [], []]
#
# for i in a:
#     x, y, m = i
#     if x < -8 and y < -13:
#         clusters[0].append(i)
#     if -15 < x < -5 and 14 < y < 25:
#         clusters[1].append(i)
#     if 2 < x < 13 and -19 < y < -8:
#         clusters[2].append(i)
#     if x > 15 and y < -19:
#         clusters[3].append(i)
#
# t = 0.3
# def tri(star, k):
#     tri = []
#     for star1 in clusters[k]:
#         if dist(star, star1) <= t and star != star1:
#             tri.append(star1)
#     if len(tri) == 2:
#         return tri
#     return False
# def good(star, k):
#     tri = []
#     for star1 in clusters[k]:
#         if dist(star, star1) < t and star != star1:
#             tri.append(star1)
#     if len(tri) == 2:
#         return True
#     return False
# def ans(s1, s2, s3):
#     if 0.08 <= s1[2] <= 0.6:
#         if 0.8 <= s2[2] <= 1.2 or 0.8 <= s3[2] <= 1.2:
#             return True
#     if 0.08 <= s2[2] <= 0.6:
#         if 0.8 <= s1[2] <= 1.2 or 0.8 <= s3[2] <= 1.2:
#             return True
#     if 0.08 <= s3[2] <= 0.6:
#         if 0.8 <= s1[2] <= 1.2 or 0.8 <= s2[2] <= 1.2:
#             return True
#     return False
#
# for k in range(4):
#     for star1 in clusters[k]:
#         if good(star1, k):
#             f = tri(star1, k)
#             if good(f[0], k) and good(f[1], k):
#                 if dist(f[0], f[1]) <= t:
#                     if ans(star1, f[0], f[1]):
#                         if star1 != f[0] and star1 != f[1] and f[0] != f[1]:
#                             print(star1, f[0], f[1])
#
# # print(star1, star2, star3)
# # print((star1[0]+star2[0]+star3[0])/3, (star1[1]+star2[1]+star3[1])/3)
#
# # m = 10
# # tracer(0)
# # up()
# # for k in range(4):
# #     for i in clusters[k]:
# #         x, y, m1 = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# # 0 0