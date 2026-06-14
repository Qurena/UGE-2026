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


'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/31903'''

# 1
# f = open("Файлы к задачам/17_4__8cuce.txt")
# n = [int(i) for i in f]
# count = 0
# mn = 10**10
# for i in range(len(n) - 3):
#     t = n[i:i+4]
#     q = sum(1 for el in t if el < 0)
#     m = sum(1 for el in t if el > 0)
#     if q > m and sum(t) > 0:
#         count += 1
#         mn = min(mn, sum(t))
# print(count, mn)
# # 131 23


# 2
# from math import prod
# f = open("Файлы к задачам/17_3__8cu84.txt")
# n = [int(i) for i in f]
# count = mx = 0
# for i in range(len(n) - 6):
#     t = n[i:i+7]
#     if prod(t) % 23 == 0:
#         odds = evens = 0
#         for el in t:
#             flag_odd = 0
#             flag_even = 0
#             for dig in str(el):
#                 if dig in '02468':
#                     flag_odd = 1
#                 else:
#                     flag_even = 1
#             if flag_odd == 0:
#                 odds += 1
#             if flag_even == 0:
#                 evens += 1
#         if odds > evens:
#             count += 1
#             mx = max(mx, max(t) - min(t))
# print(count, mx)
# # 367 49348


# 3
# f = open("Файлы к задачам/17_15__89i3v.txt")
# n = [int(i) for i in f]
# count = 0
# mn = 10**10
# for i in range(len(n) - 2):
#     t = n[i:i + 3]
#     if sum(t) % 7 == 0:
#         n_check = set()
#         for el in t:
#             n_check.add(len(str(abs(el))))
#         if len(n_check) == 3:
#             count += 1
#             mn = min(mn, sum(t))
# print(count, mn)
# # 8 2086


# 4
# f = open("Файлы к задачам/17_14__89i3l.txt")
# n = [int(i) for i in f]
# mid = sum(n)/len(n)
# count = 0
# mn = 10**10
# for i in range(len(n) - 1):
#     t = n[i:i+2]
#     c1 = sum(1 for el in t if el % 4 == 0)
#     c2 = sum(1 for el in t if el > mid)
#     c3 = sum(1 for el in t if el > mid and el % 4 == 0) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     if c1 == 1 and c2 == 1 and c3 == 0:
#         count += 1
#         mn = min(mn, sum(t))
# print(count, mn)
# # 1174 -4457


# 5
# f = open("Файлы к задачам/17_13__89i39.txt")
# n = [int(i) for i in f]
# count = mx = 0
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     evens = sum(1 for el in t if el % 2 == 0)
#     odds = sum(1 for el in t if el % 2 != 0)
#     if evens == 2 and odds == 1:
#         count += 1
#         mx = max(mx, sum(t))
# print(count, mx)
# # 3399 104017


# 6
# f = open("Файлы к задачам/17_10__89i27.txt")
# n = [int(i) for i in f]
# def e(n):
#     for dig in str(n):
#         if dig in '13579':
#             return False
#     return True
#
# evenmx = (max(el for el in n if e(el)))**2
# count = 0
# mn = 10**10
# for i in range(len(n) - 1):
#     t = n[i:i+2]
#     sm = sum(el**2 for el in t)
#     if sm > evenmx:
#         count += 1
#         mn = min(mn, sum(t))
# print(count, mn)
# # 1945 895


# 7
# f = open("Файлы к задачам/17_9__89i1v.txt")
# n = [int(i) for i in f]
# count = mx = 0
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     c1 = sum(1 for el in t if el % 13 == 0)
#     if c1 > 0 and sum(t) % 10 == 0:
#         count += 1
#         mx = max(mx, sum(t))
# print(count, mx)
# # 216 77740
















