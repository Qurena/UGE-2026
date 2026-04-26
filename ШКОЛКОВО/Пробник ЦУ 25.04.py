# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(x or y)) or w or (x or (not(z))) and y
#                 if F == 0:
#                     print(x, y, w, z, int(F))
# # ywzx


# 5
# def ans(n):
#     k1 = 1
#     for i in str(n):
#         if int(i) != 0:
#             k1 *= int(i)
#     mn = min(int(i) for i in str(n))
#     mx = max(int(i) for i in str(n))
#     k2 = mx - mn
#
#     t1 = k1 + k2
#     t2 = k1*k2 + 1
#
#     if t1 >= t2:
#         r = int(str(t2) + str(t1))
#     else:
#         r = int(str(t1) + str(t2))
#
#     return r
#
# for n in range(10000):
#     if ans(n) == 25127:
#         print(n)
# # 92


# 6
# from turtle import *
# tracer(0)
# lt(90)
# m = 10
# screensize(4000, 4000)
#
# rt(45)
# for _ in range(7):
#     fd(12*m)
#     rt(45)
#     fd(10*m)
#     rt(135)
#
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 72


# 8
# from itertools import *
# s = 'ИСКАНДЕР'
# glass = ['А', 'И', 'Е']
#
# ans = 0
# for i in product(s, repeat=6):
#     g = ''.join(i)
#     gl = sum(1 for i in g if i in glass)
#     if gl == 1:
#         if g[0] in glass or g[-1] in glass:
#             ans += 1
# print(ans)
# # 18750


# 12
# s = '1' + '9'*100
#
# while ('19' in s) or ('299' in s) or ('3999' in s):
#     if '19' in s:
#         s = s.replace('19', '2', 1)
#     if '299' in s:
#         s = s.replace('299', '3', 1)
#     if '3999' in s:
#         s = s.replace('3999', '1', 1)
# print(s)
# # 39


# 13
# from ipaddress import *
#
# net = ip_network('98.81.154.195/255.252.0.0', 0)
#
# for ip in net.hosts():
#     print(ip)
# # 9883255254


# 14
# def six(n):
#     s = ''
#     a = '0123456789ABCDEF'
#     while n != 0:
#         s += a[n % 16]
#         n //= 16
#     return s[::-1]
#
# f = 16 * (64**8) - 3 * (256**8) - 6 * (16**9) - 2 * (4**6) + 4 * (4096**6) + 5 * (1024**2)
# print(six(f))
# # 3FD000FFFA0004FE000


# 15
# for x in range(0, 1000):
#     for y in range(0, 1000):
#         if x + 2*y == 60 and y >= x:
#             print(y)
# # 19


# 16
# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n - 1)
#
# for i in range(100_000):
#     f(i)
#
# print((f(87654) - 87650 * f(87653))/f(87652))
# # 350612


# 17
# f = open("17.txt")
# n = [int(i) for i in f.readlines()]
# mnc = min(i for i in n if i > 0 and i % 2 != 0)
#
# count = 0
# mnsum = set()
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     evens = sum(1 for el in t if abs(el) % 2 == 0)
#     if max(t) % mnc == 0 and evens >= 2:
#         count += 1
#         mnsum.add(sum(t))
# print(count, min(mnsum))
# # 556-27330


# 19
# # решение 1:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 75:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 67):
#     p = (8, s)
#     if not(play(p, 1)) and play(p, 2):
#         print(s)
# # 33


# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 75:
#         return 0
#
#     steps = [f(a + 1, b), f(a, b + 1), f(a * 2, b), f(a, b * 2)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(1, 67):
#     if f(8, s) == -1:
#         print(s)
# # 33


# 20
# решение 1:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 75:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 67):
#     p = (8, s)
#     if not(play(p, 1)) and play(p, 3):
#         print(s)
# # 29 32


# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 75:
#         return 0
#
#     steps = [f(a + 1, b), f(a, b + 1), f(a * 2, b), f(a, b * 2)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(1, 67):
#     if f(8, s) == 2:
#         print(s)
# # 29 32


# 21
# решение 1:
# def steps(p):
#     h1, h2 = p
#     return [(h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)]
#
# def play(p, r):
#     if sum(p) >= 75:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 67):
#     p = (8, s)
#     if not(play(p, 2)) and play(p, 4):
#         print(s)
# # 28


# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 75:
#         return 0
#
#     steps = [f(a + 1, b), f(a, b + 1), f(a * 2, b), f(a, b * 2)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(1, 67):
#     if f(8, s) == -2:
#         print(s)
# # 28


# 23
# def f(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#
#     if int(str(start)[-1]) < int(str(start)[0]):
#         return f(int(str(start)[-1] + str(start)[0]), end) + f(start - 3, end)
#     return f(start - 3, end)
#
# print(f(43, 13))
# # 4


# 24
# f = open("24.txt")
# s = f.readline().upper()
# a = 'ABCDEFGHIJKLMNOPRQRSTUVWXYZ'
#
# for letter in s:
#     if letter in a:
#         a = a.replace(letter, '*')
# print(a)
# # 6


# 25
# def divs(x):
#     div = set()
#
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             if i % 10 == 7 and i != 7 and i != x:
#                 div.add(i)
#             if (x//i) % 10 == 7 and (x//i) != 7 and (x//i) != x:
#                 div.add((x//i))
#     if div:
#         return div
#     return 0
#
# stop = 0
# for x in range(600_001, 10**10):
#     if divs(x) != 0:
#         print(x, min(divs(x)))
#         stop += 1
#     if stop == 5:
#         break
# # 600001 437
# # 600002 47
# # 600003 1227
# # 600005 217
# # 600012 16667


# 26
# from math import ceil
#
# f = open('26.txt')
# # f = open('test')
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
#
# amount = set()
# for st in data:
#     amount.add(st[1])
# amount = list(amount)
# amount.sort()
#
# schools = []
# for i in range(len(amount)):
#     schools.append([[amount[i]]])
#
# for st in data:
#     for i in range(len(amount)):
#         if st[1] == schools[i][0][0]:
#             schools[i].append(st)
#
# ans2 = 0
# smart_fcks = []
# for sch in schools:
#     sch.remove(sch[0])
#     sch.sort(key=lambda x: -x[2])
#
#     passing_amount = ceil(len(sch) * 0.2)
#
#     smart_st_in_school = []
#
#     kvota = 0
#     passed = 0
#     for student in sch:
#         if smart_st_in_school != []:
#             if student[-1] == smart_st_in_school[-1][-1]:
#                 smart_st_in_school.append(student)
#                 kvota += 1
#                 smart_fcks.append(student[0])
#             if student[-1] >= 50 and student[-1] != smart_st_in_school[-1][-1]:
#                 if passed < passing_amount:
#                     smart_st_in_school.append(student)
#                     passed += 1
#                     smart_fcks.append(student[0])
#         if student[-1] >= 50 and smart_st_in_school == []:
#             if passed < passing_amount:
#                 smart_st_in_school.append(student)
#                 passed += 1
#                 smart_fcks.append(student[0])
#
#     if smart_st_in_school:
#         if passed + kvota > passing_amount:
#             ans2 += 1
#             # print(smart_st_in_school, passed, kvota, passing_amount)
#
# ans1 = min(smart_fcks)
# print(ans1, ans2)
# # 5 98


# 27
# Файл A:
# from math import dist
#
# f = open("27A.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# print(f'len(data): {len(data)}')
# clusters = []
# n_clusters = []
# trash = []
# r = 1
#
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
#
# for c in clusters:
#     if len(c) > 50:
#         n_clusters.append(c)
#         print(f'len(c): {len(c)}')
#     else:
#         trash.append(c)
#
# print(f'len(n_clusters): {len(n_clusters)}')
# print(f'len(trash): {len(trash)}')
#
# centers = []
# for k in range(len(n_clusters)):
#     mn = 10**10
#     for star in n_clusters[k]:
#         s = 0
#         for i in n_clusters[k]:
#             s += dist(star, i)
#         if mn > s:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#
# p1 = dist(centers[0], centers[1])
# p2 = 0
# for k in range(len(centers)):
#     for i in n_clusters[k]:
#         p2 = max(p2, dist(centers[k], i))
#
# print(int(p1*10_000), int(p2*10_000))
# # 160921 25049
#
# # from turtle import *
# # tracer(0)
# # lt(90)
# # m = 5
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# # screensize(4000, 4000)
# #
# # up()
# # for k in range(len(n_clusters)):
# #     for i in n_clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(trash)):
# #     for i in trash[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(6, 'purple')
# #
# # for i in centers:
# #     x, y = i
# #     goto(x*m, y*m)
# #     dot(6, 'red')
# # done()


# Файл B:
# from math import dist
#
# f = open("27B.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# print(f'len(data): {len(data)}')
# clusters = []
# n_clusters = []
# trash = []
# r = 1
#
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
#
# for c in clusters:
#     if len(c) > 50:
#         n_clusters.append(c)
#         print(f'len(c): {len(c)}')
#     else:
#         trash.append(c)
#
# print(f'len(n_clusters): {len(n_clusters)}')
# print(f'len(trash): {len(trash)}')
#
# centers = []
# q1 = 0
# q2 = 0
# for k in range(len(n_clusters)):
#     mn = 10**10
#     for star in n_clusters[k]:
#         s = 0
#         for i in n_clusters[k]:
#             s += dist(star, i)
#         if mn > s:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#     q1 += mn_star[0]
#     q2 += mn_star[1]
# print(int(abs((q1/3)*10_000)), int(abs((q2/3)*10_000)))
# # 189300 106295



# from turtle import *
# tracer(0)
# lt(90)
# m = 5
# for _ in range(4):
#     fd(100*m)
#     back(100*m)
#     lt(90)
# screensize(4000, 4000)
#
# up()
# for k in range(len(n_clusters)):
#     for i in n_clusters[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3, 'blue')
#
# for k in range(len(trash)):
#     for i in trash[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(6, 'purple')
#
# for i in centers:
#     x, y = i
#     goto(x*m, y*m)
#     dot(6, 'red')
# done()
