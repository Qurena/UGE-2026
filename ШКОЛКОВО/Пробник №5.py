"""Решение пробника №5: https://3.shkolkovo.online/my/course/7259/dz/26335"""

# 2
# print('a b c d')
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 F = ((a and b) or (b and c)) == ((a <= d) and (d <= c))
#                 if F == 1:
#                     print(a, b, c, d)
# # adcb

# 5
# def ans(N):
#     s = bin(N)[2:]
#     if N % 3 == 0 or N % 3 == 1:
#         s += s[:2]
#     else:
#         k = s.count('0')
#         l = bin(k)[2:]
#         s += l
#     return int(s ,2)
#
# for n in range(1, 100):
#     if ans(n) > 122:
#         print(n, ans(n))
#         break
# # 30

# 6
# from turtle import *
# m = 10
# tracer(0)
# lt(90)
# screensize(200*200)
#
# for _ in range(2):
#     fd(10*m)
#     rt(90)
#     fd(20*m)
#     rt(90)
# up()
# fd(3*m)
# rt(90)
# fd(5*m)
# lt(90)
# down()
# for _ in range(2):
#     fd(70*m)
#     rt(90)
#     fd(80*m)
#     rt(90)
#
# up()
# for x in range(-20, 30):
#     for y in range(-20, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 128

# 8
# t = 0
# for i in range(10000000, 99999999):
#     s = str(i)
#     if int(s[0]) % 2 == 0:
#         if int(s[2]) % 2 == 0 and int(s[4]) % 2 == 0 and int(s[6]) % 2 == 0 and int(s[1]) % 2 == 1 and int(s[3]) % 2 == 1 and int(s[5]) % 2 == 1 and int(s[7]) % 2 == 1:
#             t += 1
#
#     else:
#         if int(s[2]) % 2 == 1 and int(s[4]) % 2 == 1 and int(s[6]) % 2 == 1 and int(s[1]) % 2 == 0 and int(s[3]) % 2 == 0 and int(s[5]) % 2 == 0 and int(s[7]) % 2 == 0:
#             t += 1
#
# print(t)
# # 703125

# 12
# a = {
#     'q0.':['.','L','q1'],
#     'q1.':['.','S','q1'],
#
#     'q11':['0','S','q1'],
#
#     'q10':['1','L','q1']
#
# }
#
# s1 = '0'*342 + '1' + '0'*(1000-1-342)
# s = list('..'+s1+'..')
# i = -2
# c = 0
# p = 'q0'
#
# while c != 'S':
#     s[i], c, p = a[p+s[i]]
#     i -= 1
# print(''.join(s).count('0'))
# # 999

# 13
# from ipaddress import *
# net = ip_network('205.182.128.0/255.255.192.0')
# ans = 0
#
# for ip in net:
#     i = str(ip).split('.')
#     h = bin(int(i[2]))[2:]
#     if h.count('1') == h.count('0'):
#         ans += 1
# print(ans)
# # 5120

# 14
# a = '0123456789ABCDEFGHIJKL'
# for x in a:
#     f = int(f'98{x}79641', 22) + int(f'25{x}49', 22) + int(f'63{x}5', 22)
#     if f % 21 == 0:
#         print(f//21)
#         break
# # 1112804491

# 16
# from functools import lru_cache
# from sys import setrecursionlimit
# setrecursionlimit(10**6)
# @lru_cache(None)
# def f(n):
#     if n < 3:
#         return n
#     else:
#         return (n-1)*f(n-2)
# print((f(2024) - f(2022))/f(2020))
# # 4086462

# 17
# f = open("Файлы для пробников/17__1w6mz.txt")
# s1 = f.readlines()
# s = []
# for el in s1:
#     s.append(int(el))
#
# t = 0
# mn = 10 ** 10
# for i in range(len(s) - 1):
#     for j in range(i+1, len(s)):
#         if (((s[i] + s[j]) % 18 == 0) and ((s[i] * s[j]) % 18 != 0)) or (((s[i] + s[j]) % 18 != 0) and ((s[i] * s[j]) % 18 == 0)):
#             t += 1
#             mn = min(mn, s[i] * s[j])
# print(t, mn)
# # 118094 270

# 19
# # 1 вариант решения
# from functools import lru_cache
# @lru_cache(None)
# def f(a):
#     if a >= 80:
#         return 0
#
#     t = [f(a+2), f(a+3), f(a*2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 80):
#     if f(s) != 1 and f(s) == -1:
#         print(s)
# # 38
# print('     ')
# # 2 вариант решения
# def steps(p):
#     return p+2, p+3, p*2
#
# def play(p, r):
#     if p >= 80 and (r == 0 or r == 2):
#         return True
#
#     if p >= 80 and (r == 1 or r == 3):
#         return False
#
#     if r == 0:
#         return False
#
#     next_plays = []
#     for step in steps(p):
#         next_plays.append(play(step, r - 1))
#
#     if r - 1 == 1:
#         return all(next_plays)
#
#     if r - 1 == 0:
#         return any(next_plays)
#
# for s in range(1, 80):
#     if play(s, 2):
#         print(s)
# # 38

# 20
# # 1 вариант решения
# from functools import lru_cache
# @lru_cache(None)
# def f(a):
#     if a >= 80:
#         return 0
#
#     t = [f(a+2), f(a+3), f(a*2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 80):
#     if f(s) != 1 and f(s) == 2:
#         print(s)
# # 19 35
# print('     ')
# # 2 вариант решения
# def steps(p):
#     return p+2, p+3, p*2
#
# def play(p, r):
#     if p >= 80 and (r == 0 or r == 2):
#         return True
#
#     if p >= 80 and (r == 1 or r == 3):
#         return False
#
#     if r == 0:
#         return False
#
#     next_plays = []
#     for step in steps(p):
#         next_plays.append(play(step, r - 1))
#
#     if r - 1 == 2:
#         return any(next_plays)
#
#     if r - 1 == 1:
#         return all(next_plays)
#
#     if r - 1 == 0:
#         return any(next_plays)
#
# for s in range(1, 80):
#     if not play(s, 1) and play(s, 3):
#         print(s)
# # 19 35

# 21
# # 1 вариант решения
# from functools import lru_cache
# @lru_cache(None)
# def f(a):
#     if a >= 80:
#         return 0
#
#     t = [f(a+2), f(a+3), f(a*2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 80):
#     if f(s) == -2:
#         print(s)
# # 34
#
# print('     ')
#
# # 2 вариант решения
# def steps(p):
#     return p+2, p+3, p*2
#
# def play(p, r):
#     if p >= 80 and (r % 2 == 0):
#         return True
#
#     if p >= 80 and (r % 2 != 0):
#         return False
#
#     if r == 0:
#         return False
#
#     next_plays = []
#     for step in steps(p):
#         next_plays.append(play(step, r - 1))
#
#     if r - 1 == 3:
#         return all(next_plays)
#
#     if r - 1 == 2:
#         return any(next_plays)
#
#     if r - 1 == 1:
#         return all(next_plays)
#
#     if r - 1 == 0:
#         return any(next_plays)
#
# for s in range(1, 80):
#     if (not play(s, 2)) and play(s, 4):
#         print(s)
# # 34

# 23
# def f(start: int, end: int) -> int:
#     d = {}
#
#     for i in range(start ,end + 1):
#         d[i] = 0
#
#     d[start] = 1
#
#     if 15 in d:
#         del d[15]
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
# print(f(1, 11)*f(11, 25))
# # 46

# 24
# from re import *
# f = open("Файлы для пробников/24__7h51q.txt")
# s = f.readline()
#
# pattern = r'A([1-6]+([-*][1-6]+)+)'
# mx = 0
# for i in finditer(pattern, s):
#     t = i.group()
#     mx = max(mx, len(t))
# print(mx)
# # 85

# 25
# def d(x:int) -> list[int]:
#     divs = []
#     for div in range(2, int(x**0.5)+1):
#         if x % div == 0:
#             divs.append(div)
#             if x//div != x:
#                 divs.append(x//div)
#     return sorted(divs)
#
# def is_prime(x:int) -> bool:
#     divs = []
#     for div in range(2, int(x ** 0.5) + 1):
#         if x % div == 0:
#             divs.append(div)
#             if x // div != x:
#                 divs.append(x // div)
#     if divs == []:
#         return True
#     else:
#         return False
#
# t = 0
# mn = 10**10
# for x in range(268_312, 336_493):
#     if len(d(x)) == 2:
#         if is_prime(d(x)[0]) and is_prime((d(x))[1]):
#             t += 1
#             mn = min(mn, x)
# print(t, mn)
# # 14389 268313

# 27
# Для файла A:
# from math import dist
# f = open("Файлы для пробников/27_5_A__51ud2.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
# r = 2.1
#
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# px = py = 0
# for i in clusters:
#     mn = 10**10
#     for star in i:
#         s = 0
#         for j in i:
#             s += dist(star, j)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
# print(int(px*525), int(py*525))
# # -221 1917

# Для файла B:
# from math import *
# # from turtle import *
# # tracer(0)
# # m = 15
# # up()
#
# f = open("Файлы для пробников/27_5_B__51ud4.txt")
# a = [list(map(float, i.replace(",", ".").split())) for i in f if "X" not in i]
# clusters = []
# r = 2.1
#
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 # x, y = i
#                 # goto(x*m, y*m)
#                 # dot(3, 'blue')
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# # for t in range(1):
# #     for i in clusters[t]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# px = py = 0
# for i in clusters:
#     mn = 10**10
#     for star in i:
#         s = 0
#         for j in i:
#             s += dist(star, j)
#             if s < mn:
#                 mn = s
#                 mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
# print(int((px/2)*300), int((py/2)*300))
# # 587 740