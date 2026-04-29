"""
Решение ДЗ к вебу: https://3.shkolkovo.online/lesson/34221
И к вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/36690
"""


# 1
'''
def f(n):
    if n <= 2:
        return n + 3
    return f(n-1) + g(n-2)

def g(n):
    if n <= 2:
        return n + 1
    return g(n-1) + f(n-1)

print(g(4) + f(5))
# 33
'''

# 2
'''
def f(n):
    if n ==1:
        return 1
    if n % 2 == 0:
        return n + f(n-1)
    return 3*f(n-2)
print(f(30))
# 4782999
'''

# 3
'''
# from functools import *
# @lru_cache(None)

from sys import *
setrecursionlimit(10000)
def g(n):
    if n < 10:
        return 2 * n
    return g(n-2) + 1

# for i in range(16000, -1, -1):
#     g(i)

print(2*(g(15545) + 8))
# 15588
'''

# 4
'''
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a + 2, b) + f(a * 4, b)

print(f(2, 17))
# 1052
'''

# 7
'''
def f(a, b):
    if a > b or a == 11 or a == 14:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a * 2, b) + f(a * 3, b)

print(f(1, 17) * f(17, 32))
# 20
'''

# 10
'''
def f(a, b):
    if a > b or a == 14:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 2, b) + f(a * 3, b)

print(f(2, 10) * f(10, 15))
# 120
'''


# ----------------------------------------------------------------------------------------------------------------------

# 1
# def f(start, end):
#     if start > end:
#         return 0
#
#     if start == end:
#         return 1
#
#     return f(start + 2, end) + f(start * 3, end)
#
# print(f(7, 77))
# # 14


# 2
# def f(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#
#     return f(start + 2, end) + f(start * 3, end)
#
# print(f(2, 42))
# # 15


# 3
# def f(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#
#     return f(start - 1, end) + f(start - 3, end) + f(start // 3, end)
#
# print(f(22, 2))
# # 2196


# 4
# def f(start, end, g11, g17):
#     if start > end:
#         return 0
#     if start == end and g11 == 1 and g17 == 1:
#         return 1
#
#     if start == 11:
#         g11 = 1
#     if start == 17:
#         g17 = 1
#
#     return f(start + 1, end, g11, g17) + f(start + 5, end, g11, g17) + f(start * 2, end, g11, g17)
#
# print(f(4, 24, 0, 0))
# # 72


# 5
# def f(start, end, g8, b14):
#     if start > end:
#         return 0
#     if start == end and g8 == 1 and b14 == 0:
#         return 1
#
#     if start == 8:
#         g8 = 1
#     if start == 14:
#         b14 = 1
#
#     return f(start + 1, end, g8, b14) + f(start + 2, end, g8, b14)
#
# print(f(1, 19, 0, 0))
# # 840


# 6
# def f(start, end, g8, b10):
#     if start > end:
#         return 0
#     if start == end and g8 == 1 and b10 == 0:
#         return 1
#
#     if start == 8:
#         g8 = 1
#     if start == 10:
#         b10 = 1
#
#     return f(start + 1, end, g8, b10) + f(start * 2, end, g8, b10) + f(start + 5, end, g8, b10)
#
# print(f(1, 16, 0,0))
# # 45


# 7
# def f(start, end, g14, b16):
#     if start > end:
#         return 0
#     if start == end and g14 == 1 and b16 == 0:
#         return 1
#
#     if start == 14:
#         g14 = 1
#     if start == 16:
#         b16 = 1
#
#     return f(start + 1, end, g14, b16) + f(start * 2, end, g14, b16) + f(start * 3, end, g14, b16)
#
# print(f(1, 50, 0, 0))
# # 192


# 8
# def f(start, end, k1, k2, g):
#     if start > end:
#         return 0
#
#     if start == end and g == 0:
#         return 1
#
#     if k1 == 3 or k2 == 3:
#         g = 1
#
#     return f(start + 1, end, k1 + 1, 0, g) + f(start * 2, end, 0, k2 + 1, g)
#
# print(f(1, 14, 0, 0, 0))
# # 6


# 9 !!!!!!!!!!!!!!!
# def f(start, end, cA):
#     if start > end + 1:
#         return 0
#     if start == end and cA != 2:
#         return 1
#
#     if cA == 1:
#         return f(start * 2, end, 0) + f(start * 3, end, 0)
#
#     return f(start - 1, end, cA + 1) + f(start * 2, end, cA) + f(start * 3, end, cA)
#
# print(f(3, 15, 0))
# # 6


# 10
# def f(start, end, cB):
#     if start > end:
#         return 0
#
#     if start == end and cB != 2:
#         return 1
#
#     if cB == 1:
#         return f(start + 1, end, 0) + f(start * 2, end, 0)
#     return f(start + 1, end, 0) + f(start + 2, end, cB + 1) + f(start * 2, end, 0)
#
# print(f(2, 22, 0))
# # 4953