"""https://3.shkolkovo.online/my/course/7259/dz/32175"""

# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x <= w) and ((not(z)) or y) and (y <= x))
#                 if int(F) == 1:
#                     print(x, y, w, z, int(F))
# # xwzy


# 5
# def ans(n):
#     s = bin(n)[2:]
#     q = s[1:]
#     q = q.replace('0', '*')
#     q = q.replace('1', '0')
#     q = q.replace('*', '1')
#     p = s[0] + q
#     r = n + int(p, 2)
#     return r
#
# a = set()
# for n in range(1, 1000):
#     r = ans(n)
#     if r > 85 and n % 2 != 0:
#         a.add(n)
# print(min(a))
#
# # 33


# 6
# from turtle import *
# lt(90)
# tracer(0)
# m = 15
# screensize(4000, 4000)
#
# for _ in range(3):
#     for _ in range(5):
#         fd(5*m)
#         rt(60)
#     fd(5*m)
#     lt(60)
# up()
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 15


# 8
# from itertools import *
#
# s = '012345678'
# count = 0
# for i in product(s, repeat=5):
#     g = ''.join(i)
#     if (g.count('3') <= 1) and (g[0] not in '01357') and (g[-1] not in '18'):
#         count += 1
# print(count)
# # 18944


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q00': ['0', 'L', 'q1'],
#     'q01': ['0', 'L', 'q0'],
#     'q1.': ['.', 'S', 'q1'],
#     'q10': ['1', 'L', 'q1'],
#     'q11': ['0', 'L', 'q0']
# }
# s1 = '0101' + 50*'0'
# s = list('...' + s1 + '...')
# i = -3
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(''.join(s))
# # 1100


# 13
# print(bin(200)[2:])
# print(bin(192)[2:])
# print(int('11000000', 2))
# # 192


# 14
# def sev(n):
#     s = ''
#     while n != 0:
#         s += str(n % 7)
#         n //= 7
#     return s[::-1]
#
# for n in range(7**6 - 1000, 7**7+100):
#     print(sev(n), n)
# # 823544


# 16
# def f(n):
#     if n <= 1:
#         return n + 3
#     return f(n - 3) + n + 2
#
# ans = 0
# for n in range(1, 61):
#     k = f(n)
#     if k < 666:
#        ans += n
# print(ans)
# # 1770


# 17
# f = open("Файлы для пробников/17_17__8hqnx.txt")
# n = [int(i) for i in f]
# mx17 = max(el for el in n if el % 17 == 0)
# count = 0
# mn = 10**10
# for i in range(len(n) - 4):
#     t = n[i:i+5]
#     c1 = sum(1 for el in t if el % 2 == 0)
#     if c1 == 3 and sum(t) > mx17:
#         count += 1
#         mn = min(mn, sum(t))
# print(count, mn)
# # 8416 622108


# 19
# Решение 1:
# def steps(p):
#     return (p + 2, p * 2)
#
# def play(p, r):
#     if p >= 25:
#         return r % 2 == 0
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 25):
#     if play(s, 2) and (not(play(s, 1))):
#         print(s)
# # 11


# Решение 2:
# def f(a):
#     if a >= 25:
#         return False
#     steps = [f(a + 2), f(a * 2)]
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for s in range(1, 25):
#     if f(s) == -1:
#         print(s)
# # 11


# 20
# Решение 1:
# def steps(p):
#     return (p + 2, p * 2)
#
# def play(p, r):
#     if p >= 25:
#         return r % 2 == 0
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# ans = 0
# for s in range(1, 25):
#     if play(s, 3) and (not(play(s, 1))):
#         ans += 1
# print(ans)
# # 3


# Решение 2:
# def f(a):
#     if a >= 25:
#         return False
#     steps = [f(a + 2), f(a * 2)]
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# ans = 0
# for s in range(1, 25):
#     if f(s) == 2:
#         ans += 1
# print(ans)
# # 3


# 21
# Решение 1:
# def steps(p):
#     return (p + 2, p * 2)
#
# def play(p, r):
#     if p >= 25:
#         return r % 2 == 0
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 25):
#     if play(s, 4) and (not(play(s, 2))):
#         print(s)
# # 7 8


# Решение 2:
# def f(a):
#     if a >= 25:
#         return False
#     steps = [f(a + 2), f(a * 2)]
#     petya_win_check = [i for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for s in range(1, 25):
#     if f(s) == -2:
#         print(s)
# # 7 8


# 23
# Решение 1:
# def f(start, end):
#     if start > end or start == 8 or start == 15:
#         return 0
#     if start == end:
#         return 1
#     return f(start + 1, end) + f(start + 2, end) + f(start * 3, end)
#
# print(f(3, 10)*f(10, 22))
# # 390

# Решение 2:
# def f(start, end):
#     d = {}
#     for i in range(start, end + 1):
#         d[i] = 0
#
#     d[start] = 1
#     if 8 in d:
#         del d[8]
#     if 15 in d:
#         del d[15]
#
#     for key in d.keys():
#         if key + 1 in d:
#             d[key + 1] += d[key]
#         if key + 2 in d:
#             d[key + 2] += d[key]
#         if key * 3 in d:
#             d[key * 3] += d[key]
#     return d[end]
#
# print(f(3, 10)*f(10, 22))
# # 390


# 24
# Решение 1:
# from re import *
# f = open("Файлы для пробников/24__3ns0t.txt")
# s = f.readline()
#
# pattern = r'(?=(([^B]*)(B[^B]*){53}))'
# mx = 0
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mx = max(mx, len(g))
# print(mx)
# # 515

# Решение 2:
# f = open("Файлы для пробников/24__3ns0t.txt")
# s = f.readline()
# cb = start = mx = 0
# for end in range(len(s)):
#     if s[end] == 'B':
#         cb += 1
#     while cb > 53:
#         if s[start] == 'B':
#             cb -= 1
#         start += 1
#     if cb == 53:
#         mx = max(mx, end + 1 - start)
# print(mx)
# # 515


# Решение 3:
# f = open("Файлы для пробников/24__3ns0t.txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(mx + i, len(s)):
#         t = s[i:j + 1]
#         if t.count('B') > 53:
#             break
#         if t.count('B') == 53:
#             mx = max(mx, len(t))
# print(mx)
# # 515


# 25
# def s_find(n):
#     divs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n // i)
#     if len(divs) >= 6:
#         s = list(divs)
#         s.sort(reverse=True)
#         return sum(s[:6])
#     return 0
#
# stop = 0
# for n in range(20_001, 100_000):
#     k = s_find(n)
#     if k > 0 and k % 25 == 0:
#         print(n, k)
#         stop += 1
#     if stop == 5:
#         break
# # 20056 19075
# # 20106 23475
# # 20188 20600
# # 20196 29325
# # 20250 28575


# 26
# f = open("Файлы для пробников/Задание_26__lood__rjlq.txt")
# # f = open("test.txt")
# n = int(f.readline())
# data = [[] for _ in range(10_001)]
# for el in f:
#     row, sit = map(int, el.split())
#     data[row].append(sit)
#
# lens = []
# for i in range(len(data)):
#     p = data[i]
#     if p:
#         p.sort()
#         l = 1
#         for k in range(len(p) - 1):
#             if p[k + 1] - p[k] == 1:
#                 l += 1
#             if p[k + 1] - p[k] == 0:
#                 pass
#             if p[k + 1] - p[k] > 1:
#                 lens.append([l, i])
#                 l = 1
#         lens.append([l, i])
#
# ans1 = 0
# for el in lens:
#     ans1 = max(ans1, el[0])
#
# ans2 = 10**10
# for el in lens:
#     l = el[0]
#     if l == ans1:
#         ans2 = min(ans2, el[1])
# print(ans1, ans2)
# # 2 29


# 27A
# from math import dist
# f = open("Файлы для пробников/27_2A__achhc (1).txt")
# u = f.readline()
# data = []
# for el in f:
#     x, y, par = el.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#
# old_clusters = []
# clusters = []
# centers = []
# trash = []
# r = 1.2
# print(len(data))
#
# while data:
#     old_clusters.append([data.pop(0)])
#     for i in old_clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 old_clusters[-1].append(j)
#                 data.remove(j)
# check = 0
# for o in old_clusters:
#     if len(o) > 50:
#         print(f'len(c):{len(o)}')
#         check += len(o)
#         clusters.append(o)
#     else:
#         trash.append(o)
# print(len(clusters), len(trash), check)
#
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
# print(centers)
#
# ans1 = set()
# for k in range(len(clusters)):
#     for star in clusters[k]:
#         x, y, par = star
#         if par[0] == 'G' and par[-3:] == 'VII' and par[-4] in '0123456789':
#             for i in clusters[k]:
#                 xi, yi, pari = i
#                 if pari[-2:] == 'II' and pari[-3] in '0123456789':
#                     if dist(star[:2], i[:2]) <= 0.8:
#                         ans1.add(star[0])
# ans2 = 0
# for star in clusters[2]:
#     x, y, par = star
#     if par[0] == 'J':
#         ans2 += dist(centers[2][:2], star[:2])
# print(int(len(ans1)), int(ans2*1000))
# # 11 94839
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 10
# # screensize(4000, 4000)
# # up()
# #
# # for k in range(len(clusters)):
# #     xc, yc, pc = centers[k]
# #     goto(xc*m, yc*m)
# #     dot(6, 'red')
# #     for star in clusters[k]:
# #         x, y, p = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(trash)):
# #     for star in trash[k]:
# #         x, y, p = star
# #         goto(x*m, y*m)
# #         dot(10, 'purple')
# # done()


# 27B
# from math import dist
# f = open("Файлы для пробников/27_2B__achhd (1).txt")
# u = f.readline()
# data = []
# for el in f:
#     x, y, par = el.split()
#     data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#
# old_clusters = []
# clusters = []
# centers = []
# trash = []
# r = 0.8
# print(len(data))
#
# while data:
#     old_clusters.append([data.pop(0)])
#     for i in old_clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 old_clusters[-1].append(j)
#                 data.remove(j)
# check = 0
# for o in old_clusters:
#     if len(o) > 50:
#         print(f'len(c):{len(o)}')
#         check += len(o)
#         clusters.append(o)
#     else:
#         trash.append(o)
# print(len(clusters), len(trash), check)
#
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
# print(centers)
#
# ans1 = 0
# counts = []
# for k in range(len(clusters)):
#     c = 0
#     for star in clusters[k]:
#         x, y, par = star
#         if par[-3:] == 'III' and par[-4] in '0123456789':
#             c += 1
#     counts.append(c)
# ans1 = dist(centers[5][:2], centers[2][:2])
#
# ans2 = 0
# for k in range(len(clusters)):
#     for star in clusters[k]:
#         x, y, par = star
#         if par[-1] == 'V' and par[-2] in '0123456789':
#             ans2 = max(ans2, dist(centers[k][:2], star[:2]))
# print(int(ans1 * 1000), int(ans2 * 1000))
# # 30959 2824
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 12
# # screensize(4000, 4000)
# # up()
# #
# # for k in range(len(clusters)):
# #     # xc, yc, pc = centers[k]
# #     # goto(xc*m, yc*m)
# #     # dot(6, 'red')
# #     for star in clusters[k]:
# #         x, y, p = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(trash)):
# #     for star in trash[k]:
# #         x, y, p = star
# #         goto(x*m, y*m)
# #         dot(10, 'purple')
# # done()