'''https://3.shkolkovo.online/my/course/7259/dz/30092'''


# 2
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x == (not(y))) <= (z == (y or w))
#                 if F == 0 and z == 0:
#                     print(x, y, z, w, int(F))
# # zwyx


# 5
# def inv(r):
#     q = str(r)[::-1]
#     j = -1
#     for d in q:
#         if d == '1':
#             break
#         j -= 1
#     invert = r[:j]
#     invert = invert.replace('1', '*')
#     invert = invert.replace('0', '1')
#     invert = invert.replace('*', '0')
#     return invert + r[j:]
#
#
# for n in range(1, 256):
#     r = bin(n)[2:].zfill(8)
#     if int(inv(r), 2) == 98:
#         print(n)
# # 158


# 6
# from turtle import *
# m = 10
# lt(90)
# screensize(2000*2000)
#
# for _ in range(10):
#     fd(15*m)
#     rt(60)
# done()
# # 6


# 8
# from itertools import *
# s = 'МОРС'
#
# num = 0
# for i in product(s, repeat=5):
#     num += 1
#     g = ''.join(i)
#     if g.count('М') == 1 and g.count('Р') == 2:
#         print(g, num)
# # 1001


# 12
# a = {
#     'q0.': ['.','S','q0'],
#     'q00': ['0', 'L', 'q1'],
#     'q01': ['1', 'L', 'q0'],
#     'q1.': ['.','S','q1'],
#     'q10': ['0', 'L', 'q1'],
#     'q11': ['0', 'L', 'q0']
# }
#
# s1 = '101101'
# s = list('..'+s1+'..')
# i = -3
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(int('001001', 2))
# # 9


# 14
# from sys import *
# set_int_max_str_digits(10**10)
#
# def egg(n):
#     s = ''
#     while n != 0:
#         s += str(n % 8)
#         n //= 8
#     return s[::-1]
#
# q = 8**30_000 + 3 * (8**20_000)
# mx7 = 0
# for x in range(1000, 2000):
#     f = q - x
#     g = egg(f).count('7')
#     if g > mx7:
#         mx7 = g
# print(mx7)
# SyntaxError: Exceeds the limit (4300 digits) for integer string conversion: value has 18063 digits; use sys.set_int_max_str_digits() to increase the limit - Consider hexadecimal for huge integer literals to avoid decimal conversion limits.


# 15
# def f(a, x):
#     return ((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 90)
#
# for a in range(1, 90):
#     if all(f(a, x) for x in range(1, 90)):
#         print(a)
#         break
# # 75


# 16
# from sys import *
# setrecursionlimit(10**9)
# def g(n):
#     if n < 7:
#         return n**5
#     return g(n - 4) + 1
#
# def f(n):
#     return g(n - 20_000) + 10_000
#
# print(f(30_000))
# # 13523


# 17
# f = open("Файлы для пробников/17_21__8hqq3.txt")
# n = [int(i) for i in f.readlines()]
#
# def sumdig(x):
#     s = 0
#     for i in str(abs(x)):
#         s += int(i)
#     return s
#
#
# ans1 = 0
# mn = 10**10
# for i in range(len(n) - 6):
#     t = n[i:i+7]
#     even = sum(1 for el in t if sumdig(el) % 2 == 0)
#     odd = sum(1 for el in t if sumdig(el) % 2 != 0)
#     if even > odd and sum(t) % 5 == 0:
#         ans1 += 1
#         mn = min(mn, sum(t))
# print(ans1, abs(mn))
# # 3004 23220


# 19
# def steps(p):
#     h1, h2 = p
#     return (h1+2, h2), (h1*3, h2), (h1, h2+2), (h1, h2*3)
#
# def play(p, r):
#     if sum(p) >= 50:
#         return r == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else any(next_plays)
#
# ans = 0
# for s in range(1, 40):
#     for q in range(1, 40):
#         p = (s, q)
#         if play(p, 2) and (not(play(p, 1))):
#             ans += 1
# print(ans)
# # 164


# 20
# def steps(p):
#     h1, h2 = p
#     return (h1+2, h2), (h1*3, h2), (h1, h2+2), (h1, h2*3)
#
# def play(p, r):
#     if sum(p) >= 50:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
#
# for s in range(1, 40):
#     p = (s, 10)
#     if play(p, 3) and not(play(p, 1)):
#         print(s)
# # 11 12


# 21
# def steps(p):
#     h1, h2 = p
#     return (h1+2, h2), (h1*3, h2), (h1, h2+2), (h1, h2*3)
#
# def play(p, r):
#     if sum(p) >= 50:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else all(next_plays)
#
# ans = 0
# for s in range(1, 40):
#     for q in range(1, 40):
#         p = (s, q)
#         if play(p, 6) and not(play(p, 2)) and not(play(p, 4)):
#             ans += 1
# print(ans)
# # 19


# 23
# def count(start, end, evens):
#     if start == end and evens <= 4:
#         return 1
#
#     if start > end:
#         return 0
#
#     if start % 2 == 0:
#         return count(start + 1, end, evens) + count(start * 2, end, evens + 1)
#
#     if start % 2 != 0:
#         return count(start + 1, end, evens + 1) + count(start * 2, end, evens + 1)
#
#
# print(count(1, 19, 0))
# # 6


# 24
f = open("Файлы для пробников/24_13715__3kjzr.txt")
s = f.readline()
s = s.replace('CD', '*&')
mx = c = start = 0
for end in range(len(s)):
    if s[end:end+2] == '*&':
        c += 1
    while c > 50:
        if s[start:start + 2] == '*&':
            c -= 1
        start -= 1
    if c == 50:
        mx = max(mx, end - start + 1)
print(mx)
# 27911


# 25
# from fnmatch import *
#
# def div(x):
#     divs = set()
#     for i in range(1, int(x**0.5)+1):
#         if x % i == 0:
#             divs.add(i)
#             divs.add(x//i)
#     return divs
#
# def f(x):
#     ndivs = set()
#     for el in div(x):
#         if fnmatch(str(el), '1*4'):
#             ndivs.add(el)
#     return ndivs
#
# for x in range(0, 10**7 + 1, 2048):
#     if x != 0:
#         if fnmatch(str(x), '2*56??'):
#             if len(f(x)) > 5:
#                 print(x, x//2048)
# # 2715648 1326


# 26
# f = open("Файлы для пробников/26_2__3whrz.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# l_start = []
# l_end = []
# num = -1
# for d in data:
#     num += 1
#     d.append(num)
#
# data.sort(key=lambda x: (x[0], x[1]))
#
# current = []
# for detail in data:
#     sh = detail[0]
#     pt = detail[1]
#     if sh not in current and pt not in current:
#         if sh > pt:
#             l_start.append([sh, detail[2]])
#             current.append(sh)
#             current.append(pt)
#         if pt > sh:
#             l_end.append([pt, detail[2]])
#             current.append(sh)
#             current.append(pt)
#     else:
#         print('Error')
# l_start.sort()
# l_end.sort(reverse=True)
# print(len(l_end), l_end[0][-1])
# # 277 87


# 27
# Файл A:
# from math import *
# f = open("Файлы для пробников/4A__58wvv.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f.readlines() if 'X' not in i]
# clusters = []
# nclusters = []
# r = 0.9
#
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
#
# for cl in clusters:
#     if len(cl) > 100:
#         nclusters.append(cl)
#
# # from turtle import *
# # tracer(60)
# # m = 10
# # lt(90)
# # screensize(2000*2000)
# # up()
# # for k in range(len(nclusters)):
# #     for i in nclusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'green')
# # done()
#
# px, py = 0, 0
# for k in range(len(nclusters)):
#     mn = 10**10
#     for star in nclusters[k]:
#         s = 0
#         for i in nclusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
#
# print(int(abs(px/len(nclusters))*100), int(abs(py/len(nclusters))*100))
# # 195 105

# Файл B:
# from math import *
# f = open("Файлы для пробников/4B__58wvw.txt")
# data = [list(map(float, i.replace(',','.').split())) for i in f.readlines() if 'X' not in i]
# clusters = []
# nclusters = []
# r = 0.9
#
# while data:
#     clusters.append([data.pop(0)])
#     for i in clusters[-1]:
#         for j in data[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 data.remove(j)
#
# for cl in clusters:
#     if len(cl) > 100:
#         nclusters.append(cl)
#
# # from turtle import *
# # tracer(0)
# # m = 10
# # lt(90)
# # screensize(2000*2000)
# # up()
# # for k in range(len(nclusters)):
# #     for i in nclusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'green')
# # done()
#
# px, py = 0, 0
# for k in range(len(nclusters)):
#     mn = 10**10
#     for star in nclusters[k]:
#         s = 0
#         for i in nclusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
#
# print(int(abs(px/len(nclusters))*100), int(abs(py/len(nclusters))*100))
# # 276 263