"""https://3.shkolkovo.online/my/course/7259/dz/30731"""

# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = w and (z == (x <= y))
#                 print(x, y, w, z, int(F))
# # zwxy


# 5
# from math import *
#
# ans = set()
# for n in range(10001):
#     k = [int(i) for i in str(n)]
#     p = prod(k)
#     s = max(k) - min(k)
#     t1 = p + s
#     t2 = p * s + 1
#     if t1 >= t2:
#         r = int(str(t2) + str(t1))
#     else:
#         r = int(str(t1) + str(t2))
#     if r == 25127:
#         ans.add(n)
# print(max(ans))
# # 92


# 6
# from turtle import *
# tracer(0)
# lt(90)
# m = 15
# screensize(2000*2000)
#
# for _ in range(2):
#     fd(7*m)
#     lt(270)
#     back(5*m)
#     rt(90)
# up()
# fd(6*m)
# rt(90)
# back(4*m)
# lt(90)
# down()
# for _ in range(2):
#     fd(9*m)
#     rt(90)
#     fd(4*m)
#     rt(90)
# up()
# fd(4*m)
# rt(180)
# back(2*m)
# down()
# for _ in range(2):
#     fd(7*m)
#     rt(90)
#     fd(7*m)
#     rt(90)
# up()
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 114


# 8
# def tw(n):
#     s = ''
#     a = '0123456789AB'
#     while n != 0:
#         s += a[n % 12]
#         n //= 12
#     return s[::-1]
#
# ans = 0
# for n in range(1, 1_000_000):
#     t = tw(n)
#     if len(t) == 5:
#         odd = sum(1 for i in t if i in '13579B')
#         if odd == 3:
#             good = ['111', '333', '555', '777', '999', 'BBB']
#             for k in good:
#                 if k in t:
#                     ans += 1
# print(ans)


# ans = 0
# for n in range(10000, 100000):
#     s = tw(n)
#     odd = sum(1 for i in s if i in '13579B')
#     if odd == 3:
#         good = ['111', '333', '555', '777', '999', 'BBB']
#         for k in good:
#             if k in s:
#                 ans += 1
# print(ans)
# 262


# 12
# a = {
#     'q0.': ['.','R','q1'],
#     'q1.': ['.', 'S', 'q1'],
#     'q13': ['7', 'R', 'q1'],
#     'q16': ['8', 'R', 'q1'],
#     'q19': ['3', 'R', 'q1']
# }
# s1 = '963'
# s = list('..'+s1+'..')
# i = 1
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i += 1
# print(''.join(s))
# # 133164


# 14
# def ft(n):
#     s = ''
#     a = '0123456789ABCDE'
#     while n != 0:
#         s += a[n % 15]
#         n //= 15
#     return s[::-1]
#
# ans = set()
# for x in range(1, 2000):
#     g = 11*15**13 + 14*15**8 - x
#     ng = ft(g)
#     if ng.count('0') % 2 != 0:
#         ans.add(x)
# print(max(ans))
# # 1995


# 15
# def f(x, a):
#     return ((x % a == 0) or ((140 <= x <= 230) <= ((x % 41 != 0) or (x + a <= 306))))
#
# for a in range(1, 305):
#     t = [f(x, a) for x in range(1, 305)]
#     if all(t):
#         print(a)
# # 101


# 16
# from sys import *
# setrecursionlimit(10**9)
#
# def g(n):
#     if n > 19999:
#         return n**2
#     if n < 20000:
#         return 20 + n + g(n + 4)
#
# def f(n):
#     if n > 19999:
#         return n + f(n - 6)
#     if n < 20000:
#         return n + g(n - 3)
#
# print(f(65000))
# # 718992548


# 17
# f = open("Файлы для пробников/17__9jc1d.txt")
# n = [int(i) for i in f.readlines()]
#
# m77 = min(i for i in n if i > 0 and abs(i) % 100 == 77)
#
# count = 0
# ms = set()
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     tr = sum(1 for el in t if len(str(abs(el))) == 3)
#     if tr <= 1 and sum(t) >= m77:
#         count += 1
#         ms.add(sum(t))
#
# print(count, min(ms))
# # 2414 280

# Ситуация на any-any
# 19
# from math import *
#
# def steps(p):
#     h1, h2 = p
#     return (h1, h2 + 5), (h1, h2 + 19), (h1 + 5, h2), (h1 + 19, h2)
#
# def play(p, r):
#     if prod(p) >= 450:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else any(next_steps)
#
# ans = 0
# for s in range(1, 90):
#     p = (5, s)
#     if not(play(p, 1)) and play(p, 2):
#         ans += 1
# print(ans)
# # 18


# 20
# from math import *
# def steps(p):
#     h1, h2 = p
#     return (h1, h2 + 5), (h1, h2 + 19), (h1 + 5, h2), (h1 + 19, h2)
#
# def play(p, r):
#     if prod(p) >= 450:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_steps) if r % 2 != 0 else any(next_steps)
#
# for s in range(1, 90):
#     p = (5, s)
#     if play(p, 4) and not(play(p, 2)): # play(s, 4) включает в себя решение play(s, 2)
#         print(s)



# 21
# как это решить кодом...


# 23
# def change(n):
#     if int(str(n)[1]) < int(str(n)[0]):
#             r = int(str(n)[1] + str(n)[0])
#             return r
#     return None
#
# def f(start, end):
#     d = {}
#
#     for i in range(start, end - 1, -1):
#         d[i] = 0
#
#     d[start] = 1
#
#     for key in d.keys():
#         if key - 3 in d:
#             d[key - 3] += d[key]
#         if change(key) in d:
#             d[change(key)] += d[key]
#     return d[end]
#
# print(f(43, 13))
# # 4


# 24
# f = open("Файлы для пробников/24__9jc3z.txt")
# s = f.readline()
# c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = cl = start = mx = 0
# # from string import *
# # print(ascii_uppercase)
# for end in range(len(s)):
#     if s[end] == '0':
#         c0 += 1
#     if s[end] == '1':
#         c1 += 1
#     if s[end] == '2':
#         c2 += 1
#     if s[end] == '3':
#         c3 += 1
#     if s[end] == '4':
#         c4 += 1
#     if s[end] == '5':
#         c5 += 1
#     if s[end] == '6':
#         c6 += 1
#     if s[end] == '7':
#         c7 += 1
#     if s[end] == '8':
#         c8 += 1
#     if s[end] == '9':
#         c9 += 1
#     if s[end] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         cl += 1
#     while cl > 0:
#         if s[start] == '0':
#             c0 -= 1
#         if s[start] == '1':
#             c1 -= 1
#         if s[start] == '2':
#             c2 -= 1
#         if s[start] == '3':
#             c3 -= 1
#         if s[start] == '4':
#             c4 -= 1
#         if s[start] == '5':
#             c5 -= 1
#         if s[start] == '6':
#             c6 -= 1
#         if s[start] == '7':
#             c7 -= 1
#         if s[start] == '8':
#             c8 -= 1
#         if s[start] == '9':
#             c9 -= 1
#         if s[start] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             cl -= 1
#         start += 1
#     if cl == 0 and c0 > 0 and c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0 and c6 > 0 and c7 > 0 and c8 > 0 and c9 > 0:
#         mx = max(mx, end - start + 1)
# print(mx)
# # 119


# 25
# def prime(x):
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
# def good_div(div):
#     s3 = sum(1 for i in str(div) if int(i) == 3)
#     s7 = sum(1 for i in str(div) if int(i) == 7)
#     if s3 + s7 == 0:
#         return False
#     return True
#
# def div(x):
#     divs = set()
#     for i in range(1, int(x**0.5) + 1):
#         if x % i == 0:
#             if good_div(i) and prime(i):
#                 divs.add(i)
#             if good_div(x//i) and prime(x//i):
#                 divs.add(x//i)
#     return divs
#
# current = set()
# for n in range(5_000_001, 5_100_000):
#     if len(current) == 5:
#         print(*current)
#         break
#     if div(n):
#         divs = div(n)
#         for el1 in divs:
#             for el2 in divs:
#                 for el3 in divs:
#                     if el1*el2*el3 == n:
#                         current.add(n)
# # 5000001 5000003 5000007 5000013 5000019


# 26
# f = open("Файлы для пробников/26__9jeu3.txt")
# # f = open("Файлы для пробников/test_26_24i195i23u932.txt")
# n = int(f.readline())
# camps = [[int(i)] for i in f.readlines()]
# camps.sort(reverse=True)
#
# for k in range(len(camps)-1):
#     safe = 12
#     deep = 0
#     for i in range(k, len(camps)-1):
#         if (38 < camps[i][0] - camps[i + 1][0] <= 70 and safe <= 0) or camps[i][0] - camps[i + 1][0] > 70:
#             break
#         if camps[i][0] - camps[i + 1][0] <= 38:
#             deep += 1
#         if 38 < camps[i][0] - camps[i + 1][0] <= 70 and safe > 0:
#             deep += 1
#             safe -= 1
#     camps[k].append(deep+1)
#
# ans1 = 0
# ans2 = 0
# mx = 0
# for i in range(n-1):
#     if camps[i][1] > mx:
#         mx = camps[i][1]
#         ans1 = camps[i][1]
#         ans2 = camps[i + camps[i][1] - 1][0]
# print(ans1, ans2)
# # 1519 59477


# 27
# Файл A:
# from math import *
#
# f = open("Файлы для пробников/27_A__9jfiw.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
# r = 0.9
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# for c in clusters:
#     if len(c) < 50:
#         clusters.remove(c)
#
# # from turtle import *
# # tracer(0)
# # lt(90)
# # m = 15
# # screensize(2000*2000)
# #
# # up()
# # for k in range(len(clusters)):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m , y*m)
# #         dot(3, 'blue')
# # done()
#
# mxd = s1 = s2 = 0
# for star1 in clusters[0]:
#     for star2 in clusters[1]:
#         if dist(star1, star2) > mxd:
#             mxd = dist(star1, star2)
#             s1 = star1
#             s2 = star2
# px = s1[0] + s2[0]
# py = abs(s1[1] - s2[1])
# print(int(abs(px*1000)), int(py*1000))
# # 6019 14475


# Файл B:
# from math import *
#
# f = open("Файлы для пробников/27_B__9jfix.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
# r = 0.3
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) <= r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# cl = []
# for c in clusters:
#     if len(c) > 100:
#         cl.append(c)
#
# # from turtle import *
# # tracer(0)
# # lt(90)
# # m = 5
# # screensize(2000*2000)
# #
# # up()
# # for k in range(len(cl)):
# #     for i in cl[k]:
# #         x, y = i
# #         goto(x*m , y*m)
# #         dot(3, 'blue')
# # done()
#
# stars = []
# mxd1 = s1_1 = s1_2 = 0
# for star1 in cl[0]:
#     for star2 in cl[1]:
#         if dist(star1, star2) > mxd1:
#             mxd1 = dist(star1, star2)
#             s1_1 = star1
#             s1_2 = star2
#
# mxd2 = s2_1 = s2_2 = 0
# for star1 in cl[0]:
#     for star2 in cl[2]:
#         if dist(star1, star2) > mxd2:
#             mxd2 = dist(star1, star2)
#             s2_1 = star1
#             s2_2 = star2
#
# mxd3 = s3_1 = s3_2 = 0
# for star1 in cl[1]:
#     for star2 in cl[2]:
#         if dist(star1, star2) > mxd3:
#             mxd3 = dist(star1, star2)
#             s3_1 = star1
#             s3_2 = star2
#
# q1 = mxd1 + mxd2 + mxd3
# stars.append(s1_1)
# stars.append(s1_2)
# stars.append(s2_1)
# stars.append(s2_2)
# stars.append(s3_1)
# stars.append(s3_2)
#
# q2 = 0
# for star in stars:
#     q2 = max(q2, dist(star, [2.0, 2.0]))
# print(int(q1*100), int(q2*100))
# # 7140 2159