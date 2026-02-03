"""Решение пробника №8: https://3.shkolkovo.online/my/course/7259/dz/27815"""

# 2
# print('y w z x')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F1 = (w or not(y)) <= (z == x)
#                 F2 = (w or not(y)) == (x <= z)
#                 if F2 == 0:
#                     print(y, w, z, x)
# # ywzx


# 5
# def ans(n):
#     s = bin(n)[2:]
#     if n % 5 == 0:
#         s += '11'
#     else:
#         l = bin(n//5)[2:]
#         s += l
#     return int(s, 2)
#
# for n in range(1000):
#     if ans(n) >= 783 and n % 2 != 0:
#         print(n, ans(n))
#         break
# # 49


# 6
# from turtle import *
# tracer(0)
# m = 20
# screensize(200*200)
# lt(90)
#
# rt(45)
# for _ in range(70):
#     fd(5*m)
#     rt(45)
#     fd(10*m)
#     rt(135)
# up()
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'purple')
# done()
# # 27


# 8
# ans = 0
# for n in range(1, 10**6):
#     s = hex(n)[2:]
#     if len(s) == 4 and s.count('3') == 1:
#         if s[0] != s[1] and s[1] != s[2] and s[2] != s[3]:
#             ans += 1
# print(ans)
# # 11564


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q10': ['1', 'L', 'q1'],
#     'q11': ['0', 'S', 'q1']
# }
# s1 = '1110011'
# s = list('..'+s1+'..')
# i = -2
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     if c == 'L':
#         i -= 1
# print(''.join(s))
# # 523


# 13
# from ipaddress import *
# net = ip_network('98.81.154.195/255.252.0.0', 0)
# for ip in net.hosts():
#     print(ip)
# # 9883255254


# 14
# def six(n: int) -> str:
#     s = ''
#     while n != 0:
#         s += str(n % 6)
#         n //= 6
#     return s[::-1]
#
# for x in range(1, 2001):
#     n = 81 * (6**412) + 6**301 - 6**154 - x
#     nn = six(n)
#     if nn.count('0') == 114 and nn.count('1') > 1:
#         print(x)
# # 1295


# 16
# from sys import *
# setrecursionlimit(10**9)
#
# def f(n):
#     if n <= 4:
#         return 1
#     if n > 4 and n % 2 == 0:
#         return 7 * n + f(n-3)
#     if n > 4 and n % 2 != 0:
#         return (4*n)**4 + f(n-4)
#
# print(f(16432) - f(16422))
# # 46591566824555946822


# 17
# f = open("Файлы для пробников/17_2__8cp30.txt")
# a = [int(i) for i in f]
#
# def oddeven(t: list) -> int:
#     ans = 0
#     for el in t:
#         if el % 2 != 0:
#             ans += 1
#     return ans
#
# def d(t):
#     s = set()
#     for el in t:
#         p = str(el)[0]
#         s.add(int(p))
#     if len(s) == 5:
#         return True
#     return False
#
# count = 0
# mn = 10**10
# for i in range(len(a)-4):
#     t = [a[i], a[i+1], a[i+2], a[i+3], a[i+4]]
#     if d(t) and oddeven(t) == 3:
#         count += 1
#         mn = min(sum(t), mn)
# print(count, mn)
# # 744 8581


# 19
# Первый вариант решения:
# def steps(p):
#     return [p + 7, p * 3, p + 5]
#
# def play(p, r):
#     if 109 > p >= 65:
#         return r % 2 == 0
#
#     if r == 0 or p >= 109:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for p in range(1, 40):
#     if play(p, 1):
#         print(p)
# # 22

# Второй вариант решения:
# from sys import *
# setrecursionlimit(10**9)
# def f(a):
#     if a >= 65:
#         return False
#     t = []
#     if a + 5 < 109:
#         t.append(f(a + 5))
#     if a + 7 < 109:
#         t.append(f(a + 7))
#     if a * 3 < 109:
#         t.append(f(a * 3))
#     n = [int(i) for i in t if i <= 0]
#     if n:
#         return -min(n) + 1
#     return -min(t)
#
# for s in range(1, 40):
#     if f(s) == 1:
#         print(s)
# # 22


# 20
# def steps(p):
#     return [p + 7, p * 3, p + 5]
#
# def play(p, r):
#     if 109 > p >= 65:
#         return r % 2 == 0
#
#     if r == 0 or p >= 109:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for p in range(1, 40):
#     if play(p, 2) or play(p, 4):
#         print(p)
# # 8 9


# 21
# def steps(p):
#     return [p + 7, p * 3, p + 5]
#
# def play(p, r):
#     if 109 > p >= 65:
#         return r % 2 == 0
#
#     if r == 0 or p >= 109:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for p in range(1, 40):
#     if play(p, 3):
#         print(p)
# # 7 36


# 23
# def f24(start, end):
#     d = {}
#
#     for i in range(start, end + 1):
#         d[i] = 0
#
#     d[start] = 1
#
#     if 27 in d:
#         del d[27]
#
#     for key in d.keys():
#         if key + 1 in d:
#             d[key + 1] += d[key]
#         if key * 2 in d:
#             d[key * 2] += d[key]
#         if key * 3 in d:
#             d[key * 3] += d[key]
#     return d[end]
#
# def f27(start, end):
#     d = {}
#
#     for i in range(start, end + 1):
#         d[i] = 0
#
#     d[start] = 1
#
#     if 24 in d:
#         del d[24]
#
#     for key in d.keys():
#         if key + 1 in d:
#             d[key + 1] += d[key]
#         if key * 2 in d:
#             d[key * 2] += d[key]
#         if key * 3 in d:
#             d[key * 3] += d[key]
#     return d[end]
#
# def f(start, end):
#     d = {}
#
#     for i in range(start, end + 1):
#         d[i] = 0
#
#     d[start] = 1
#
#     for key in d.keys():
#         if key + 1 in d:
#             d[key + 1] += d[key]
#         if key * 2 in d:
#             d[key * 2] += d[key]
#         if key * 3 in d:
#             d[key * 3] += d[key]
#     return d[end]
#
# print(f24(9, 24)*f24(24, 81) + f27(9, 27)*f27(27, 81) + f(9, 24)*f(24, 27)*f(27, 81))
# # 142


# 24
# from re import *
# f = open("Файлы для пробников/24__7y15x.txt")
# s = f.readline()
#
# pattern = r'(?=([1-9]+(([+*][1-9]+)){1,39}))'
#
# mx = 0
# for i in finditer(pattern, s):
#
#     mx = max(mx, len(i.group(1)))
# print(mx)
# # 368


# 25
# def div(n: int) -> list[int]:
#     divs = []
#     for div in range(2, int(n**0.5) + 1):
#         if n % div == 0:
#             divs.append(div)
#             if div != n//div:
#                 divs.append(n//div)
#     return sorted(divs)
#
# def sim(divs: list) -> list[int]:
#     rtn = []
#     sumodd = sumeven = 0
#     for el in divs:
#         if el % 2 != 0:
#             sumodd += el
#         else:
#             sumeven += el
#     rtn.append(sumodd)
#     rtn.append(sumeven)
#     return rtn
#
# stop = 0
# for n in range(8 * (10**5), 9 * (10**5)):
#     d = div(n)
#     if sim(d)[0] % 2 == 0 and sim(d)[-1] % 10 == 4:
#         print(n, len(d))
#         stop += 1
#     if stop == 5:
#         break
# # 806450 16 814088 34 816642 28 819200 46 821762 4


# 26
# f = open("Файлы для пробников/demo_2025_26__7a4yn.txt")
# n = int(f.readline())
# info = [list(map(int, i.split())) for i in f]
# ni = []
# otl = []
# hor = []
#
# for el in info:
#     ni.append([el[0], sum(el[1:])/4, sum(1 for i in el[1:] if i == 2)])
#
# ni = sorted(ni, key=lambda x: x[1], reverse=True)
#
# for st in ni:
#     if st[1] == 5:
#         otl.append(st)
# otl = sorted(otl, key=lambda x: x[0])
#
# for st in ni:
#     if st[2] == 0 and st[1] != 5:
#         hor.append(st)
# hor = sorted(hor, key=lambda x: x[1], reverse=True)
# print(hor)
# понимаю, что делаю супер иррационально


# 27
# Файл A
# from math import sqrt
# f = open("Файлы для пробников/5_A__62ruo.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# def dist(star1, star2):
#     x1, y1, z1 = star1
#     x2, y2, z2 = star2
#     d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
#     return sqrt(d)
#
# clusters = [[], []]
#
# for i in a:
#     x, y, z = i
#     if x < 0:
#         clusters[0].append(i)
#     if y > 37.8:
#         clusters[1].append(i)
#
# px = py = pz = 0
# cent = []
# for k in range(2):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     cent.append(mn_star)
#     px += mn_star[0]
#     py += mn_star[1]
#     pz += mn_star[2]
#
# cx = px / 2
# cy = py / 2
# cz = pz / 2
# print(int(abs(cx)*100), int(abs(cy)*100), int(abs(cz)*100))
# # 561 2764 2221


# Файл B
# from math import sqrt
# f = open("Файлы для пробников/5_B__62ruq.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# def dist(star1, star2):
#     x1, y1, z1 = star1
#     x2, y2, z2 = star2
#     d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
#     return sqrt(d)
# # r = 0.5
# #
# # clusters = []
# # while a:
# #     clusters.append([a.pop(0)])
# #     for i in clusters[-1]:
# #         for j in a[:]:
# #             if dist3(i, j) <= r:
# #                 clusters[-1].append(j)
# #                 a.remove(j)
# # print(clusters)
#
# clusters = [[], [], [], []]
# for i in a:
#     x, y, z, = i
#     if -57 < x < -30 and 21 < y < 56:
#         clusters[0].append(i)
#     if -25 < x < 5 and 30 < y < 60:
#         clusters[1].append(i)
#     if (y > x - 55) and -0.5 < x < 25 and -50 < y < -20:
#         clusters[2].append(i)
#     if (y < x - 55) and 5 < x < 35 and -65 < y < -35:
#         clusters[3].append(i)
#
# # from turtle import *
# # m = 3
# # tracer(0)
# # screensize(200*200)
# # lt(90)
# #
# # up()
# # for k in range(4):
# #     for i in clusters[k]:
# #         x, y, z, = i
# #         goto(z*m, y*m)
# #         dot(3, 'purple')
# # done()
#
# px = py = pz = 0
# for k in range(4):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
#     pz += mn_star[2]
#
# cx = px / 4
# cy = py / 4
# cz = pz / 4
# print(int(abs(cx)*100), int(abs(cy)*100), int(abs(cz)*100))
# # 652 16 1147