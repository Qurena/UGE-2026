"""Решение пробника №7: https://3.shkolkovo.online/my/course/7259/dz/27120"""

# 2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (not(x <= (y == w))) or (z <= (x == y))
#                 if F == 0:
#                     print(x, y, z, w)
# # wxzy


# 5
# def sev(n: int) -> str: # знаю, что так не нужно, но мне так удобнее)))
#     s = ''
#     while n != 0:
#         s += str(n % 7)
#         n //=7
#     return s[::-1]
#
# def ans(n: int) -> int:
#     s = sev(n)
#     s = str(n % 5) + s
#     s += str(n % 3)
#     return int(s, 7)
#
# for n in range(1, 10000):
#     if len(str(ans(n))) == 3:
#         print(ans(n), n)
# # 982


# 6
# from turtle import *
# tracer(0)
# m = 20
# screensize(200*200)
#
# for _ in range(10):
#     for _ in range(3):
#         fd(3*m)
#         rt(90)
#         fd(3*m)
#         rt(270)
#     rt(90)
# up()
#
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*m, y*m)
#         dot(3, 'purple')
# done()
# # 216


# 8
# from itertools import *
#
# p = 'КАНУЛ'
# sogl = 'КНЛ'
# count = 0
#
# for t in product(p, repeat=5):
#     s = ''.join(t)
#     if s.count('У') == 1 and s.index('У') != 0:
#         k = s.index('У')
#         if s[k-1] in sogl:
#             count += 1
# print(count)
# # 768


# 12
# a = {
#     'q0.': ['.', 'S', 'q0'],
#     'q00': ['0', 'R', 'q0'],
#     'q01': ['1', 'L', 'q1'],
#     'q1.': ['.', 'R', 'q2'],
#     'q10': ['1', 'R', 'q2'],
#     'q11': ['1', 'R', 'q2'],
#     'q2.': ['.', 'R', 'q0'],
#     'q20': ['0', 'R', 'q0'],
#     'q21': ['1', 'R', 'q0']
# }
#
# s1 = '0001010101'
# s = list('..' + s1 + '..')
# i = 2
# c = 0
# p = 'q0'
#
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     if c == 'R':
#         i += 1
#     if c == 'L':
#         i -= 1
# print(''.join(s))
# # 230


# 13
# from ipaddress import *
#
# net = ip_network('42.54.160.28/255.255.255.252', 0)
# count = 0
#
# for t in net:
#     s = bin(int(t))[2:].zfill(32)
#     if '1111' not in s:
#         count += 1
# print(count)
# # 2


# 14
# for x in range(1, 47):
#     f1 = 1 * (47**4) + x * (47**3) + 2 * (47**2) + 4 * (47**1) + 10 * (47**0)
#     f2 = x * (47**4) + 2 * (47**3) + 0 * (47**2) + 2 * (47**1) + 4 * (47**0)
#     f3 = 6 * (47**3) + x * (47**2) + 0 * (47**1) + 8 * (47**0)
#     F = f1 + f2 - f3
#     if F % 46 == 0:
#         print(x, F)
# # 178814420


# 16
# from sys import *
# setrecursionlimit(10**6)
# def f(n):
#     if n <= 2:
#         return 1
#     return (5 * n + 8) * f(n - 2)
# print(f(6532)/f(6530))
# # 32668


# 17
# f = open("Файлы для пробников/17_7__89i1k.txt")
# a = [int(i) for i in f]
# mn = 10**10
# count = 0
# def sdig(n: int) -> int:
#     s = 0
#     n = abs(n)
#     while n != 0:
#         s += n % 10
#         n //= 10
#     return s
#
# for i in range(len(a) - 2):
#     t = [a[i], a[i+1], a[i+2]]
#     if sum(t) % 11 == 0:
#         f = 0
#         for el in t:
#             if sdig(el) % 2 != 0:
#                 mn = min(sum(t), mn)
#                 f += 1
#         if f == 3:
#             count += 1
#         f == 0
#
# print(count, mn)
# # 109 -25883


# 19-21
# | вариант решения
from functools import *
@lru_cache(None)
def f(a, b):
    if a + b >= 78:
        return 0
    t = [f(a + 3, b), f(a, b + 3), f(a * 2, b), f(a, b * 2)]
    n = [int(i) for i in t if i <= 0]
    if n:
        return -max(n) + 1
    return -max(t)

for s in range(1, 71):
    # В данной позиции после неудачного хода Пети возможен выигрыш Вани
    if f(7+3,s) == 1 or f(7,s+3) == 1 or f(7*2,s) == 1 or f(7,s*2) == 1:
        print(s)
# 18

# for s in range(1, 71):
#     if f(7, s) == 2:
#         print(s)
# # 17

# for s in range(1, 71):
#     if (f(7, s) == -1 or f(7, s) == -2) and (f(7, s) != -1): # f(7, s) == -2
#         print(s)
# # 2830



# || вариант решения
# def step(p):
#     a, b = p
#     return [(a + 3, b), (a, b + 3), (a * 2, b), (a, b * 2)]
#
# def play(p, r):
#     if sum(p) >= 78:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(steep, r - 1) for steep in step(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# # for s in range(1, 71):
# #     p = (7, s)
# #     if play(p, 2):
# #         print(s)
# # # 34
#
# # for s in range(1, 71):
# #     p = (7, s)
# #     if not(play(p, 1)) and play(p, 3):
# #         print(s)
# # # 17
#
# # for s in range(1, 71):
# #     p = (7, s)
# #     if (play(p, 2) or play(p, 4)) and not(play(p, 2)):
# #         print(s)
# # # 2830


# 23
# def f(start, end):
#     d = {}
#     for i in range(start, end + 1):
#         d[i] = 0
#
#     d[start] = 1
#
#     if 33 in d:
#         del d[33]
#
#     for key in d.keys():
#         if key + 2 in d:
#             d[key + 2] += d[key]
#         if key + 3 in d:
#             d[key + 3] += d[key]
#         if key * 4 in d:
#             d[key * 4] += d[key]
#     return d[end]
#
# count = 0
# for s in range(50, 61):
#     count += f(12, s)
# print(count)
# # 686306


# 24
# f = open("Файлы для пробников/24__7h7cq.txt")
# s = f.readline()
#
# ca = cb = start = mx = 0
# for end in range(len(s)):
#     if s[end] == 'B':
#         cb += 1
#     if s[end] == 'A':
#         ca += 1
#     while ca > 1:
#         if s[start] == 'B':
#             cb -= 1
#         if s[start] == 'A':
#             ca -= 1
#         start += 1
#
#     if cb == 1 and ca == 1:
#         mx = max(mx, end - start + 1)
# print(mx)
# # 182


# 25
# from fnmatch import *
# mask = '3*4?50'
# count = 0
# for x in range(1, 10**7 + 1):
#     if fnmatch(str(x), mask):
#         count += 1
# print(count)
# # 1110


# 26
# f = open("Файлы для пробников/26__1uxcb.txt")
# n = int(f.readline())
# box = [int(i) for i in f]
#
# box = sorted(box, reverse=True)
# gb = [box[0]]
# for i in range(n):
#     for k in range(n):
#         if gb[-1] - box[k] >= 3:
#             gb.append(box[k])
#             break
# print(len(gb), gb[-1])
# # 2787 51


# 27
# from math import *
# f = open('5_A__5vo3z.txt')
# a = [list(map(float, i.replace(",", ".").split())) for i in f if "X" not in i]
# clusters = []
# r = 0.5
#
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# print(clusters, len(clusters))
#
# # Почему DBSCAN не сработал?


