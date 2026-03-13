# 2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((not(x)) and y and z and (not(w))) or ((not(x)) and y and (not(z)) and (not(w))) or (x and y and z and (not(w)))
#                 if F == 1:
#                     print(x, y, z, w)

# 5
# def ans(n):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = '10' + s
#     else:
#         s = '1' + s + '01'
#     return int(s, 2)
#
# mn = 10**10
# for n in range(19, 10**5):
#     if ans(n) < mn:
#         mn = min(mn, ans(n))
# print(mn)
# # 84



# 17
# f = open("17_27629.txt")
# n = [int(i) for i in f]
# mx43 = max(i for i in n if len(str(abs(i))) == 4 and abs(i) % 100 == 43)
#
# c = mx = 0
# for i in range(len(n) - 1):
#     t = n[i:i+2]
#     fours = sum(1 for i in t if len(str(abs(i))) == 4)
#     if fours >= 1 and sum(t)**2 < mx43**2:
#         c += 1
#         mx = max(mx, sum(t)**2)
#
# print(c, mx)
# # 1218 98843364


# 23
# def f(start: int, end: int) -> int:
#     d = {}
#     for i in range(start, end - 1, -1):
#         d[i] = 0
#
#     d[start] = 1
#
#     for key in d.keys():
#         if key - 1 in d:
#             d[key - 1] += d[key]
#         if key // 2 in d:
#             d[key // 2] += d[key]
#     return d[end]
#
# print(f(40, 16)*f(16, 6))
# # 60


# 24
# from re import *
# f = open("24_27777.txt")
# s = f.readline()
# pattern = r'(?=(([1-9]*[AB]*[1-9]*[AB]*[1-9]*)+))'
# mx = 0
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mx = max(mx, len(g))
#     print(g)
# # 18


# 25
# from fnmatch import *
#
# for i in range(271, 10**8, 271):
#     if fnmatch(str(i), '12??15*6'):
#         print(i, i//271)
# # 1202156 4436
# # 12001506 44286
# # 12131586 44766
# # 12421556 45836
# # 12711526 46906


# 19
# def steps(p):
#     h1, h2 = p
#     return (h1 + 1, h2), (h1 * 2, h2), (h1, h2 + 1), (h1, h2 * 2)
# def play(p, r):
#     if sum(p) >= 207 and r == 0:
#         return True
#     if sum(p) >= 207 or r == 0:
#         return False
#
#     next_plays = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_plays) if r % 2 != 0 else any(next_plays)
#
# for s in range(2, 190):
#     if play((17, s), 2) and not(play((17, s), 1)):
#         print(s)
# # 48


# 20
def steps(p):
    h1, h2 = p
    return (h1 + 1, h2), (h1 * 2, h2), (h1, h2 + 1), (h1, h2 * 2)
def play(p, r):
    if sum(p) >= 207 and r % 2 == 0:
        return True
    if sum(p) >= 207 or r == 0:
        return False

    next_plays = [play(step, r - 1) for step in steps(p)]

    return any(next_plays) if r % 2 != 0 else all(next_plays)

for s in range(2, 190):
    p = (17, s)
    if not(play(p, 1)) and play(p, 3):
        print(s)
# 48
from functools import *

@lru_cache(None)
def f(a, b):
    if a + b >= 207:
        return True
    t = [f(a + 1, b), f(a * 2, b), f(a, b + 1), f(a, b * 2)]
    n = [int(i) for i in t if i <= 0]
    if n:
        return -max(n) + 1
    return -max(t)

for s in range(2, 190):
    if f(17, s) != 1 and f(17, s) == 2:
        print(s)