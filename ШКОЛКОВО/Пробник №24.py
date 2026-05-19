"""https://3.shkolkovo.online/my/course/7259/dz/31902"""

# 1
# 31

# 2
# print('x y w z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = w and (x or (not(y))) and (not(w == z))
#                 if F == 1:
#                     print(x, y, w, z, int(F))
# # wzyx


# 3
# 120


# 4
# 110

# 5
# def ans(k):
#     m = 1
#     c10 = k//10
#     c1 = k % 10
#     m = k * c10 + c1
#     return m
#
# for k in range(1, 100):
#     if ans(k) == 61:
#         print(k)
# # 27


# 6
# from turtle import *
# lt(90)
# tracer(0)
# m = 15
# screensize(4000, 4000)
#
# for _ in range(3):
#     fd(12*m)
#     rt(90)
#     fd(6*m)
#     rt(90)
#
# up()
# fd(5*m)
# rt(90)
# fd(1*m)
# lt(90)
#
# down()
# for _ in range(5):
#     fd(10*m)
#     rt(90)
#     fd(14*m)
#     rt(90)
#
# up()
#
#
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 48


# 7
# 16


# 8
# def nine(n):
#     s = ''
#     while n != 0:
#         s += str(n % 9)
#         n //= 9
#     return s[::-1]
# ans = 0
# for x in range(553030, 10_000_000):
#     q = nine(x)
#     r = [el for el in q]
#     ch = '02468'
#     nch = '1357'
#     if len(q) == 7:
#         if len(set(r)) == 7:
#             if r[0] in ch and r[1] in nch and r[2] in ch and r[3] in nch and r[4] in ch and r[5] in nch and r[6] in ch:
#                 ans += 1
#             if r[0] in nch and r[1] in ch and r[2] in nch and r[3] in ch and r[4] in nch and r[5] in ch and r[6] in nch:
#                 ans += 1
# print(ans)
# # 3744


# 9
# 4


# 10
# 1


# 11
# раз непосимвольное кодирование, N = 98, L = 1 -> I1 = 1 * 7 (бит)
# тогда ответ: 92*7 = 644


# 12
# XYYXXYYX


# 13
# from ipaddress import *
#
# net = ip_network('17.100.13.33/255.255.248.0', 0)
#
# ip = ip_address('17.100.13.33')
#
# num = 0
# for i in net.hosts():
#     num += 1
#     if i == ip:
#         print(num)
# 1313


# 14
# mx = []
# for x in range(37):
#     for y in range(37):
#         F = 9 * (37**0) + y * (37**1) + 7 * (37**2) + 5 * (37**3) + 4 * (37**4) + x * (37**5)+ 1 * (37**6) + 2 * (37**7)
#         if F % 36 == 0:
#             rt = y * (37**0) + x * (37**1)
#             mx.append(rt)
# print(max(mx))
# # 1340


# 15
# 417


# 16
# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n - 1)
#
# for n in range(3000):
#     f(n)
#
# print(f(2023)/f(2020))
# # 8266912626


# 17
# f = open("Файлы для пробников/17-1__7byb8.txt")
# n = [int(i) for i in f]
# mx7 = max(el for el in n if abs(el)%10 == 7)
#
# ans1 = 0
# ans2 = []
# for i in range(len(n) - 2):
#     t = n[i:i+3]
#     fr = str(abs(t[0]))[0]
#     k1 = sum(1 for el in t if str(abs(el))[0] == fr)
#     k2 = sum(1 for el in t if abs(el) % 10 == 7 and len(str(abs(el))) == 3)
#     sm = abs(sum(t))
#     if sm < mx7 and k1 == 3 and k2 >= 1:
#         ans1 += 1
#         ans2.append(abs(sum(t)))
# print(ans1, max(ans2))
# # 1 45768


# 18
# 3282 - первое значение
# def f(start1, end1, start2, end2):
#     if start1 > start2 or end1 < end2:
#         return 0
#     if start1 == start2 and end1 == end2:
#         return 1
#     return f(start1 + 1, end1, start2, end2) + f(start1, end1 - 1, start2, end2)
#
# print(f(0, 0, 24, -24) - 1)
# для второго, думаю, можно было бы сделать что-то подобное + выколоть поля с нулями, указав их координаты


# 19
# # 1 решение:
# def steps(p):
#     return [p + 2, p * 3]
#
# def play(p, r):
#     if p >= 53:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_steps) if r % 2 == 0 else any(next_steps)
#
# for s in range(1, 52):
#     if play(s, 2) and (not(play(s, 1))):
#         print(s)
# # 16


# # 2 решение:
# def f(a):
#     if a >= 53:
#         return False
#
#     steps = [f(a + 2), f(a * 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(1, 52):
#     if f(s) == -1:
#         print(s)
# # 16


# 20
# # 1 решение:
# def steps(p):
#     return [p + 2, p * 3]
#
# def play(p, r):
#     if p >= 53:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_steps) if r % 2 == 0 else any(next_steps)
#
# for s in range(1, 52):
#     if play(s, 3) and (not(play(s, 1))):
#         print(s)
# # 14 15


# # 2 решение:
# def f(a):
#     if a >= 53:
#         return False
#
#     steps = [f(a + 2), f(a * 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(1, 52):
#     if f(s) == 2:
#         print(s)
# # 14 15


# 21
# # 1 решение:
# def steps(p):
#     return [p + 2, p * 3]
#
# def play(p, r):
#     if p >= 53:
#         return r % 2 == 0
#
#     if r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return all(next_steps) if r % 2 == 0 else any(next_steps)
#
# for s in range(1, 52):
#     if play(s, 4) and (not(play(s, 2))):
#         print(s)
# # 13


# # 2 решение:
# def f(a):
#     if a >= 53:
#         return False
#
#     steps = [f(a + 2), f(a * 3)]
#     win_check = [i for i in steps if i <= 0]
#     if win_check:
#         return -max(win_check) + 1
#     return -max(steps)
#
# for s in range(1, 52):
#     if f(s) == -2:
#         print(s)
# # 13


# 22
# 6112


# 23
# def f(start, end):
#     if start > end or start == 7:
#         return 0
#     if start == end:
#         return 1
#
#     return f(start + 1, end) + f(start + 2, end) + f(start * 2, end)
#
# print(f(2, 30) * f(30, 41))
# # 58667328


# 24
# 1 решение:
# f = open("Файлы для пробников/24_2024__7aiiq.txt")
# s = f.readline()
# start = ct = mx = 0
#
# for end in range(len(s)):
#     if s[end] == 'T':
#         ct += 1
#     while ct > 100:
#         if s[start] == 'T':
#             ct -= 1
#         start += 1
#     if ct == 100:
#         mx = max(mx, end + 1 - start)
# print(mx)
# # 133


# 2 решение:
# f = open("Файлы для пробников/24_2024__7aiiq.txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(mx + i, len(s)):
#         t = s[i:j+1]
#         if t.count('T') == 100:
#             mx = max(mx, len(t))
#         if t.count('T') > 100:
#             break
# print(mx)
# # 133


# 25
# def rdivs(n):
#     div = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             if i % 2 == 0:
#                 div.add(i)
#             if (n // i) % 2 == 0:
#                 div.add(n // i)
#     if len(div) == 4:
#         return div
#     return 0
#
# for n in range(81234, 81298 + 1):
#     if rdivs(n) != 0:
#         print(*sorted(list(rdivs(n))))
#
# # 2 302 538 81238
# # 2 82 1982 81262
# # 2 358 454 81266
# # 2 194 838 81286
# # 2 4 40646 81292
# # 2 14 11614 81298



# 26
# f = open("Файлы для пробников/26__1nxs0.txt")
# # f = open("test.txt")
# n, budget = map(int, f.readline().split())
#
# A_series = []
# B_series = []
# for d in f:
#     cost, amount, type = d.split()
#     if type == 'A':
#         A_series.append([int(cost), int(amount), type])
#     else:
#         B_series.append([int(cost), int(amount), type])
#
# A_series.sort(key=lambda x: (x[0], x[1]))
# B_series.sort(key=lambda x: (x[0], x[1]))
#
# bought_A = 0
# cost_A = 0
# for el in A_series:
#     cost_A += el[0]*el[1]
# st_B = budget - cost_A  # -> мы закупили все детали А, так как st_B > 0
#
# for el in A_series:
#     bought_A += el[1]
#
# bought_B = 0
# ost_B = []
# cost_B = 0
# for i in range(len(B_series)):
#     el = B_series[i]
#     if st_B > el[0]*el[1]:
#         st_B -= el[0] * el[1]
#         bought_B += el[1]
#         cost_B += el[0] * el[1]
#     else:
#         ost_B.append(el)
#
# dobor = ost_B[0]
# last_price = dobor[0]
# last_take = 0
# for am in range(1, dobor[1] + 1):
#     if st_B >= am * last_price:
#         last_take = am
#
# st_B -= last_take * last_price
# cost_B += last_take * last_price
# bought_B += last_take
#
# ans1 = bought_B + bought_A
# ans2 = cost_B
# print(ans1, ans2)
# # 14735 613321


# 27A
# from math import dist
#
# f = open("Файлы для пробников/27_3A__achk4.txt")
# data = []
# for star in f:
#     if 'X' not in star:
#         x, y, par = star.split()
#         data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#
# # print(len(data))
#
# n_clusters = []
# clusters = []
# trash = []
# r = 0.5
#
# while data:
#     n_clusters.append([data.pop(0)])
#     for i in n_clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 n_clusters[-1].append(j)
#                 data.remove(j)
#
# for c in n_clusters:
#     if len(c) > 60:
#         clusters.append(c)
#         # print(f'len(c): {len(c)}')
#     else:
#         trash.append(c)
# # print(len(clusters), len(trash))
#
# centers = []
# for k in range(len(clusters)):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
# # print(centers)
#
# mn_dist = 10**10
# for star1 in centers:
#     for star2 in centers:
#         if star1 != star2:
#             mn_dist = min(mn_dist, dist(star1[:2], star2[:2]))
# ans1 = mn_dist
#
# # сначала найдём ближайшие к центрам 3-х кластеров подходящие звезды:
# # 1 кластер:
# dst = 10**10
# h1 = 0
# num_cl = 0
# for star in clusters[num_cl]:
#     par_star = star[2]
#     if (par_star[0] == 'B') and (par_star[1] in '3456789'):
#         dst = min(dst, dist(centers[num_cl][:2], star[:2]))
#
# for star in clusters[num_cl]:
#     par_star = star[2]
#     if (par_star[0] == 'B') and (par_star[1] in '3456789'):
#         if dist(centers[num_cl][:2], star[:2]) == dst:
#             h1 = star
#
# # 2 кластер:
# dst = 10**10
# h2 = 0
# num_cl = 1
# for star in clusters[num_cl]:
#     par_star = star[2]
#     if (par_star[0] == 'B') and (par_star[1] in '3456789'):
#         dst = min(dst, dist(centers[num_cl][:2], star[:2]))
#
# for star in clusters[num_cl]:
#     par_star = star[2]
#     if (par_star[0] == 'B') and (par_star[1] in '3456789'):
#         if dist(centers[num_cl][:2], star[:2]) == dst:
#             h2 = star
#
# # 3 кластер:
# dst = 10**10
# h3 = 0
# num_cl = 2
# for star in clusters[num_cl]:
#     par_star = star[2]
#     if (par_star[0] == 'B') and (par_star[1] in '3456789'):
#         dst = min(dst, dist(centers[num_cl][:2], star[:2]))
#
# for star in clusters[num_cl]:
#     par_star = star[2]
#     if (par_star[0] == 'B') and (par_star[1] in '3456789'):
#         if dist(centers[num_cl][:2], star[:2]) == dst:
#             h3 = star
#
# ans2 = dist(h1[:2], h2[:2]) + dist(h2[:2], h3[:2]) + dist(h3[:2], h1[:2])
# print(int(abs(ans1*10_000)), int(abs(ans2*10_000)))
# # 114265 453688
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 15
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# #
# # up()
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y, t = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(centers)):
# #     star = centers[k]
# #     x, y, t = star
# #     goto(x*m, y*m)
# #     dot(5, 'red')
# #
# # for k in range(len(check)):
# #     star = check[k]
# #     x, y, t = star
# #     goto(x*m, y*m)
# #     dot(6, 'green')
# #
# # done()


# 27B
# from math import dist
#
# f = open("Файлы для пробников/27_3B__achk5.txt")
# data = []
# data_for_ans = []
# for star in f:
#     if 'X' not in star:
#         x, y, par = star.split()
#         data.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
#         data_for_ans.append([float(x.replace(',','.')), float(y.replace(',','.')), par])
# # print(len(data))
#
# n_clusters = []
# clusters = []
# trash = []
# r = 0.5
#
# while data:
#     n_clusters.append([data.pop(0)])
#     for i in n_clusters[-1]:
#         for j in data[:]:
#             if dist(i[:2], j[:2]) <= r:
#                 n_clusters[-1].append(j)
#                 data.remove(j)
#
# for c in n_clusters:
#     if len(c) > 60:
#         clusters.append(c)
#         # print(f'len(c): {len(c)}')
#     else:
#         trash.append(c)
# # print(len(clusters), len(trash))
#
# centers = []
# for k in range(len(clusters)):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star[:2], i[:2])
#         if s < mn:
#             mn = s
#             mn_star = star
#     centers.append(mn_star)
# # print(centers)
#
# # min len - 5 кластер; max len - первый кластер
# ver1 = centers[0]
# ver2 = centers[-1]
# # print(ver1, ver2)
#
# ans1 = 0
# ans2 = 0
# for star in data_for_ans:
#     x, y, par = star
#     if par[0] == 'K':
#         if min(ver1[0], ver2[0]) <= x <= max(ver1[0], ver2[0]):
#             if min(ver1[1], ver2[1]) <= y <= max(ver1[1], ver2[1]):
#                 ans1 += 1
#     if par[-3:] == 'III':
#         if min(ver1[0], ver2[0]) <= x <= max(ver1[0], ver2[0]):
#             if min(ver1[1], ver2[1]) <= y <= max(ver1[1], ver2[1]):
#                 ans2 += 1
# print(ans1, ans2)
# # 137 201
#
# # from turtle import *
# # lt(90)
# # tracer(0)
# # m = 15
# # screensize(4000, 4000)
# # for _ in range(4):
# #     fd(100*m)
# #     back(100*m)
# #     lt(90)
# #
# # up()
# # for k in range(len(clusters)):
# #     for star in clusters[k]:
# #         x, y, t = star
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# #
# # for k in range(len(centers)):
# #     star = centers[k]
# #     x, y, t = star
# #     goto(x*m, y*m)
# #     dot(5, 'red')
# #
# # done()