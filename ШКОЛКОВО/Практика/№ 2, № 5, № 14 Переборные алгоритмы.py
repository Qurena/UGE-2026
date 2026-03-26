"""ДЗ к вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/37106"""

# 1
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (x and y) and (x and (z <= w))
#                 if F == 1:
#                     print(x, y, z, w)
# # wzyx


# 2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (((not(w)) or y) == (x and (not(z)))) <= (y and x)
#                 if F == 0:
#                     print(x, y, z, w)
# # ywxz


# 3
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (y <= w) and ( (w <= x) == (z <= w))
#                 if F == 1:
#                     print(x, y, z, w)
# # zxwy


# 4
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((not(y)) and x) <= (w and (not(z)))
#                 if F == 0:
#                     print(x, y, z, w)
# # xzwy


# 5
# for n in range(1, 10000):
#     s = bin(n)[2:]
#     if n % 2 != 0:
#         s = '0' + s + '1'
#     else:
#         s += bin(s.count('1'))[2:]
#     r = int(s, 2)
#     if r == 603:
#         print(n)
# # 301


# 6
# mn = set()
# for n in range(1, 10000):
#     s = bin(n)[2:]
#     if n % 4 == 0:
#         s += s[-2:]
#     else:
#         s += bin((n % 4)*3)[2:]
#     r = int(s, 2)
#     if r > 76:
#         mn.add(r)
# print(min(mn))
# # 80


# 7
# mx = set()
# for n in range(1, 100000):
#     s = bin(n)[2:]
#     if n % 3 == 0:
#         f = s[0]
#         e = s[-1]
#         s += f + e
#     else:
#         f = s[0]
#         e = s[-1]
#         s = e + f + s
#     r = int(s, 2)
#     if r < 500:
#         mx.add(n)
# print(max(mx))
# # 242


# 8
# def f(n):
#     s = ''
#     a = '012'
#     while n != 0:
#         s += a[n % 3]
#         n //= 3
#     return s[::-1]
#
# mn = set()
# for n in range(1, 10000):
#     s = f(n)
#     k = s.count('1') + s.count('2')
#     if k % 2 == 0:
#         s += '0'
#     else:
#         s += '1'
#     k = s.count('1') + s.count('2')
#     if k % 2 == 0:
#         s += '0'
#     else:
#         s += '1'
#     r = int(s, 3)
#     if r > 337:
#         mn.add(r)
# print(min(mn))
# # 345


# 9
# def f(n):
#     s = ''
#     a = '012345'
#     while n != 0:
#         s += a[n % 6]
#         n //= 6
#     return s[::-1]
#
# n = 5 * 216**6 + 3 * 36**4 - 10
# print(f(n).count('5'))
# # 7


# 10
# def f(n):
#     s = ''
#     a = '01234'
#     while n != 0:
#         s += a[n % 5]
#         n //= 5
#     return s[::-1]
#
# n = 5**14 + 25**3 - 117
# print(f(n).count('4'))
# # 3


# 11
# # from string import *
# # print(ascii_uppercase)
# def f(n):
#     s = ''
#     a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     while n != 0:
#         s += a[n % 27]
#         n //= 27
#     return s[::-1]
#
# ans = set()
# for x in range(27001):
#     n = 3 * 27**9 + 2 * 27**6 + 27**3 - x
#     g = f(n)
#     if g.count('0') == 6:
#         ans.add(x)
# print(min(ans))
# # 27


# 12
# ans = set()
# for x in range(27):
#     s1 = int(f'2F{x}L325', 27)
#     s2 = int(f'17{x}BC5', 27)
#     s3 = int(f'31{x}MN', 27)
#     s = s1 + s2 + s3
#     if s % 15 == 0:
#         print(x, s//15)
# # 67382266


# 13
# # from string import *
# # s = '0123456789' + ascii_uppercase
# # for i in range(len(s)):
# #     print(i, s[i])
#
#
# for x in range(45):
#     s1 = 35*(45**4) + x*(45**3) + 33*(45**2) + 9*(45*1) + 8*(45**0)
#     s2 = x*(45**5) + 3*(45**4) + 9*(45**3) + 9*(45**2) + 6*(45**1) + 2*(45**0)
#     s = s1 + s2
#     if x == 34:
#         print(s//26)
# # 247453235