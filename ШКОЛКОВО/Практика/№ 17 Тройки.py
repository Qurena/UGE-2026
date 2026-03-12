"""Дз к вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/37103"""

# 1
# f = open("Файлы к задачам/17_16__8hqqv.txt")
# a = [int(i) for i in f]
# mxd = max(i for i in a if abs(i) % 100 == 13)
#
# mn = 10**10
# c = 0
# for i in range(len(a) - 8):
#     t = a[i:i+9]
#     sevens = sum(i**2 for i in t if i % 2 == 0)
#     e = sum(1 for i in t if (abs(i) % 10) % 2 == 0)
#     o = sum(1 for i in t if (abs(i) % 10) % 2 != 0)
#     if sevens < mxd**2 and o > e:
#         c += 1
#         mn = min(mn, sum(t))
# print(c, mn)
# # 1041 -161653


# 2
# f = open("Файлы к задачам/17_22__8hqqr.txt")
# a = [int(i) for i in f]
#
# def tr(t):
#     fd = set()
#     for el in t:
#         fd.add(int(str(el)[0]))
#     if len(fd) == 8:
#         return True
#     return False
#
# mx = c = 0
# for i in range(len(a) - 7):
#     t = a[i:i+8]
#     frs = sum(1 for i in t if i % 4 == 0)
#     trs = sum(1 for i in t if i % 3 == 0)
#     if tr(t) and frs > trs:
#         c += 1
#         mx = max(mx, sum(t))
# print(c, mx)
# # 51 495359


# 3
# from math import prod
# f = open("Файлы к задачам/17_18__8hqpf.txt")
# a = [int(i) for i in f]
#
# def f(t):
#     mxs = []
#     for _ in range(3):
#         m1 = max(t)
#         mxs.append(m1)
#         t.remove(m1)
#     return mxs, t
#
# mx = c = 0
# for i in range(len(a) - 5):
#     t = a[i:i+6]
#     evens = sum(1 for i in t if i % 2 == 0)
#     odds = sum(1 for i in t if i % 2 != 0)
#     mxs, mns = f(t)
#     t = a[i:i + 6]
#     if prod(mxs) % sum(mns) == 0 and evens == odds:
#         c += 1
#         mx = max(mx, sum(t))
# print(c, mx)
# # 2 328373


# 4
# f = open("Файлы к задачам/17_20__8hqp5.txt")
# a = [int(i) for i in f]
# c = 0
# mid = []
# for i in range(len(a) - 5):
#     t = a[i:i+6]
#     minus = sum(1 for i in t if i < 0)
#     if minus >= 2 and int(sum(t)/6) % 3 == 0:
#         c += 1
#         mid.append(sum(t)/6)
# print(c, int(min(mid)))
# # 4473 -7950


# 5
# f = open("Файлы к задачам/17_17__8hqnx.txt")
# a = [int(i) for i in f]
# mx17 = max(i for i in a if abs(i) % 17 == 0)
# c, mn = 0, 10**10
# for i in range(len(a) - 4):
#     t = a[i:i+5]
#     evens = sum(1 for i in t if i % 2 == 0)
#     if evens == 3 and sum(t) > mx17:
#         c += 1
#         mn = min(mn, sum(t))
# print(c, mn)
# # 8416 622108
