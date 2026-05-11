"""https://3.shkolkovo.online/my/course/7259/dz/31782"""

# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 F = ( (z <= x) <= (x == y) ) or (not(w))
#                 if F == 0:
#                     print(x, y, w, z, int(F))
# # yxwz


# 5
# def ans(n):
#     s = bin(n)[2:]
#     sm = sum(int(i) for i in s)
#     if sm % 2 == 0:
#         s += '0'
#         s = '10' + s[2:]
#     else:
#         s += '1'
#         s = '11' + s[2:]
#     r = int(s, 2)
#     return r
#
# a = set()
# for n in range(100):
#     if ans(n) <= 19:
#         a.add(n)
# print(max(a))
# # 12


# 6
# from turtle import *
# tracer(0)
# lt(90)
# m = 15
# screensize(4000, 4000)
#
# rt(45)
# for _ in range(3):
#     rt(45)
#     fd(10*m)
#     rt(45)
# rt(315)
# fd(10*m)
# rt(90)
# fd(20*m)
# rt(90)
# for _ in range(2):
#     fd(10*m)
#     rt(90)
#
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 261


# 8
# from itertools import *
# s = 'АЕЛПРЬ'
#
# num = 0
# for i in product(s, repeat=6):
#     g = ''.join(i)
#     num += 1
#     if num % 2 != 0:
#         if g[0] != 'А' and g[0] != 'Л' and g.count('П') >= 2:
#             print(num, g)
#             break
# # 7903


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q1.': ['1', 'L', 'q2'],
#     'q10': ['1', 'S', 'q2'],
#     'q11': ['0', 'L', 'q1'],
#     'q2.': ['.', 'S', 'q2']
# }
#
# s1 = bin(1023)[2:]
# s = list('...'+s1+'...')
# i = -3
# c = 0
# p = 'q0'
#
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(''.join(s))
# print(int('10000000000', 2))
# # 1024


# 13
# from ipaddress import *
#
# net = ip_network('68.203.243.87/255.255.224.0', 0)
#
# for ip in net.hosts():
#     print(ip)
# # 68.203.255.254 -> 780


# 17
# f = open("Файлы для пробников/1_17__adeax.txt")
# n = [int(i) for i in f]
# mn123 = min(i for i in n if i > 0 and i % 123 == 0)
#
# ans1 = 0
# ans2 = 0
# for i in range(len(n) - 1):
#     t = n[i:i+2]
#     if sum(t) < mn123:
#         ans1 += 1
#         ans2 = max(ans2, sum(t))
# print(ans1, abs(ans2))
# # 5001 962


# 19
# решение 1:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 4, h2), (h1, h2 + 4), (h1 * 3, h2), (h1, h2 * 3)]
#
# def play(p, r):
#     if sum(p) >= 154:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 143):
#     p = (11, s)
#     if play(p, 2) and (not(play(p, 1))):
#         print(p)
# # 16

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 154:
#         return False
#
#     steps = [f(a + 4, b), f(a, b + 4), f(a * 3, b), f(a, b * 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
#
# for s in range(1, 143):
#     if f(11, s + 4) == 1 or f(11, s * 3) == 1 or f(11 + 4, s) == 1 or f(11 * 3, s) == 1:
#         print(s)
# # 16
# Мы же пишем такое условие для того, чтобы сымитировать ситуацию, когда не при всех ходах П выигрывает В?


# 20
# решение 1:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 4, h2), (h1, h2 + 4), (h1 * 3, h2), (h1, h2 * 3)]
#
# def play(p, r):
#     if sum(p) >= 154:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 143):
#     p = (11, s)
#     if play(p, 3) and (not(play(p, 1))):
#         print(p)
# # 39 40

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 154:
#         return False
#
#     steps = [f(a + 4, b), f(a, b + 4), f(a * 3, b), f(a, b * 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
#
# for s in range(1, 143):
#     if f(11, s) == 2:
#         print(s)
# # 39 40


# 21
# решение 1:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 4, h2), (h1, h2 + 4), (h1 * 3, h2), (h1, h2 * 3)]
#
# def play(p, r):
#     if sum(p) >= 154:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 143):
#     p = (11, s)
#     if play(p, 4) and (not(play(p, 2))):
#         print(p)
# # 41

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 154:
#         return False
#
#     steps = [f(a + 4, b), f(a, b + 4), f(a * 3, b), f(a, b * 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
#
# for s in range(1, 143):
#     if f(11, s) == -2:
#         print(s)
# # 41


# 23
# def f(start, end):
#     if start == end:
#         return 1
#     if start > end or start == 14:
#         return 0
#     return f(start + 1, end) + f(start * 2, end) + f(start * 3, end)
#
# print(f(2, 39))
# # 188


# 24
# from re import *
# f = open("Файлы для пробников/1_24__addwk.txt")
# s = f.readline()
#
# # pattern = '([^B]+[^C]+[BC][^B]+[^C]+){190}'
# #
# # for i in finditer(pattern, s):
# #     g = i.group(0)
# #     # g = g.replace('BC', '*')
# #     # print(g.count('*'), g)
# #     print(g.count('BC'), g)
# # помогите пожалуйста найти ошибку в коде
#
# s = s.replace('BC', '*')
# c = start = mx = 0
# for end in range(len(s)):
#     if s[end] == '*':
#         c += 1
#     while c > 190:
#         if s[start] == '*':
#             c -= 1
#         start += 1
#
#     if c == 190:
#         p = s[start:end + 1]
#         p = p.replace('*', 'BC')
#         # if len(p) >= 2285:
#         #     print(p)
#         #     np = s[start - 40: end + 41]
#         #     np = np.replace('*', 'BC')
#         #     print(np)
#         mx = max(mx, len(p))
# print(mx + 2)
# # 2287


# 25
# from fnmatch import *
#
# for x in range(0, 10**10 + 1, 9874):
#     if fnmatch(str(x), '89*6?7?9?'):
#         print(x, x // 9874)
# # 8901677598 901527
# # 8905627198 901927
# # 8912617990 902635
# # 8941667298 905577
# # 8952607690 906685
# # 8970607992 908508
# # 8988647790 910335


# 26
# f = open("Файлы для пробников/1_26__adew3.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# data.sort()
# sm = 0
# mxart = 0
# for product in data:
#     sm += product[1]
#     mxart = max(mxart, product[0])
# av = sm/n
#
# for product in data:
#     mon = product[1]
#     if mon > sm/n:
#         product.append('expensive')
#     else:
#         product.append('chip')
#
# art = [[] for _ in range(mxart + 1)]
#
# for product in data:
#     if product[2] == 0 and product[-1] == 'expensive':
#         art[product[0]].append(product)
#
# # mxprod = 0
# # for i in range(len(art)):
# #     if len(art[i]) == 51:
# #         print(i, art[i])
#
# favorites = [46481, 51786]
# solds = []
# n_solds = []
# for fav_art in favorites:
#     sold_products = 0
#     n_sold_products = 0
#     for product in data:
#         if product[0] == fav_art:
#             if product[2] == 0:
#                 sold_products += 1
#             else:
#                 n_sold_products += 1
#     solds.append(sold_products)
#     n_solds.append(n_sold_products)
# # print(n_solds)
#
# sold_products = 0
# n_sold_products = 0
# money_from_sell = 0
# for product in data:
#     if product[0] == 46481:
#         if product[2] == 0:
#             sold_products += 1
#             money_from_sell += product[1]
#         else:
#             n_sold_products += 1
# print(money_from_sell, n_sold_products)
# # 43656 36


# 27A
# from math import dist
# f = open("Файлы для пробников/1_27_A__adh5g.txt")
# data = []
# for star in f:
#     x, y, par = star.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
# # print(len(data))
#
# clusters = []
# r = 1
#
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
# n_clusters = []
# trash = []
# for cl in clusters:
#     if len(cl) > 50:
#         n_clusters.append(cl)
#         # print(len(cl))
#     else:
#         trash.append(cl)
# # print(len(n_clusters), len(trash))
#
# centers = []
# for k in range(len(n_clusters)):
#     mn = 10**10
#     for star in n_clusters[k]:
#         s = 0
#         for i in n_clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#
# # мин. кол-во точек у первого кластера 114 < 121
#
# ax = ay = 0
# center = centers[0]
#
# d = 0
# mnd = 10**10
# for star in n_clusters[0]:
#     if star[-1][0] == 'M' and star[-1][-3:] == 'III' and star[-1][-4] in '0123456789':
#         d = dist(star[:2], center[:2])
#         mnd = min(mnd, d)
#
# for star in n_clusters[0]:
#     if star[-1][0] == 'M' and star[-1][-3:] == 'III' and star[-1][-4] in '0123456789':
#         d = dist(star[:2], center[:2])
#         if d == mnd:
#             ax = star[0]
#             ay = star[1]
#
# print(int(abs(ax * 10_000)), int(abs(ay * 10_000)))
# # 44694 69754
#
#
# # from turtle import *
# # tracer(0)
# # lt(90)
# # m = 15
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# # up()
# #
# # for k in range(len(n_clusters)):
# #     for star in n_clusters[k]:
# #         x, y = star[:2]
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(centers)):
# #     x, y = centers[k][:2]
# #     goto(x*m, y*m)
# #     dot(6, 'red')
# # done()


# 27B
# from math import dist
# f = open("Файлы для пробников/1_27_B__adh5h.txt")
# data = []
# for star in f:
#     x, y, par = star.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
# print(len(data))
#
# clusters = []
# r = 1
#
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
# n_clusters = []
# trash = []
# for cl in clusters:
#     if len(cl) > 50:
#         n_clusters.append(cl)
#         print(len(cl))
#     else:
#         trash.append(cl)
# print(len(n_clusters), len(trash))
#
# centers = []
# for k in range(len(n_clusters)):
#     mn = 10**10
#     for star in n_clusters[k]:
#         s = 0
#         for i in n_clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#
# # b1
# giants = []
# for k in range(len(n_clusters)):
#     c = 0
#     for star in n_clusters[k]:
#         par = star[-1]
#         if par[0] == 'K' and par[-3:] == 'III' and par[-4] in '0123456789':
#             c += 1
#     giants.append(c)
# print(giants)
#
# b1 = dist(centers[0][:2], centers[-1][:2])
#
# # b2
# b2 = 0
# for k in range(len(n_clusters)):
#     c = 0
#     for star1 in n_clusters[k]:
#         for star2 in n_clusters[k]:
#             par = star1[-1]
#             per = star2[-1]
#             if par[0] == 'G' and par[-1] == 'V' and par[-2] in '0123456789':
#                 if per[0] == 'G' and per[-1] == 'V' and per[-2] in '0123456789':
#                     b2 = max(b2, dist(star1[:2], star2[:2]))
#
# print(int(b1 * 10_000), int(b2 * 10_000))
# # 138716 34029
#
# # from turtle import *
# # tracer(0)
# # lt(90)
# # m = 15
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# # up()
# #
# # for k in range(len(n_clusters)):
# #     for star in n_clusters[k]:
# #         x, y = star[:2]
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(centers)):
# #     x, y = centers[k][:2]
# #     goto(x*m, y*m)
# #     dot(6, 'red')
# # done()
