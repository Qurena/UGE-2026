# 2
# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 F = w and (z == (y and (not(x))))
#                 if F == 1:
#                     print(x, y, w, z)
# #yzwx


# 5
# def sxt(n):
#     s = ''
#     a = 'ABCDEFG'
#     while n != 0:
#         if n % 16 < 10:
#             s += str(n % 16)
#         else:
#             s += a[n % 16 - 10]
#         n //= 16
#     return s[::-1]
#
# def ans(n):
#     s = sxt(n)
#     sm = sum(int(i) for i in str(n))
#     av = int(sm/len(str(n)))
#     if av > 5:
#         s = '1' + s
#     else:
#         s = '2' + s
#     return int(s, 16)
#
# for n in range(10**9):
#     if 350 > ans(n) > 310:
#         print(n)
#         break
# # 57


# 6
# from turtle import *
# tracer(0)
# m = 15
# screensize(2000*2000)
#
# for _ in range(4):
#     fd(12*m)
#     lt(270)
#
# up()
#
# for _ in range(3):
#     fd(1*m)
#     lt(270)
#     fd(1*m)
#     lt(90)
#
# down()
#
# for _ in range(2):
#     fd(8*m)
#     lt(270)
#     fd(12*m)
#     lt(270)
#
# up()
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 54


# 9
# from itertools import *
# s = 'БОР'
# num = 0
# for i in product(s, repeat=5):
#     num += 1
#     g = ''.join(i)
#     if g == 'ОБРОБ' or g == 'РОББР':
#         print(g, num)
# # 88


# 12
# a = {
#     'q0.': ['.', 'L', 'q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q15': ['1', 'L', 'q1'],
#     'q17': ['1', 'L', 'q1'],
#     'q19': ['0', 'L', 'q1']
# }
# s1 = '5959595'
# s = list('..' + s1 + '..')
# i = -2
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(''.join(s))
# # 6991


# 13
# from ipaddress import *
# net = ip_network('200.60.130.4/20', 0)
#
# ans = 0
# for i in net:
#     ip = bin(int(i))[2:].zfill(32)
#     if ip.count('1') == 10:
#         ans += 1
# print(ans)
# # 66


# 14
# def sev(n):
#     s = ''
#     while n != 0:
#         s += str(n % 7)
#         n //= 7
#     return s[::-1]
#
# mx = []
# for x in range(1, 2301):
#     F = 7**350 + 7**150 - x
#     s = sev(F)
#     if s.count('0') == 200:
#         mx.append(x)
# print(max(mx))
# # 2001


# 15
# for A in range(20000):
#     flag = 1
#     for x in range(20000):
#         f = (x&21074 != 0) <= ((x&12369 == 0) <= (x&A != 0))
#         if f == 0:
#             flag = 0
#             break
#     if flag == 1:
#         print(A)
#         break
# # 16898


# 14
# from sys import *
# setrecursionlimit(10**9)
# def f(n):
#     if n == 1:
#         return 4
#     else:
#         return 4 * f(n - 1)
#
# print(f(4040)//(2**8059))
# # 2097152


# 15
# f = open("Файлы для пробников/8__1vf5e.txt")
# n = [int(i) for i in f.readlines()]
#
# ans = mx = 0
# for i in range(len(n) - 1):
#     t = [n[i], n[i+1]]
#     fv = sum(1 for i in t if i % 5 == 0)
#     if sum(t) % 10 == 0 and fv != 0:
#         ans += 1
#         mx = max(mx, sum(t))
# print(ans, mx)
# # 205 19720


# 19
# def steps(p):
#     return p + 3, p * 4
#
# def play(p, r):
#     if 120 > p >= 100 and r == 0:
#         return True
#
#     if 120 > p >= 100 or r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for s in range(1, 61):
#     if play(s, 1):
#         print(s)
#         break
# # 25


# 20-21
# def steps(p):
#     return p + 3, p * 4
#
# def play(p, r):
#     if 120 > p >= 100 and r % 2 == 0:
#         return True
#
#     if 120 > p >= 100 or r % 2 == 0:
#         return False
#
#     if r == 0 or p >= 120:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# for s in range(1, 61):
#     if not(play(s, 2)) and play(s, 4):
#         print(s)
# # хз, почему не работает...

# Второй вариант решения:
# from sys import *
# from functools import *
# setrecursionlimit(10**9)
#
# @lru_cache(None)
# def f(s):
#     if 120 > s >= 100:
#         return True
#     t = [f(s + 3), f(s * 4)]
#     n = [int(i) for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(62):
#     f(s)
#
# for s in range(1, 61):
#     if f(s) == -2:
#         print(s)
# # RecursionError: Stack overflow (used 2912 kB)


# 23
# def f(start, end):
#     d = {}
#
#     for i in range(start, end + 1):
#         d[i] = 0
#
#     d[start] = 1
#
#     if 12 in d:
#         del d[12]
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
# print(f(3, 40))
# # 11824582


# 24
# from re import *
# f = open("Файлы для пробников/24_4__6ao17.txt")
# s = f.readline()
# pattern = r"(?=(([1-9]+[02468]|[2468]+)\,([1-9]+[0-9]*[13579])))"
#
# mx = 0
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mx = max(mx, len(g) + 0)
# print(mx)
# # 46

# 25
# from fnmatch import fnmatch
# for i in range(0, 10**9 + 1, 12233):
#     if fnmatch(str(i), '?6?9*56'):
#         print(i, i//12233)
# # 16294356 1332
# # 167983556 13732
# # 260954356 21332
# # 364934856 29832
# # 468915356 38332
# # 660973456 54032
# # 764953956 62532
# # 868934456 71032
# # 961905256 78632


# 26
# f = open("Файлы для пробников/26_dif_3__40zrx.txt")
# # f = open("Файлы для пробников/test235236523.txt")
# k = int(f.readline())
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# for el in data:
#     el.append(el[1] - el[0])
# data.sort(key=lambda x: (x[0], x[2], x[1]))
#
# safe = [[[-8, -8, -8]] for _ in range(n)]
#
# for i in range(k):
#     for j in range(n):
#         if safe[j][-1][1] + 6 <= data[i][0]:
#             safe[j].append(data[i])
#             break
#
# for el in safe:
#     el.remove(el[0])
#
# ones = sum(len(i) for i in safe)
# ans1 = k - ones
#
# ans2 = 0
# for el in safe:
#     for el0 in el:
#         ans2 += el0[-1]
# print(ans1, ans2)
# # 1858 244078


# 27
# Файл A:
# from math import *
# f = open("Файлы для пробников/3_A__5i66i.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[], []]
#
# for i in data:
#     x, y = i
#     if -5 < x < -1 and -1 < y < 2:
#         clusters[0].append(i)
#     elif 1 < x < 5 and 3 < y < 6:
#         clusters[1].append(i)
#
# # from turtle import *
# # m = 15
# # tracer(0)
# # screensize(2000*2000)
# # up()
# #
# # for k in range(2):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# centers = []
# px = py = 0
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
#     px += mn_star[0]
#     py += mn_star[1]
# print(int(abs(px/2)*1000), int(abs(py/2)*1000))
# # 18 2293

# Файл B:
# from math import *
# f = open("Файлы для пробников/3_B__5i66k.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[], [], []]
#
# for i in data:
#     x, y = i
#     if -12 < x < -7.5 and -2 < y < 6:
#         clusters[0].append(i)
#     elif -1 < x < 3.1 and -13 < y < -5:
#         clusters[1].append(i)
#     elif 5 < x < 10 and 6 < y < 14:
#         clusters[2].append(i)
#
# # from turtle import *
# # m = 15
# # tracer(0)
# # screensize(2000*2000)
# # up()
# #
# # for k in range(3):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# centers = []
# px = py = 0
# for k in range(3):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#     px += mn_star[0]
#     py += mn_star[1]
# print(int(abs(px/3)*100), int(abs(py/3)*100))
# # 25 92