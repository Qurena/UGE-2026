"""https://3.shkolkovo.online/my/course/7259/dz/31523"""


# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and (not(z)) and (not(w))) or (x and (not(z)) and y)
#                 if F == 1:
#                     print(x, y, w, z, int(F))
# # wxyz


# 5
# def t(n):
#     s = ''
#     while n != 0:
#         s += str(n % 3)
#         n //= 3
#
#     return s[::-1]
#
# def ans(n):
#     s = t(n)
#     if n % 3 == 0:
#         p = s[-2:]
#         s += p
#     else:
#         sm = sum(int(el) for el in s) * 2
#         s += t(sm)
#     return int(s, 3)
#
# a = set()
# for n in range(1, 1000):
#     l = ans(n)
#     if l % 2 != 0 and l > 520:
#         a.add(l)
# print(min(a))
# # 567


# 6
# from turtle import *
# lt(90)
# tracer(0)
# screensize(4000, 4000)
# m = 5
#
# for _ in range(6):
#     fd(71 * m)
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
#
# up()
# for x in range(-30, 60):
#     for y in range(-30, 60):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 2295


# 8
# from itertools import *
#
# s = 'ВИЛМОС'
# num = 0
#
# for i in product(s, repeat=5):
#     g = ''.join(i)
#     num += 1
#     if num % 2 != 0:
#         if g[0] not in 'ОС' and g.count('В') == 1 and g.count('С') <= 1:
#             print(g, num)
# # 5137


# 12
# a = {
#     'q0.':['.', 'R', 'q1'],
#     'q1.':['1', 'R', 'q2'],
#     'q10': ['0', 'R', 'q1'],
#     'q11': ['1', 'R', 'q1'],
#     'q2.': ['1', 'R', 'q3'],
#     'q3.': ['.', 'S', 'q3']
# }
# s1 = bin(2027)[2:]
# s = list('...' + s1 + '...')
# i = 2
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i += 1
# print(''.join(s))
# print(int('1111110101111', 2))
# # 8111


# 13
# from ipaddress import *
#
# net = ip_network('191.89.109.206/255.255.224.0', 0)
# for ip in net.hosts():
#     print(eval(str(ip).replace('.','+')))
# # 661


# 14
# for x in range(0, 23):
#     F1 = 5 * 23**0 + 3 * 23**1 + 0 * 23**2 + x * 23**3 + 1 * 23**4 + 6 * 23**5 + 7 * 23**6
#     F2 = 2 * 23**0 + 3 * 23**1 + 9 * 23**2 + x * 23**3 + 8 * 23**4 + 3 * 23**5 + 3 * 23**6
#     F = F1 + F2
#     if x == 8:
#         print(F//22)
# # 70045642


# 16
# from sys import *
# setrecursionlimit(10**9)
#
# def f(n):
#     if n >= 21:
#         return f(n-8) + 1095
#     return 10 * (g(n-7)-36)
#
# def g(n):
#     if n >= 22_560:
#         return n/23 + 33
#     return g(n + 11) - 4
#
# print(f(548))
# # 50


# 17
# f = open("Файлы для пробников/17__a7wt8.txt")
# n = [int(el) for el in f]
# mx28 = max(el for el in n if abs(el) % 100 == 28)
#
# count = sm = 0
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     c3 = sum(1 for el in t if len(str(abs(el))) == 3)
#     if c3 >= 1 and 0 < (sum(t)/3) < mx28:
#         count += 1
#         sm = max(sm, sum(t))
# print(count, sm)
# # 1290 193483


# 19
# решение 1:
# def steps(p):
#     return [p + 1, p + 5, p * 3]
#
# def play(p, r):
#     if p >= 124:
#         return r % 2 == 0
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 124):
#     if play(s, 2) and (not(play(s, 1))):
#         print(s)
# # 41

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a):
#     if a >= 124:
#         return False
#     steps = [f(a + 1), f(a + 5), f(a * 3)]
#     petya_win_check = [int(i) for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for s in range(1, 124):
#     if f(s) == -1:
#         print(s)
# # 41


# 20
# решение 1:
# def steps(p):
#     return [p + 1, p + 5, p * 3]
#
# def play(p, r):
#     if p >= 124:
#         return r % 2 == 0
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 124):
#     if play(s, 3) and (not(play(s, 1))):
#         print(s)
# # 36 40

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a):
#     if a >= 124:
#         return False
#     steps = [f(a + 1), f(a + 5), f(a * 3)]
#     petya_win_check = [int(i) for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for s in range(1, 124):
#     if f(s) == 2:
#         print(s)
# # 36 40


# 21
# решение 1:
# def steps(p):
#     return [p + 1, p + 5, p * 3]
#
# def play(p, r):
#     if p >= 124:
#         return r % 2 == 0
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for s in range(1, 124):
#     if play(s, 4) and (not(play(s, 2))):
#         print(s)
# # 35

# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a):
#     if a >= 124:
#         return False
#     steps = [f(a + 1), f(a + 5), f(a * 3)]
#     petya_win_check = [int(i) for i in steps if i <= 0]
#     if petya_win_check:
#         return -max(petya_win_check) + 1
#     return -max(steps)
#
# for s in range(1, 124):
#     if f(s) == -2:
#         print(s)
# # 35


# 23
# решение 1:
# def f(start, end):
#     if start < end or start == 73:
#         return False
#     if start == end:
#         return True
#
#     return f(start - 3, end) + f(start - 8, end) + f(start//2, end)
#
# print(f(76, 41)*f(41, 12))

# решение 2:
# def f(start, end):
#     d = {}
#
#     for i in range(start, end - 1, -1):
#         d[i] = 0
#
#     if 73 in d:
#         del d[73]
#
#     d[start] = 1
#     for key in d.keys():
#         if key - 3 in d:
#             d[key - 3] += d[key]
#         if key - 8 in d:
#             d[key - 8] += d[key]
#         if key//2 in d:
#             d[key//2] += d[key]
#     return d[end]
#
# print(f(76, 41)*f(41, 12))
# # 80


# 24
# решение 1:
# f = open("Файлы для пробников/24__a7x9e.txt")
# s = f.readline()
#
# start = c20 = cgl = 0
# mn = 10**10
# for end in range(len(s)):
#     if s[end - 1:end + 1] == '20':
#         c20 += 1
#     if s[end] in 'AEIOUY':
#         cgl += 1
#     while c20 > 26 or cgl > 1:
#         if s[start-1:start + 1] == '20':
#             c20 -= 1
#         if s[start] in 'AEIOUY':
#             cgl -= 1
#         start += 1
#     if s[end] in 'AEIOUY' and c20 == 26 and cgl == 1:
#         mn = min(mn, end - start + 1)
# print(mn)
# # 58

# решение 2:
# from re import *
# f = open("Файлы для пробников/24__a7x9e.txt")
# s = f.readline()
#
# pattern = r'[^2AEIOUY]*[^0AEIOUY]*(20[^2AEIOUY]*[^0AEIOUY]*){26}[AEIOUY]'
# mn = 10**10
# for i in finditer(pattern, s):
#     g = i.group(0)
#     print(g)
#     mn = min(mn, len(g))
# print(mn)
# # как упростить регулярку, чтобы код быстрее работал?


# 25
# def is_prime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
# def d(n):
#     divs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     return divs
#
# stop = 0
# for n in range(8_996_453, 9_100_000):
#     if d(n):
#         dvs = []
#         for el in d(n):
#             if is_prime(el):
#                 c3 = sum(1 for digit in str(el) if digit == '3')
#                 if c3 == 2:
#                     dvs.append(el)
#         for el1 in dvs:
#             for el2 in dvs:
#                 if n == el1*el2:
#                     print(n, max(dvs))
#                     stop += 1
#         if stop == 5:
#             break
# # 9001609 24133
# # 9002887 38639
# # 9006149 38653
# # 9012167 3853
# # 9012373 23531


# 26
# f = open("Файлы для пробников/26__a7ysc.txt")
# n = int(f.readline())
# land = []
# num = 0
# for st in f:
#     num += 1
#     start, ln_lnd = st.split()
#     land.append([int(start), int(start) + int(ln_lnd), num, 1])
#
# land.sort(key=lambda x: x[1])
# for el1 in land:
#     flag = 0
#     for el2 in land:
#         if el1[2] != el2[2]:
#             if el1[1] == el2[0]:
#                 land.append([el1[0], el2[1], 'somenum', el1[-1] + el2[-1]])
#                 land.remove(el2)
#                 flag = 1
#     if flag == 1:
#         land.remove(el1)
#
# land.sort(key=lambda x: x[1])
#
# cleaning_h = [land.pop(0)]
#
# for el in land:
#     if el[0] >= cleaning_h[-1][1]:
#         cleaning_h.append(el)
#
# prelast_h = cleaning_h[-2]
# ans2 = []
# for el in land:
#     if el[0] >= prelast_h[1]:
#         ans2.append(el[1])
#
# count = 0
# for el in cleaning_h:
#     count += el[-1]
# print(count, 10_000 - max(ans2))
# # 69 184


# 27A
# from math import *
# f = open("Файлы для пробников/27_A__a7xle.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# bef_cl = []
# clusters = []
# r = 0.7
# print(len(data))
#
# while data:
#     bef_cl.append([data.pop(0)])
#     for i in bef_cl[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 bef_cl[-1].append(j)
#                 data.remove(j)
#
# print('lengths of clusters:')
# la = 0
# for p in bef_cl:
#     if len(p) > 100:
#         print(len(p))
#         print('-----------')
#         clusters.append(p)
#         la += len(p)
# print(len(clusters), la)
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
# a1 = a2 = 0
# q = centers[1][1]
# for star in clusters[1]:
#     if star[1] < q:
#         a1 += 1
# a2 = abs(centers[0][0] - centers[1][0])
#
# print(a1, int(a2 * 10_000))
# # 173 27601


# 27B
# from math import *
# f = open("Файлы для пробников/27_B__a7xld.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# bef_cl = []
# clusters = []
# r = 1
# print(len(data))
#
# while data:
#     bef_cl.append([data.pop(0)])
#     for i in bef_cl[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 bef_cl[-1].append(j)
#                 data.remove(j)
#
# print('lengths of clusters:')
# la = 0
# for p in bef_cl:
#     if len(p) > 100:
#         print(len(p))
#         print('-----------')
#         clusters.append(p)
#         la += len(p)
# print(len(clusters), la)
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
# b1 = b2 = 0
# q = centers[2]
# for star in clusters[2]:
#     if q[0] - 0.9 <= star[0] <= q[0] + 0.9:
#         if q[1] - 0.9 <= star[1] <= q[1] + 0.9:
#             b1 += 1
# b2 = abs(centers[0][1] - centers[1][1])
#
# print(b1, int(b2 * 10_000))
# # 89 107171