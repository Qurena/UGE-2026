"""https://3.shkolkovo.online/my/course/7259/dz/30447"""

# 2
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((not(x)) and z and (not(y)) and (not(w))) or ((not(x)) and z and y and (not(w))) or ((not(x)) and z and y and w)
#                 if F == 1:
#                     print(x, y, z, w, int(F))
# # xywz


# 5
# def ans(n):
#     s = bin(n)[2:]
#     if n % 5 == 0:
#         s += '11'
#     else:
#         s += bin(n // 5)[2:]
#     return int(s, 2)
#
# for n in range(1, 1000, 2):
#     if ans(n) >= 783:
#         print(n)
#         break
# # 49


# 6
# from turtle import *
# lt(90)
# tracer(0)
# m = 15
# screensize(4000, 4000)
#
# for _ in range(7):
#     fd(15*m)
#     rt(90)
#     fd(23*m)
#     rt(90)
#
# up()
# fd(3*m)
# rt(90)
# fd(5*m)
# lt(90)
#
# down()
# for _ in range(7):
#     fd(252*m)
#     rt(90)
#     fd(398*m)
#     rt(90)
#
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 101084


# 8
# def ftn(n):
#     s = ''
#     a = '0123456789ABCDE'
#     while n != 0:
#         s += a[n % 15]
#         n //= 15
#     return s[::-1]
#
# p = '0123456789ABCDE'
# bad = []
# for el in p:
#     k = el*2
#     bad.append(k)
#
# ans = 0
# for n in range(1, 100_000):
#     q = ftn(n)
#
#     if q.count('8') == 1 and len(q) == 4:
#         l = 0
#         for m in bad:
#             if m in q:
#                 l += 1
#         if l == 0:
#             ans += 1
# print(ans)
# # 9295


# 13
# from ipaddress import *
#
# net = ip_network('167.66.136.176/255.254.0.0', 0)
#
# for ip in net.hosts():
#     print(ip)
#     break
# # 234


# 14
# # from string import ascii_uppercase
# # print(ascii_uppercase)
# def t(n):
#     s = ''
#     a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     while n != 0:
#         s += a[n % 29]
#         n //= 29
#     return s[::-1]
#
# mx_0 = -1
# for x in range(1, 8410 + 1):
#     F = (29**293) + (29**271) - x
#     q = t(F)
#     mx_0 = max(mx_0, q.count('0'))
# print(mx_0)
# # 24


# 15
# data = []
# for x in range(1, 100):
#     for y in range(1, 100):
#         if 2*y + 3*x == 152:
#             data.append(max(x, y))
#
# print(min(data)-1)
# # 30


# 16
# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n <= 10:
#         return n
#     return n - 12 + f(n - 21)
#
# for i in range(224357):
#     f(i)
#
# print((f(224356) - f(224272))/f(59))
# # 12125


# 17
# f = open("Файлы для пробников/17__7y5vp.txt")
# n = [int(i) for i in f]
#
# mx_3 = max(el for el in n if el < 0 and len(str(abs(el))) == 3 and el % 6 == 0)
#
# c = 0
# mx_s = 0
# for i in range(len(n) - 1):
#     t = n[i:i+2]
#     k1 = sum(1 for el in t if el < 0)
#     if k1 == 1 and sum(t) > mx_3:
#         c += 1
#         mx_s = max(mx_s, t[0]**2 + t[1]**2)
# print(c, mx_s)
# # 2553 19701728317


# 19
# 1 решение:
# from math import floor
#
# def steps(p):
#     return (p - 3, floor(p / 5))
#
# def play(p, r):
#     if p <= 505:
#         return r % 2 == 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(506, 107_000):
#     if play(s, 2) and (not(play(s, 1))):
#         print(s)
# # 12649


# 2 решение:
# from math import floor
# from functools import lru_cache
#
# @lru_cache(None)
# def f(a):
#     if a <= 505:
#         return 0
#
#     steps = [f(a - 3), f(floor(a / 5))]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(506, 20_000):
#     if f(s - 3) == 1 or f(floor(s / 5)) == 1:
#         print(s)
# # 12649


# 20
# 1 решение:
# from math import floor
#
# def steps(p):
#     return (p - 3, floor(p / 5))
#
# def play(p, r):
#     if p <= 505:
#         return r % 2 == 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(506, 107_000):
#     if play(s, 3) and (not(play(s, 1))):
#         print(s)
# # 2533 2534


# 2 решение:
# from math import floor
# from functools import lru_cache
#
# @lru_cache(None)
# def f(a):
#     if a <= 505:
#         return 0
#
#     steps = [f(a - 3), f(floor(a / 5))]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(506, 20_000):
#     if f(s) == 2:
#         print(s)
# # 2533 2534


# 21
# 1 решение:
# from math import floor
#
# def steps(p):
#     return (p - 3, floor(p / 5))
#
# def play(p, r):
#     if p <= 505:
#         return r % 2 == 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(506, 107_000):
#     if play(s, 4) and (not(play(s, 2))):
#         print(s)
# # 2536


# 2 решение:
# from math import floor
# from functools import lru_cache
#
# @lru_cache(None)
# def f(a):
#     if a <= 505:
#         return 0
#
#     steps = [f(a - 3), f(floor(a / 5))]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(506, 20_000):
#     if f(s) == -2:
#         print(s)
# # 2536


# 23
# def f(start, end, good):
#     if start > end:
#         return 0
#     if start == end and good == 1:
#         return 1
#
#     if start == 14 or start == 18:
#         good = 1
#
#     return f(start + 1, end, good) + f(start * 2, end, good) + f(start * 3, end, good)
#
# print(f(6, 48, 0))
# # 69


# 24
# from re import *
#
# f = open("Файлы для пробников/24__7y14j.txt")
# s = f.readline()
#
# pattern = r'(?=([1-9]+([+*][1-9]+){49}))'
#
# mx_l = 0
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mx_l = max(mx_l, len(g))
#     # if len(g) == 425:
#     #     print(g)
#     #     print(g.count('+') + g.count('*'))
#     #     k = i.start()
#     #     print(s[k - 1:k + 430])
# print(mx_l)
# # 428


# 25
# def is_prime(n):
#     if n <= 1:
#         return 0
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return 0
#     return 1
#
#
# def s(n):
#     s = 0
#     divs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             if is_prime(i):
#                 divs.add(i)
#             if is_prime(n // i):
#                 divs.add(n // i)
#     s = sum(divs)
#     return s
#
# stop = 0
# for n in range(1_325_000 - 1, 2, -1):
#     if s(n) != 0 and s(n) <= 30_000 and s(n) % 5 == 0:
#         stop += 1
#         print(n)
#     if stop == 5:
#         break
# # 1324994
# # 1324992
# # 1324991
# # 1324986
# # 1324980


# 26
# f = open("Файлы для пробников/26__7y63t.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
#
# # определим макс. номер дома и макс. номер подъезда
# # mx_num_h = 0
# # mx_num_p = 0
# # for el in data:
# #     nm_h = el[1]
# #     nm_p = el[2]
# #     mx_num_h = max(mx_num_h, nm_h)
# #     mx_num_p = max(mx_num_p, nm_p)
# # print(mx_num_h, mx_num_p)
# # 1000 1000
#
# houses = [[] for _ in range(1001)]
#
# for el in data:
#     id_z, h, p = el
#     houses[h].append(el)
#
# for i in range(len(houses)):
#     if houses[i]:
#         houses[i].sort(key=lambda x: x[-1])
#
# allens = []
# anses = []
# for i in range(len(houses)):
#     h = houses[i]
#     if h:
#         ln = 0
#         for p in range(len(h) - 1):
#             d = h[p+1][-1] - h[p][-1]
#             if d == 1:
#                 ln += 1
#             if d == 0:
#                 pass
#             if d != 0 and d != 1:
#                 allens.append(ln+1) # так как мы считали длину "линейки", а не кол-во цифр на ней
#                 ln = 0
#             if ln == 7 - 1:
#                 print(i, h[p-(ln-1)][2])
# # 171 701


# 27A
# from math import dist
#
# f = open("Файлы для пробников/27_A__7y44j.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# print(len(data))
#
# n_clusters = []
# clusters = []
# trash = []
# r = 1
#
# while data:
#     n_clusters.append([data.pop(0)])
#     for i in n_clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 n_clusters[-1].append(j)
#                 data.remove(j)
# for c in n_clusters:
#     if len(c) > 50:
#         clusters.append(c)
#         print(f'len(c):{len(c)}')
#     else:
#         trash.append(c)
#
# print(len(clusters), len(trash))
#
# anti_centers = []
# for k in range(len(clusters)):
#     mx = 0
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s > mx:
#             mx = s
#             mx_star = star
#     anti_centers.append(mx_star)
#
# p1 = sum(anti_centers[0])
# p2 = sum(anti_centers[1])
# print(int(abs(p1*10_000)), int(abs(p2*10_000)))
# # 1126711 1517181
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 1
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# #
# # up()
# #
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()


# 27B
# from math import dist
#
# f = open("Файлы для пробников/27_B__7y44k.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# print(len(data))
#
# n_clusters = []
# clusters = []
# trash = []
# r = 1
#
# while data:
#     n_clusters.append([data.pop(0)])
#     for i in n_clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 n_clusters[-1].append(j)
#                 data.remove(j)
# for c in n_clusters:
#     if len(c) > 50:
#         clusters.append(c)
#         print(f'len(c):{len(c)}')
#     else:
#         trash.append(c)
#
# print(len(clusters), len(trash))
#
# anti_centers = []
# for k in range(len(clusters)):
#     mx = 0
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s > mx:
#             mx = s
#             mx_star = star
#     anti_centers.append(mx_star)
#
# print(anti_centers)
# qx = 0
# qy = 0
# mx = 0
# mn = 10**10
# for k in range(len(anti_centers)):
#     ac = anti_centers[k]
#     if dist(ac, (0, 0)) > mx:
#         mx = dist(ac, (0, 0))
#         qx = ac[0]
#     if dist(ac, (0, 0)) < mn:
#         mn = dist(ac, (0, 0))
#         qy = ac[1]
#
# print(int(abs(qx*10_000)), int(abs(qy*10_000)))
# # 213883 264132
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 5
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# #
# # up()
# #
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(trash)):
# #     x, y = trash[k][0]
# #     goto(x * m, y * m)
# #     dot(7, 'red')
# #
# # done()