"""Решение новогоднего пробника: https://3.shkolkovo.online/my/course/7259/dz/27827"""


# 2
# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 F = (w and x and y and z) or (z and (not(w)) and (not(x and (y != z))))
#                 if F == 1:
#                     print(x, y, w, z)
# # wxyz


# 5
# def ans(n):
#     s = bin(n)[2:]
#     if n % 5 == 0:
#         s += '00'
#     else:
#         k = bin(n % 5)[2:]
#         s += k
#     return int(s, 2)
#
#
# mx = -1
# for n in range(1, 1001, 2):
#     mx = max(mx, ans(n))
# print(mx)
# # 7996


# 6
# from turtle import *
# m = 15
# tracer(0)
# screensize(200*200)
#
# for _ in range(6):
#     fd(5*m)
#     bk(5*m)
#     rt(60)
# up()
# rt(45)
# fd(12*m)
# down()
# for _ in range(8):
#     fd(6*m)
#     bk(6*m)
#     rt(45)
# up()
# lt(135)
# fd(20*m)
# down()
# for _ in range(10):
#     fd(4*m)
#     bk(4*m)
#     rt(36)
#
# up()
# for x in range(-45, 45):
#     for y in range(-45, 45):
#         goto(x*m, y*m)
#         dot(8, 'blue')
# done()
# # 81


# 8
# from itertools import *
# s = 'АДКОПР'
#
# n = 0
# for i in product(s, repeat=6):
#     g = ''.join(i)
#     n += 1
#     if n % 7 == 0 and g[0] == 'П' and 'Р' not in g:
#         print(g, n)
# # 37324


# 12
# a = {
#     'q0.': ['.', 'R', 'q0'],
#     'q0x': ['x', 'R', 'q1'],
#     'q0y': ['x', 'R', 'q0'],
#     'q1.': ['.', 'S', 'q1'],
#     'q1x': ['y', 'R', 'q0'],
#     'q1y': ['x', 'R', 'q1']
# }
# s1 = 'xxxxxxx'
# s = list('..' + s1 + '..')
# i = 2
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i += 1
# print(''.join(s))
# # 851


# 13
# from ipaddress import *
# net = ip_network('191.18.150.75/255.255.240.0', 0)
# for ip in net.hosts():
#     print(''.join(str(ip).split('.')))
# # 19118159254


# 14
# # from string import *
# # print(ascii_uppercase)
#
# def f(n):
#     s = ''
#     a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     while n != 0:
#         if n % 25 < 10:
#             s += str(n % 25)
#         else:
#             s += a[n % 25 - 10]
#         n //= 25
#     return s[::-1]
#
# F = 5 * (3125 ** (100)) + 2 * (625 ** (2024)) + 4 * (125 ** (2025)) - (25 ** (2026)) - 620
# G = f(F)
# ans = 0
# for el in G:
#     if el in '0123456789A':
#         ans += 1
# print(ans)
# # 2789


# 16
# from functools import *
# @lru_cache(None)
# def f(n):
#     return 2 * (g(n - 2) + 6)
#
# @lru_cache(None)
# def g(n):
#     if n < 7:
#         return 3 * n
#     return g(n - 3) + 1
#
# for i in range(3000):
#     f(i), g(i)
#
# print(f(2026) + g(2025))
# # 2079


# 17
# f = open('Файлы для пробников/Task17__8lika.txt')
# n = [int(i) for i in f.readlines()]
#
# ans, mx = 0, -1
# for i in range(len(n) - 2):
#     t = [n[i], n[i+1], n[i+2]]
#     t1, t2, t3 = str(n[i]), str(n[i+1]), str(n[i+2])
#     count_26, even, odd = 0, 0, 0
#     for el in t:
#         if '26' in str(el):
#             count_26 += 1
#         if el % 2 == 0:
#             even += 1
#         if el % 2 != 0:
#             odd += 1
#
#     if count_26 == 1 and even > odd:
#         ans += 1
#         mx = max(mx, sum(t))
# print(ans, mx)
# # 1066 291991


# 19
#  Первое решение:
# from functools import *
#
# @lru_cache(None)
# def f(s):
#     if s <= 26:
#         return 0
#     t = [f(s - 2), f(s - 3), f(s // 3)]
#     n = [int(i) for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(27, 201):
#     if f(s) != 1 and f(s) == -1:
#         print(s)
# # 81

# Второе решение:
# def steps(p):
#     return p - 2, p - 3, p//3
#
# def play(p, r):
#     if p <= 26 and r % 2 == 0:
#         return True
#
#     if p <= 26 or r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else all(next_steps)
#
# for s in range(27, 201):
#     if not(play(s, 1)) and play(s, 2):
#         print(s)
# # 81


# 20
#  Первое решение:
# from functools import *
#
# @lru_cache(None)
# def f(s):
#     if s <= 26:
#         return 0
#     t = [f(s - 2), f(s - 3), f(s // 3)]
#     n = [int(i) for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(27, 201):
#     if f(s) != 1 and f(s) == 2:
#         print(s)
# # 83 84

# Второе решение:
# def steps(p):
#     return p - 2, p - 3, p//3
#
# def play(p, r):
#     if p <= 26 and r % 2 == 0:
#         return True
#
#     if p <= 26 or r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else all(next_steps)
#
# for s in range(27, 201):
#     if not(play(s, 1)) and play(s, 3):
#         print(s)
# # 83 84


# 21
#  Первое решение:
# from functools import *
#
# @lru_cache(None)
# def f(s):
#     if s <= 26:
#         return 0
#     t = [f(s - 2), f(s - 3), f(s // 3)]
#     n = [int(i) for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(27, 201):
#     if f(s) != -1 and (f(s // 3) == 1 or f(s // 3) == 2):
#         print(s)
# # ???

# Второе решение:
# def steps(p):
#     return p - 2, p - 3, p//3
#
# def play(p, r):
#     if p <= 26 and r % 2 == 0:
#         return True
#
#     if p <= 26 or r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else all(next_steps)
#
# for s in range(27, 201):
#     if not(play(s, 2)) and (play(s, 2) or play(s, 4)):
#         print(s)
# # 87


# 23
# def f(start, end):
#     d = {}
#     for i in range(start, end - 1, -1):
#         d[i] = 0
#
#     d[start] = 1
#
#     if 31 in d:
#         del d[31]
#
#     for key in d.keys():
#         if key - 2 in d:
#             d[key - 2] += d[key]
#         if key - 3 in d:
#             d[key - 3] += d[key]
#         if key // 4 in d:
#             d[key // 4] += d[key]
#     return d[end]
#
# print(f(45, 26)*f(26, 7))
# # 3784


# 24
# f = open("Файлы для пробников/task24__8licz.txt")
# s = f.readline()
# s = s.replace('SNOW', '*')
# csn, codds, mx, start = 0, 0, 0, 0
#
# for end in range(len(s)):
#     if s[end] == '*':
#         csn += 1
#     if s[end] in '13579':
#         codds += 1
#     while codds > 70:
#         if s[start] == '*':
#             csn -= 1
#         if s[start] in '13579':
#             codds -= 1
#         start += 1
#     if codds <= 70 and csn >= 30:
#         q = s[start:end + 1].count('*')
#         mx = max(mx, end - start + 1 + q * 3)
# print(mx)
# # 2996


# 25
# def m(n):
#     divs = []
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divs.append(i)
#             divs.append(n//i)
#     divs.sort()
#     M = 0
#     if divs:
#         M = divs[-1] - divs[0]
#     return M
#
# def th(n):
#     s = ''
#     while n != 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# stop = 0
# for n in range(20252027, 10**9):
#     if m(n) != 0:
#         if th(m(n))[-1] == '2':
#             print(n, m(n))
#             stop += 1
#     if stop == 7:
#         break
# # 20252030 10126013
# # 20252031 6750674
# # 20252036 10126016
# # 20252039 227462
# # 20252042 10126019
# # 20252045 4050404
# # 20252048 10126022


# 26
# f = open("Файлы для пробников/task26__8libo.txt")
# l_start, l_end = [], []
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# num = 0
# current_fill = []
# s = 0
# for i in data:
#     num += 1
#     i.append(num)
#     p, u, n = i[0], i[1], i[2]
#     if p in current_fill or u in current_fill:
#         pass
#     else:
#         current_fill.append(p)
#         current_fill.append(u)
#         if u > p:
#             l_start.append(i)
#         if u < p:
#             l_end.append(i)
#             s += n
#
# l_start.sort()
# l_end.sort(reverse=True)
# last_num = l_start[-1][-1]
# print(last_num, s)
# # 895 253594


# 27
# Файл А:
# from math import dist
# f = open("Файлы для пробников/27A__NY__8liac.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f.readlines() if 'X' not in i]
# clusters = [[], []]
#
# for i in a:
#     x, y = i
#     if y > 4.5:
#         clusters[0].append(i)
#     if y < 0 and -2 < x < 10:
#         clusters[1].append(i)
#
# centers = []
# for k in range(2):
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
# px, py = [], []
# for el in centers:
#     px.append(el[0])
#     py.append(el[1])
#
# print(int(min(px) * 1000), int(min(py) * 1000))
# # -9955 -8292

# Файл Б:
# from math import dist
# f = open("Файлы для пробников/27B_NY__8liaf.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f.readlines() if 'X' not in i]
# clusters = [[], [], []]
#
# for i in a:
#     x, y = i
#     if y < 0 and x < 2:
#         clusters[0].append(i)
#     if -12 < y < 1 and 9 < x < 21:
#         clusters[1].append(i)
#     if 2 < y < 13 and 12 < x < 24:
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
# # done()
# l1, l2, l3 = len(clusters[0]), len(clusters[1]), len(clusters[2])
#
# # centers = []
# # for k in range(3):
# #     mn = 10**10
# #     for star in clusters[k]:
# #         s = 0
# #         for i in clusters[k]:
# #             s += dist(star, i)
# #         if s < mn:
# #             mn = s
# #             mn_star = star
# #     centers.append(mn_star)
# centers = [[-2.951964714, -10.74531788], [14.43496365, -4.29551165], [17.94438175, 5.989076476]]
# Q1 = dist(centers[2], centers[1])
# mx = -1
# for i in clusters[0]:
#         mx = max(mx, dist(i, centers[0]))
# Q2 = mx
# print(int(Q1 * 1000), int(Q2 * 1000))
# # 10866 5782