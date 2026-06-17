"""https://3.shkolkovo.online/my/course/7259/dz/32184"""
from getpass import fallback_getpass
from pprint import pformat

# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 F = (not(x <= w)) or (y == z) or y
#                 if int(F) == 0:
#                     print(x, y, w, z, int(F))
# # zxwy


# 5
# def ans(n):
#     s = bin(n)[2:]
#     if n % 3 == 0:
#         s += s[-3:]
#     else:
#         s += bin((n%3)*3)[2:]
#     return int(s, 2)
#
# a = set()
# for n in range(1, 1000):
#     r = ans(n)
#     if r >= 76:
#         a.add(n)
# print(min(a))
# # 11


# 6
# from turtle import *
# lt(90)
# tracer(0)
# m = 5
# screensize(4000, 4000)
#
# for _ in range(6):
#     fd(71*m)
#     rt(90)
#     fd(73*m)
#     rt(90)
# up()
# fd(18*m)
# rt(90)
# fd(22*m)
# lt(90)
# down()
# for _ in range(6):
#     fd(45*m)
#     rt(90)
#     fd(58*m)
#     rt(90)
# up()
#
# for x in range(-30, 30):
#     for y in range(-30 ,30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 2392


# 8
# from itertools import *
# s = 'АЕЛРСТ'
# num = 0
#
# for i in product(s, repeat=5):
#     g = ''.join(i)
#     num += 1
#     if num % 2 == 0 and (g[0] not in 'АСТ') and (g.count('Л') == 2) and ('ЛЛ' not in g):
#         print(num, g)
# # 4518


# 12
# a = {
#     'q0.': ['.','S','q0'],
#     'q0A': ['C','R','q1'],
#     'q0B': ['B', 'R', 'q0'],
#     'q0C': ['C', 'R', 'q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q1A': ['A', 'R', 'q1'],
#     'q1B': ['B', 'R', 'q0'],
#     'q1C': ['C', 'R', 'q1']
# }
# s1 = 'ABABABABABAAAAAAAAAA'
# s = list('...'+s1+'...')
# i = 3
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i += 1
# print(''.join(s))
# # 928


# 13
# from ipaddress import *
#
# net = ip_network('91.147.200.0/255.255.252.0', 0)
# count = 0
# for ip in net.hosts():
#     if (bin(int(ip))[2:].zfill(32)).count('1') % 5 == 2:
#         count += 1
# print(count)
# # 252


# 14
# def f(n):
#     s = ''
#     while n != 0:
#         s += str(n % 5)
#         n //= 5
#     return s[::-1]
#
# g = 5**1000 - 5**200 + 5**100 - 129
#
# print(f(g).count('4'))
# # 898


# 17
# f = open("Файлы для пробников/17__8syxa.txt")
# n = [int(i) for i in f]
# nums = sum(1 for el in n if len(str(abs(el))) == 5 and abs(el) % 10 == 7)
# count = 0
# mx = -10**10
#
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     if max(t)**2 + (sum(t) - max(t) - min(t))**2 < nums**2:
#         count += 1
#         mx = max(mx, sum(t))
# print(count, abs(mx))
# # 3 44335


# 19
# Решение 1:
# def steps(p):
#     return (p + 2, p + 5, p * 2)
#
# def play(p, r):
#     if p >= 47:
#         return r % 2 == 0
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 47):
#     if play(s, 2) and (not(play(s, 1))):
#         print(s)
# # 22


# Решение 2:
# def f(a):
#     if a >= 47:
#         return False
#     steps = [f(a + 2), f(a + 5), f(a * 2)]
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for a in range(1, 47):
#     if f(a) == -1:
#         print(a)
# # 22


# 20
# Решение 1:
# def steps(p):
#     return (p + 2, p + 5, p * 2)
#
# def play(p, r):
#     if p >= 47:
#         return r % 2 == 0
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 47):
#     if play(s, 3) and (not(play(s, 1))):
#         print(s)
# # 11 21


# Решение 2:
# def f(a):
#     if a >= 47:
#         return False
#     steps = [f(a + 2), f(a + 5), f(a * 2)]
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for a in range(1, 47):
#     if f(a) == 2:
#         print(a)
# # 11 21


# 21
# Решение 1:
# def steps(p):
#     return (p + 2, p + 5, p * 2)
#
# def play(p, r):
#     if p >= 47:
#         return r % 2 == 0
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 47):
#     if play(s, 4) and (not(play(s, 2))):
#         print(s)
# # 3


# Решение 2:
# def f(a):
#     if a >= 47:
#         return False
#     steps = [f(a + 2), f(a + 5), f(a * 2)]
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for a in range(1, 47):
#     if f(a) == -2:
#         print(a)
# # 3


# 23
# Решение 1:
# def f(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     tens = str(start)[-2]
#     ones = str(start)[-1]
#     if int(tens) < int(ones):
#         start1 = int(str(start)[:-2] + ones + tens)
#         return f(start1, end) + f(start + 1, end)
#     return f(start + 1, end)
#
# print(f(101, 154))
# # 89

# Решение 2:
# def f(start, end):
#     d = {}
#     for i in range(start, end + 1):
#         d[i] = 0
#
#     d[start] = 1
#
#     for key in d.keys():
#         if key + 1 in d:
#             d[key + 1] += d[key]
#         if int(str(key)[:-2] + str(key)[-1] + str(key)[-2]) in d and (int(str(key)[-2]) < int(str(key)[-1])):
#             d[int(str(key)[:-2] + str(key)[-1] + str(key)[-2])] += d[key]
#     return d[end]
#
# print(f(101, 154))
# # 89


# 24
# Решение 1:
# f = open("24__7h77f (1).txt")
# s = f.readline()
# start = cc = cd = mx = 0
#
# for end in range(len(s)):
#     if s[end] == 'C':
#         cc += 1
#     if s[end] == 'D':
#         cd += 1
#     while cc > 2 or cd > 2:
#         if s[start] == 'C':
#             cc -= 1
#         if s[start] == 'D':
#             cd -= 1
#         start += 1
#     if cc <= 2 and cd <= 2:
#         mx = max(mx, end + 1 - start)
# print(mx)


# Решение 2:
# f = open("Файлы для пробников/24__7h77f (1).txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(mx + i, len(s)):
#         t = s[i:j+1]
#         if t.count('C') > 2 or t.count('D') > 2:
#             break
#         if t.count('C') <= 2 and t.count('D') <= 2:
#             mx = max(mx, len(t))
# print(mx)
# # 253


# 25
# def f(n):
#     divs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     if divs:
#         return sum(divs)//len(divs)
#     return 0
#
# stop = 0
# for n in range(750_001, 1_000_000):
#     F = f(n)
#     if F % 7 == 6:
#         print(n, int(F))
#         stop += 1
#     if stop == 5:
#         break
# # 750002 35482
# # 750007 16316
# # 750021 125005
# # 750022 29392
# # 750024 31919


# 26
# f = open("Файлы для пробников/26_4__94fik.txt")
# # f = open('test.txt')
# n, k = map(int, f.readline().split())
# data = [list(map(int, i.split())) for i in f]
#
# orders = []
# offers = []
# for i in range(n):
#     orders.append(data[i])
# for j in range(n, k + n):
#     offers.append(data[j])
#
# orders.sort()
# offers.sort(key=lambda x: (x[1], -x[0]))
# # for i in range(len(offers) - 1):
# #     if offers[i][1] == offers[i + 1][1]:
# #         print(offers[i], offers[i+1])
#
# for i in range(len(orders)):
#     rdt = orders[i][0]
#     for product in offers:
#         if product[0] >= rdt:
#             orders[i].append(product)
#             break
# print(orders)
#
# sm = 0
# mn_p = 10**10
# for el in orders:
#     s = el[-1][-1]
#     sm += s
#     mn_p = min(mn_p, el[-1][0])
# print(sm, mn_p)
# # 10046772 103


# 27A
# from math import *
# f = open("Файлы для пробников/27_5A__achn9.txt")
# w = f.readline()
# data = []
# for u in f:
#     x, y, par = u.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#
# # from turtle import *
# # lt(90)
# # m = 15
# # tracer(0)
# # screensize(4000, 4000)
# # up()
# #
# # for star in data:
# #     x, y, p = star
# #     goto(x*m, y*m)
# #     dot(3, 'blue')
# # done()
#
# old_clusters = []
# clusters = []
# trash = []
# anticenters = []
# r = 1.2
#
# while data:
#     old_clusters.append([data.pop(0)])
#     for i in old_clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 old_clusters[-1].append(j)
#                 data.remove(j)
# for a in old_clusters:
#     if len(a) > 50:
#         clusters.append(a)
#     else:
#         trash.append(a)
# print(len(clusters), len(trash))
#
# for k in range(len(clusters)):
#     mx = 0
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s > mx:
#             mx = s
#             mx_star = star
#     anticenters.append(mx_star)
#
# print(anticenters)
#
# from turtle import *
# lt(90)
# m = 15
# tracer(0)
# screensize(4000, 4000)
# up()
#
# colours = ['blue', 'orange', 'purple', 'yellow']
# for k in range(len(clusters)):
#     for star in clusters[k]:
#         x, y, p = star
#         goto(x*m, y*m)
#         dot(3, colours[k])
#
# for el in anticenters:
#     x1, y1, p1 = el
#     goto(x1*m, y1*m)
#     down()
#     dot(6, 'red')
#
# done()
#
# ans1 = 0
# for k in range(len(clusters)):
#     for star in clusters[k]:
#         if star[-1][1] == '9':
#             for i in clusters[k]:
#                 if i[-1][1] == '9':
#                     ans1 = max(ans1, dist(star[:2], i[:2]))
#
# r01 = dist(anticenters[0][:2], anticenters[1][:2])
# r12 = dist(anticenters[1][:2], anticenters[2][:2])
# r23 = dist(anticenters[2][:2], anticenters[3][:2])
# r30 = dist(anticenters[3][:2], anticenters[0][:2])
# p = (r01 + r12 + r23 + r30)/2
# ans2 = sqrt((p-r01)*(p-r12)*(p-r23)*(p-r30))
#
# print(int(ans1 * 10_000), int(ans2 * 10_000))
# # 42770 1893385


# 27B
# from math import *
#
# f = open("Файлы для пробников/27_5B__achna.txt")
# w = f.readline()
# data = []
# for u in f:
#     x, y, par = u.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#
# # from turtle import *
# # lt(90)
# # m = 15
# # tracer(0)
# # screensize(4000, 4000)
# # up()
# #
# # for star in data:
# #     x, y, p = star
# #     goto(x*m, y*m)
# #     dot(3, 'blue')
# # done()
#
# clusters = [[], [], [], []]
# anticenters = []
# for star in data:
#     x, y, p = star
#     if x < -4:
#         clusters[0].append(star)
#     if -2 < x < 4:
#         clusters[1].append(star)
#     if 6 < x < 12:
#         clusters[2].append(star)
#     if x > 14:
#         clusters[3].append(star)
#
# for k in range(len(clusters)):
#     mx = 0
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s > mx:
#             mx = s
#             mx_star = star
#     anticenters.append(mx_star)
#
# print(anticenters)
#
# # from turtle import *
# # lt(90)
# # m = 15
# # tracer(0)
# # screensize(4000, 4000)
# # up()
# #
# # colours = ['blue', 'orange', 'purple', 'yellow']
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y, p = star
# #         goto(x*m, y*m)
# #         dot(3, colours[k])
# #
# # for el in anticenters:
# #     x1, y1, p1 = el
# #     goto(x1*m, y1*m)
# #     down()
# #     dot(6, 'red')
# #
# # done()
#
# ans1 = 0
# for k in range(len(clusters)):
#     acent = anticenters[k]
#     s = 0
#     for star in clusters[k]:
#         x, y, par = star
#         if par[0] == 'F' and par[-1] == 'I' and par[-2] in '0123456789':
#                 if dist(acent[:2], star[:2]) <= 0.5:
#                     if star != acent:
#                         s += 1
#     ans1 += s
#
# print(ans1)
#
#
# ans2 = 0
# for k in range(len(clusters)):
#     q = 0
#     p = 0
#     for star in clusters[k]:
#         x, y, par = star
#         if par[-1] == 'I' and (par[-2] in '0123456789'):
#             q += 1
#         if par[-3:] == 'III':
#             p += 1
#     if q > p:
#         ans2 += 1
# print(ans1, ans2)
# # 4 1


