"""https://3.shkolkovo.online/my/course/7259/dz/31143"""

# 2
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x or (not(y))) <= (z == (x and y)) or (not(w))
#                 if F == 0:
#                     print(x, y, z, w, int(F))
# # zxyw


# 5
# def ans(n):
#     s = bin(n)[2:]
#     secdig = s[1]
#     s = s[:-1] + secdig + secdig
#     r = int(s, 2)
#     return r
#
# a = set()
# for n in range(23, 10000):
#     if ans(n) > 177:
#         a.add(n)
# print(min(a))
# # 90


# 6
# from turtle import *
#
# lt(90)
# tracer(0)
# screensize(4000, 4000)
# m = 15
#
# for _ in range(4):
#     fd(4*m)
#     rt(90)
#     fd(8*m)
#     rt(90)
#
# up()
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 21


# 8
# from itertools import *
#
# n = '12345'
#
# ans = set()
# for i in product(n, repeat=6):
#     s = ''.join(i)
#     if (s[0] in '135') and (s[-1] in '24'):
#        ans.add(s)
# print(len(ans))
# # 3750


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q00': ['0', 'L', 'q1'],
#     'q01': ['0', 'L', 'q0'],
#     'q1.': ['.', 'S', 'q1'],
#     'q10': ['1', 'L', 'q1'],
#     'q11': ['0', 'L', 'q0']
# }
#
# s1 = '10001000110001000100000000000'
# s = list('...' + s1 + '...')
# i = -3
# c = 0
# p = 'q0'
#
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(''.join(s), s.count('0'))
# # 180


# 13
# from ipaddress import *
#
# net = ip_network('191.89.109.206/255.255.224.0', 0)
#
# for ip in net.hosts():
#     print(ip)
# # 191.89.127.254 -> 661


# 14
# def tr(n):
#     s = ''
#     while n != 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# f = 3**23 + 3**7 - 723
#
# print(tr(f).count('0'))
# # 21


# 16
# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n < 50:
#         return n**3
#     if n >= 50 and n % 3 == 0:
#         return (f(n - 2) // 3) + n
#     if n >= 50 and n % 3 != 0:
#         return 5 * f(n - 2)
#
# for i in range(16000):
#     f(i)
#
# print(f(15890)//f(15789))
# # 63463933490935737


# 17
# f = open("Файлы для пробников/17__7n55g.txt")
# n = [int(i) for i in f]
# ost3 = max(n) % 3
# ost7 = min(n) % 7
#
# count = 0
# mxs = set()
#
# for i in range(len(n) - 1):
#     t = n[i:i+2]
#     c3 = sum(1 for el in t if (el % 3) == ost3)
#     c7 = sum(1 for el in t if (el % 7) == ost7)
#     if c3 >= 1 and c7 >= 1:
#         count += 1
#         mxs.add(sum(t))
#
# print(count, max(mxs))
# # 1467 197700


# 19
# решение 1:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 48:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else any(next_plays)
#
#
# for s in range(1, 44):
#     p = (4, s)
#     if play(p, 2) and (not(play(p, 1))):
#         print(s)
# # 11

# решение 2:
# from functools import *
# from sys import setrecursionlimit
# setrecursionlimit(10**9)
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 48:
#         return False
#
#     steps = [f(a + 1, b), f(a, b + 1), f(a * 2, b), f(a, b * 2)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# # for s in range(50):
# #     f(s, 4)
#
# for s in range(1, 44):
#     if f(4 - 1, s) == 1 or f(4, s - 1) == 1 or f(4 * 2, s) == 1 or f(4, s * 2) == 1:
#         print(s)
# # Ошибка: Stack overflow (used 2914 kB)
# # Подскажите пожалуйста, как ее исправить в данном решении?


# 20
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 48:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
#
# for s in range(1, 44):
#     p = (4, s)
#     if play(p, 3) and (not(play(p, 1))):
#         print(s)
# # 21


# 21
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 48:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
#
# for s in range(1, 44):
#     p = (4, s)
#     if play(p, 4) and (not(play(p, 2))):
#         print(s)
# # 20


# 23
# def f(start, end):
#     if start > end or start == 21:
#         return 0
#     if start == end:
#         return 1
#     return f(start + 1, end) + f(2 * start + 1, end)
#
# print(f(1, 25))
# # 20


# 24
# from re import *
# f = open("Файлы для пробников/24_2022__7bpdm.txt")
# s = f.readline()
#
# pattern = '(AB|CB)+'
#
# mxc = 0
# for i in finditer(pattern, s):
#     g = i.group(0)
#     mxc = max(len(g), mxc)
#
# print(mxc//2)
# # 65


# 25
# from fnmatch import *
#
# for x in range(0, 10**7 + 1, 290):
#     if fnmatch(str(x), '?75*47?'):
#         print(x, x//290)
#
# # 1752470 6043
# # 3753470 12943
# # 5754470 19843
# # 7755470 26743
# # 9756470 33643


# 26
from math import ceil
f = open("Файлы для пробников/4__tdop.txt")
n = int(f.readline())
data = [int(i) for i in f]

potential_sale_list = []
trash = []

for product in data:
    if product > 200:
        potential_sale_list.append(product)
    else:
        trash.append(product)

potential_sale_list.sort()

optimal_sale_list = [potential_sale_list.pop(-1)]

real_sale = []
rejected_sale = [optimal_sale_list[0]]
for i in range(len(potential_sale_list)//2): # так как длина = 820
    optimal_sale_list.append(potential_sale_list[i])
    optimal_sale_list.append(potential_sale_list[-i-1])

    real_sale.append(potential_sale_list[i])

    rejected_sale.append(potential_sale_list[-i-1])

all_sum = sum(trash) + ceil(sum(real_sale)*0.7) + sum(rejected_sale)

print(all_sum, max(real_sale))
# 464632 602


# 27A
# from math import dist
# f = open("Файлы для пробников/27_2A__achhc.txt")
# e = f.readline()
# data = []
# for planet in f:
#     x, y, par = planet.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#
# print(f'len(data): {len(data)}')
# r = 1
# old_clusters = []
# trash = []
# clusters = []
# while data:
#     old_clusters.append([data.pop(0)])
#     for i in old_clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 old_clusters[-1].append(j)
#                 data.remove(j)
#
# for pl in old_clusters:
#     if len(pl) > 100:
#         clusters.append(pl)
#         print(f'len(c): {len(pl)}')
#     else:
#         trash.append(pl)
# print(f'len(clusters): {len(clusters)}')
# print(f'len(trash): {len(trash)}')
#
# centers = []
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
#
# # from turtle import *
# #
# # lt(90)
# # tracer(0)
# # screensize(4000, 4000)
# # m = 10
# # up()
# #
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y, z = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for star in centers:
# #     x, y, z = star
# #     goto(x*m, y*m)
# #     dot(5, 'red')
# # done()
#
# ans1 = []
# for k in range(len(clusters)):
#     for star in clusters[k]:
#         par = star[-1]
#         if par[0] == 'G' and par[-3:] == 'VII':
#             for new_star in clusters[k]:
#                 n_par = new_star[-1]
#                 if n_par[-2:] == 'II' and n_par[-3] in '0123456789':
#                     if dist(star[:2], new_star[:2]) <= 0.8:
#                         ans1.append(star)
# check = [ans1.pop(0)]
# for el in ans1:
#     if el not in check:
#         check.append(el)
#
# sm = 0
# for star in clusters[2]:
#     if star[-1][0] == 'J':
#       sm += dist(star[:2], centers[2][:2])
#
# print(len(check), int(sm*1000))
# # 11 94839


# 27B
# from math import dist
# f = open("Файлы для пробников/27_2B__achhd.txt")
# e = f.readline()
# data = []
# for planet in f:
#     x, y, par = planet.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#
# print(f'len(data): {len(data)}')
# r = 1
# old_clusters = []
# trash = []
# clusters = []
# while data:
#     old_clusters.append([data.pop(0)])
#     for i in old_clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 old_clusters[-1].append(j)
#                 data.remove(j)
#
# for pl in old_clusters:
#     if len(pl) > 100:
#         clusters.append(pl)
#         print(f'len(c): {len(pl)}')
#     else:
#         trash.append(pl)
# print(f'len(clusters): {len(clusters)}')
# print(f'len(trash): {len(trash)}')
#
# centers = []
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
#
# # from turtle import *
# #
# # lt(90)
# # tracer(0)
# # screensize(4000, 4000)
# # m = 10
# # up()
# #
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y, z = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for star in centers:
# #     x, y, z = star
# #     goto(x*m, y*m)
# #     dot(5, 'red')
# # done()
#
# g = []
# for k in range(len(clusters)):
#     gigs = 0
#     for star in clusters[k]:
#         par = star[-1]
#         if par[-3:] == 'III' and par[-4] in '0123456789':
#             gigs += 1
#     g.append(gigs)
#
# ans1 = dist(centers[5][:2], centers[2][:2])
#
# ans2 = 0
# for k in range(len(clusters)):
#     for star in clusters[k]:
#         par = star[-1]
#         if par[-1] == 'V' and par[-2] in '0123456789':
#             ans2 = max(ans2, dist(star[:2], centers[k][:2]))
#
# print(int(ans1*1000), int(ans2*1000))
# # 30959 2824

