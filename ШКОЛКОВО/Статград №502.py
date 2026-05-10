"""https://3.shkolkovo.online/my/course/7259/dz/31522"""


# 2
# print('z y x w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = y <= ( (z <= x) and w )
#                 print(z, y, x, w, int(F))
# # zyxw


# 5
# def ans(n):
#     s = bin(n)[2:]
#     sm = sum(int(i) for i in s)
#     if sm % 2 == 0:
#         s += '0'
#         s = '1' + s[2:]
#     else:
#         s += '1'
#         s = '11' + s[2:]
#     r = int(s, 2)
#     return r
#
#
# for n in range(10**5):
#     if ans(n) == 766:
#         print(n)
# # 639


# 6
# from turtle import *
# screensize(4000, 4000)
# m = 2
#
# rt(9)
# for _ in range(8):
#     fd(97*m)
#     rt(135)
#     fd(81*m)
#     rt(45)
# done()
# # 2778


# 8
# ans = 0
# for n in range(4096, 65537):
#     h = hex(n)[2:].upper()
#     if h.count('E') == 1 and len(h) == 4:
#         h = '.' + h + '.'
#         index_e = h.find('E')
#         even = '02468ACE'
#         if (h[index_e - 1]) not in even and (h[index_e + 1] not in even):
#             ans += 1
# print(ans)
# # 5336


# 12
# a = {
#     'q0.': ['.', 'R', 'q1'],
#
#     'q1.': ['1', 'L', 'q2'],
#     'q10': ['0', 'R', 'q1'],
#     'q11': ['1', 'R', 'q1'],
#
#     'q2.': ['0', 'L', 'q3'],
#     'q20': ['1', 'L', 'q2'],
#     'q21': ['1', 'L', 'q2'],
#
#     'q3.': ['1', 'L', 'q4'],
#
#     'q4.': ['1', 'S', 'q4']
# }
#
# def f(n):
#     s1 = bin(n)[2:]
#     s = list('....' + s1 + '....')
#     i = 3
#     c = 0
#     p = 'q0'
#     while c != 'S':
#         s[i], c, p = a[p + s[i]]
#         if c == 'L':
#             i -= 1
#         if c == 'R':
#             i += 1
#     res = ''.join(i for i in s if i in '01')
#     return int(res, 2)
#
# for n in range(10**4):
#     if f(n) <= 941:
#         print(f(n))
# # 895

# 13
# from ipaddress import *
#
# net = ip_network('178.176.0.0/255.240.0.0', 0)
#
# ans = set()
# for ip in net.hosts():
#     dp = bin(int(ip))[2:].zfill(32)
#     if dp.count('0') == dp.count('1'):
#         r = str(ip).split('.')
#         k = [int(i) for i in r]
#         ans.add(sum(k))
# print(max(ans))
# # 842


# 14
# def fn(f):
#     s = ''
#     a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     while f != 0:
#         s += a[f % 14]
#         f //= 14
#     return s[::-1]
#
# for x in range(1, 100):
#     F = 14**300 + 14**240 + 14**170 + 14**150 - x
#     nw = fn(F)
#     if nw.count('D') == 148:
#         print(x)
#         break
# # 16


# 16
# from functools import *
# from sys import *
#
# setrecursionlimit(10**9)
#
# @lru_cache(None)
# def g(n):
#     if n < 31:
#         return 4
#     if n >= 31:
#         return (n / 2) * g(n - 2)
#
# def f(n):
#     if n >= 14:
#         return n * f(n - 1)
#     if n < 14:
#         return 8 * g(n - 3)
#
# for i in range(642000):
#     f(i)
#     g(i)
#
# print(f(320_727), g(641_452))


# 17
# f = open('Файлы для пробников/17__a5mrt.txt')
# n = [int(i) for i in f]
# mxtr = max(i for i in n if len(str(abs(i))) == 3 and i%10 == 7)
# m = mxtr**2
#
# count = 0
# ans2 = set()
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     fours = sum(1 for el in t if len(str(abs(el))) == 4)
#     negatives = sum(1 for el in t if el >= 0)
#     if negatives == 0 and fours == 0:
#         sm = abs(min(t)) + abs(max(t))
#         if sm <= m:
#             count += 1
#             ans2.add(sm)
#
# print(count, max(ans2))
# # 759 185635


# 19
# решение 1:
# def steps(p):
#     return (p - 2, p - 7, p // 3)
#
# def play(p, r):
#     if p <= 26005:
#         return r % 2 == 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(26006, 10**6):
#     if play(p, 2) and (not(play(p, 1))):
#         print(p)
# # 78019


# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a):
#     if a <= 26005:
#         return 0
#     steps = [f(a - 2), f(a - 7), f(a // 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
#
# for a in range(26006, 10**5):
#     if f(a) == -1:
#         print(a)
# # 78019


# 20
# решение 1:
# def steps(p):
#     return (p - 2, p - 7, p // 3)
#
# def play(p, r):
#     if p <= 26005:
#         return r % 2 == 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(26006, 10**6):
#     if play(p, 3) and (not(play(p, 1))):
#         print(p)
# # 78020 78021


# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a):
#     if a <= 26005:
#         return 0
#     steps = [f(a - 2), f(a - 7), f(a // 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
#
# for a in range(26006, 10**6):
#     if f(a) == 2:
#         print(a)
# # 78020 78021


# 21
# решение 1:
# def steps(p):
#     return (p - 2, p - 7, p // 3)
#
# def play(p, r):
#     if p <= 26005:
#         return r % 2 == 0
#
#     if r == 0:
#         return 0
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_plays) if r % 2 == 0 else any(next_plays)
#
# for p in range(26006, 10**6):
#     if play(p, 4) and (not(play(p, 2))):
#         print(p)
# # 78022


# решение 2:
# from functools import *
#
# @lru_cache(None)
# def f(a):
#     if a <= 26005:
#         return 0
#     steps = [f(a - 2), f(a - 7), f(a // 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
#
# for a in range(26006, 10**6):
#     if f(a) == -2:
#         print(a)
# # 78022


# 23
# решение 1:
# def f(start, end, cond1, cond2):
#     if start > end:
#         return 0
#     if start == end and cond1 == 1 and cond2 == 1:
#         return 1
#
#     if start == 26:
#         cond1 = 1
#     if start == 41:
#         cond2 = 1
#     return f(start + 3, end, cond1, cond2) + f(start ** 2, end, cond1, cond2) + f(start + 5, end, cond1, cond2)
#
# print(f(10, 52,0, 0))
# # 36


# решение 2:
# def f(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     return f(start + 3, end) + f(start ** 2, end) + f(start + 5, end)
#
# print(f(10, 26)*f(26, 41)*f(41, 52))
# # 36


# 24
# from re import *
# from string import *
# f = open("Файлы для пробников/24__a5mjz.txt")
# s = f.readline()
# glass = 'AEIOUY'
# cogl = 'BCDFGHJKLMNPQRSTVWXZ'
#
# pattern = r'0[^0123456789]+0|2[^0123456789]+2|4[^0123456789]+4|6[^0123456789]+6|8[^0123456789]+8'
# alpf = []
# for el in ascii_uppercase:
#     alpf.append(el + el)
#
# goods = []
# for i in finditer(pattern, s):
#     g = i.group(0)
#     flagalf = 0
#     gl = 0
#     cgl = 0
#     for i in range(len(g) - 1):
#         t = g[i:i+2]
#         for el in alpf:
#             if el == t:
#                 flagalf = 1
#         if g[i] in glass:
#             gl += 1
#         if g[i] in cogl:
#             cgl += 1
#
#     if flagalf == 1 and gl == cgl and len(g) == 8:
#         goods.append(g)
#
# ans = set()
# for i in range(len(s) - 7):
#     t = s[i:i+8]
#     if t in goods:
#         ans.add(i)
# print(max(ans))
# # 3613619


# 25
# def prime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
# def d(x):
#     divs = set()
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             divs.add(i)
#             divs.add(x//i)
#     s, k = 0, 0
#     for el in divs:
#         s += el
#         if prime(el):
#             k += 1
#     return s, k
#
# limit = 0
# for x in range(4_333_796, 5_000_000):
#     if x % 10 != 9:
#         s, k = d(x)
#         if (x - s - k) % 100 == 29 and (x - s - k) > 0:
#             print(x)
#             limit += 1
#     if limit == 5:
#         break
# # 4333870
# # 4334131
# # 4334545
# # 4334554
# # 4334611


# 26
# f = open("Файлы для пробников/26__a5oal.txt")
# # f = open("Файлы для пробников/test27.04.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# data.sort(key=lambda x: x[0])
# # used_boxes = [data.pop(0)]
# # for box in data:
# #     num = len(used_boxes)
# #     size = box[0]
# #     material = box[1]
# #     c_size = used_boxes[-1][0]
# #     c_material = used_boxes[-1][1]
# #
# #     if material != c_material and size - c_size >= num + 3000:
# #         used_boxes.append(box)
# #
# #
# # ans1 = len(used_boxes)
# # control = used_boxes[-2][0]
# # mt = used_boxes[-2][1]
# # for el in data:
# #     if el[0] - control >= len(used_boxes) - 1 + 3000:
# #         if mt != el[1]:
# #             pass
# # ans2 = used_boxes[-1][0]
# # print(ans1, ans2)
#
# used_boxes = []
# start_index = 0
# for el in data:
#     if el[1] == 0:
#         used_boxes.append(el)
#         break
#
# for box in data[start_index+1:]:
#     num = len(used_boxes)
#     size = box[0]
#     material = box[1]
#     c_size = used_boxes[-1][0]
#     c_material = used_boxes[-1][1]
#
#     if material != c_material and size - c_size >= num + 3000:
#         used_boxes.append(box)
#
#
# ans1 = len(used_boxes)
# control = used_boxes[-2][0]
# mt = used_boxes[-2][1]
# for el in data:
#     if el[0] - control >= len(used_boxes) - 1 + 3000:
#         if mt != el[1]:
#             pass
# ans2 = used_boxes[-1][0]
# print(ans1, ans2)
# # 2300 9996036

# 27
# A:
# from math import *
# f = open("Файлы для пробников/27_A__a5n8e.txt")
# data = []
# for s in f.readlines():
#     x, y, cl = s.split()
#     x = x.replace(',','.')
#     y = y.replace(',', '.')
#     data.append([float(x), float(y), cl])
#
# clusters = []
# n_clusters = []
# trash = []
# r = 1
# print(len(data))
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         k = i[:2]
#         for j in data[:]:
#             p = j[:2]
#             if dist(k, p) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
#
# for c in clusters:
#     if len(c) > 50:
#         n_clusters.append(c)
#         print(f'len(c): {len(c)}')
#     else:
#         trash.append(c)
#         print(f'len(trash): {len(trash)}')
#
# centers = []
# for k in range(len(n_clusters)):
#     mn = 10**10
#     for star in n_clusters[k]:
#         s = 0
#         q = star[:2]
#         for i in n_clusters[k]:
#             w = i[:2]
#             s += dist(q, w)
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#
# t = []
# for star in n_clusters[1]:
#     x, y, cl = star
#     if cl[0] == 'G' and cl[-3:] == 'III':
#         print(star, dist(star[:2], centers[1][:2]))
#         t.append(star)
# ans1 = t[-1][0]
# ans2 = t[-1][1]
# print(int(ans1*10_000), int(ans2*10_000))
# # 158409 407193
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 10
# # screensize(4000, 4000)
# #
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# #
# # up()
# # for k in range(len(n_clusters)):
# #     for i in n_clusters[k]:
# #         x, y = i[:2]
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for i in centers:
# #     x, y = i[:2]
# #     goto(x*m, y*m)
# #     dot(6, 'red')
# #
# # done()


# B:
# from math import *
# f = open("Файлы для пробников/27_B__a5n8d.txt")
# data = []
# for s in f.readlines():
#     x, y, cl = s.split()
#     x = x.replace(',','.')
#     y = y.replace(',', '.')
#     data.append([float(x), float(y), cl])
#
# clusters = []
# n_clusters = []
# trash = []
# r = 1
# print(len(data))
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         k = i[:2]
#         for j in data[:]:
#             p = j[:2]
#             if dist(k, p) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
#
# for c in clusters:
#     if len(c) > 50:
#         n_clusters.append(c)
#         print(f'len(c): {len(c)}')
#     else:
#         trash.append(c)
#         print(f'len(trash): {len(trash)}')
#
# centers = []
# for k in range(len(n_clusters)):
#     mn = 10**10
#     for star in n_clusters[k]:
#         s = 0
#         q = star[:2]
#         for i in n_clusters[k]:
#             w = i[:2]
#             s += dist(q, w)
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
#
# whites = []
# for k in range(len(n_clusters)):
#     amount = 0
#     for star in n_clusters[k]:
#         cl = star[-1]
#         if cl[0] == 'A' and cl[-1] == 'I' and len(cl) == 3:
#             amount += 1
#     whites.append(amount)
#
# ans1 = dist(centers[0][:2], centers[-1][:2])
#
# ans2 = 0
# for k in range(len(n_clusters)):
#     for star1 in n_clusters[k]:
#         cl1 = star1[-1]
#         for star2 in n_clusters[k]:
#             cl2 = star2[-1]
#             if cl1[0] == 'O' and cl2[0] == 'O':
#                 if cl1[-1] == 'V' and cl2[-1] == 'V':
#                     if len(cl1) == 3 and len(cl2) == 3:
#                         ans2 = max(ans2, dist(star1[:2], star2[:2]))
# print(int(ans1 * 10_000), int(ans2 * 10_000))
# # 59134 15419
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 10
# # screensize(4000, 4000)
# #
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# #
# # up()
# # for k in range(len(n_clusters)):
# #     for i in n_clusters[k]:
# #         x, y = i[:2]
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for i in centers:
# #     x, y = i[:2]
# #     goto(x*m, y*m)
# #     dot(6, 'red')
# #
# # done()