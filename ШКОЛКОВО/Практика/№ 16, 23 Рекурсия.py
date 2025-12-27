"""Решение ДЗ к вебу https://3.shkolkovo.online/lesson/34221"""

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