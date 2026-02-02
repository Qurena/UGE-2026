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



