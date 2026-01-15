"""Решение дз к вебу:
https://3.shkolkovo.online/lesson/34223
+ https://3.shkolkovo.online/my/course/7259/dz/27814"""

# 1
'''
# Построил диаграмму в либре по файлу Б
# Код для файла A:
from math import *
f = open("27_A_1__4uxdd.txt")
a = [list(map(float, i.replace(",", '.').split())) for i in f if 'X' not in i]
clusters = []


clusters = [[], []]

for i in a:
    x, y = i
    if x < -35:
        clusters[0].append(i)
    else:
        clusters[1].append(i)


centers = []

for n in range(2):
    mn = 10**10
    for star in clusters[n]:
        s = 0
        for i in clusters[n]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)
px = (centers[0][0] + centers[1][0]) / 2
py = (centers[0][1] + centers[1][1]) / 2
print(int(abs(px)*1000), int(abs(py)*1000))
# A: 33644 4375
# B: 792 24451
'''

# 2

'''
# Код для файла A:
from math import *
f = open("27_A_2__4uxf2.txt")
a = [list(map(float, i.replace(",", ".").split())) for i in f if "X" not in i]

clusters = [[], [], [], [], []]

for i in a:
    x, y = i
    if y > x/2 + 20:
        clusters[0].append(i)
    elif x < -18:
        clusters[1].append(i)
    if y < -30:
        clusters[2].append(i)
    if y < 0 and x > 28:
        clusters[3].append(i)
    if y > 0 and x > 30:
        clusters[4].append(i)



centers = []

for n in range(5):
    mn = 10**10
    for star in clusters[n]:
        s = 0
        for i in clusters[n]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)
px = (centers[0][0] + centers[1][0] + centers[2][0] + centers[3][0] + centers[4][0]) / 5
py = (centers[0][1] + centers[1][1] + centers[2][1] + centers[3][1] + centers[4][1]) / 5
print(int(abs(px) * 1000), int(abs(py) * 1000))
# A: 409 6531
# B: 7839 25017'''


# 3
'''
# Код для файла B:
from math import *
f = open("27_1_B__51u81.txt")
a = [list(map(float, i.replace(",", ".").split())) for i in f if 'X' not in i]

clusters = [[], []]

for i in a:
    x, y = i
    if x**2 + y**2 < 12**2 and x < 0:
        clusters[0].append(i)
    if x**2 + y**2 < 12**2 and x > 0:
        clusters[1].append(i)

centers = []
for n in range(2):
    mn = 10**10
    for star in clusters[n]:
        s = 0
        for i in clusters[n]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)
px = (centers[0][0] + centers[1][0]) / 2
py = (centers[0][1] + centers[1][1]) / 2
print(int(px * 100), int(py * 100))
# A: -8 -9 
# B: -5 -4

# from turtle import *
#
# m = 15
# tracer(0)
# up()
# cl = ['red', 'green', 'blue']
#
# for j in range(3):
#     for i in clusters[j]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5, cl[j])
#
# for i in range(-200, 200):
#     for j in range(-200, 200):
#         x, y = i/10, j/10 # задаем плотность наших точек
#         if x**2 + y**2 > 12**2 and -20 < y < 20 and -18 < x < 18: # можем заменить на ур-е окр-ти - (x - 1.3)**2 + (y - 0.3)**2 < 1.5**2
#             goto(x*m, y*m)
#             dot(3, 'purple')
#
# for i in centers:
#     x, y = i
#     goto(x*m, y*m)
#     dot(15)
#
# done()
'''

# 4
# Файл А
# from math import dist
# from turtle import *
# f = open("Файлы к задачам/27_A__8vcrw.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[], []]
#
# c0 = 0
# c1 = 0
# for i in a:
#     x, y = i
#     if y > 90 and x < 40:
#         clusters[0].append(i)
#         c0 += 1
#     if y > 80 and x > 60:
#         c1 += 1
#         clusters[1].append(i)
# print(c0, c1)
#
# p1 = p2 = 0
# for k in range(2):
#     if k != 0:
#         mn = 10**10
#         for star in clusters[k]:
#             s = 0
#             for j in clusters[k]:
#                 s += dist(star, j)
#             if s < mn:
#                 mn = s
#                 mn_star = star
#         p1 += mn_star[0] + mn_star[1]
# print(p1)
# ans1 = 117.11175644254592
# ans2 = 153.21673240650313
# print(int(ans1*10000), int(ans2*10000))
# m = 20
# tracer(2)
# screensize(200*200)
# up()
# for k in range(2):
#     for i in clusters[k]:
#         x, y = i
#         goto(x, y)
#         dot(3, 'blue')
# done()

# 1171117 1532167

# Файл Б
# from math import dist
# from turtle import *
# f = open("Файлы к задачам/27_B__8vcrx.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[], [], []]
# trash  = []
#
# for i in a:
#     x, y = i
#     if x > 18 and y > 42:
#         clusters[0].append(i)
#     elif x > 19 and 42 > y > 33:
#         clusters[1].append(i)
#     elif x > 22 and 33 > y > 24:
#         clusters[2].append(i)
#     else:
#         trash.append(i)
#
# mn = 10**10
# for star in clusters[0]:
#     s = 0
#     for i in clusters[0]:
#         s += dist(i, star)
#     if s < mn:
#         mn = s
#         mn_star = star
#
# mn = 10**10
# for star1 in clusters[2]:
#     s1 = 0
#     for i1 in clusters[2]:
#         s1 += dist(i1, star1)
#     if s1 < mn:
#         mn = s1
#         mn_star1 = star1
#
# qx = mn_star[0]
# qy = mn_star1[1]
#
# print(int(qx*10000), int(qy*10000))
#
# # m = 5
# # tracer(5)
# # up()
# #
# # for k in range(3):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
# #
# # c1 = c2 = c3 = 0
# # for i in clusters[0]:
# #         c1 += dist([0, 0], i)
# # print(c1)
# # for i in clusters[1]:
# #         c2 += dist([0, 0], i)
# # print(c2)
# # for i in clusters[2]:
# #         c3 += dist([0, 0], i)
# # print(c3)
#
# # 222238 280837


# 5
# Файл А
# from math import dist
# from turtle import *
# f = open("Файлы к задачам/27А__7rojb.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[],[]]
#
# for i in a:
#     x, y = i
#     if x < 3 and y > 6:
#         clusters[0].append(i)
#     else:
#         clusters[1].append(i)
#
# # m = 10
# # tracer(0)
# # up()
# # for k in range(2):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# px = py = 0
# for k in range(2):
#     mn = 10**10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
# print(int((px/2)*10000), int((py/2)*10000))
# # 32055 58097

# Файл Б
# from math import dist
# from turtle import *
# f = open("Файлы к задачам/27Б__7rojd.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[],[],[]]
# trash = []
#
# for i in a:
#     x, y = i
#     if x < 3 and y < 2.3:
#         clusters[0].append(i)
#     elif x < 4 and y > 2.3:
#         clusters[1].append(i)
#     elif x > 5:
#         clusters[2].append(i)
#     else:
#         trash.append(i)
# # m = 20
# # tracer(0)
# # up()
# # for k in range(3):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# px = py = 0
# for k in range(3):
#     mn = 10*10
#     for star in clusters[k]:
#         s = 0
#         for i in clusters[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
# print(int((px/3)*10000), int((py/3)*10000))
# # 31886 25834


# 6
# Файл А
# from math import dist
# from turtle import *
# f = open('Файлы к задачам/3_A__5pzlk.txt')
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# c = [[], [], [], [], [], []]
#
# for i in a:
#     x, y = i
#     if x < 7 and y > 12:
#         c[0].append(i)
#     elif x < 12 and y < 8:
#         c[1].append(i)
#     elif 9 < x < 15 and 15 < y < 22:
#         c[2].append(i)
#     elif  26 > x > 20 and 24 > y > 18.5:
#         c[3].append(i)
#     elif 26 > x > 20 and 13 < y < 18.5:
#         c[4].append(i)
#     elif x > 24 and y < 12:
#         c[5].append(i)
#
# # m = 5
# # tracer(5)
# # up()
# # for k in range(6):
# #     for i in c[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# zx = zy = 0
# for k in range(6):
#     mn = 10**10
#     for star in c[k]:
#         s = 0
#         for i in c[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     zx += mn_star[0]
#     zy += mn_star[1]
# print(int((zx/6)*100), int((zy/6)*100))
# # 1619 1401


# Файл Б
# from math import dist
# from turtle import *
# f = open('Файлы к задачам/3_B__5pzln.txt')
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# c = [[], [], [], [], []]
#
# for i in a:
#     x, y = i
#     if x < 9 and y < 12:
#         c[0].append(i)
#     elif 7 < x < 14 and 16 < y < 23:
#         c[1].append(i)
#     elif 16 < x < 23 and 8 < y < 16:
#         c[2].append(i)
#     elif 29 > x > 21 and 8 > y > 0:
#         c[3].append(i)
#     elif 30 > x > 23 and 13 < y < 21:
#         c[4].append(i)
#
# # m = 5
# # tracer(0)
# # up()
# # for k in range(5):
# #     for i in c[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'blue')
# # done()
#
# zx = zy = 0
# for k in range(5):
#     mn = 10**10
#     for star in c[k]:
#         s = 0
#         for i in c[k]:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     zx += mn_star[0]
#     zy += mn_star[1]
# print(int((zx/5)*100), int((zy/5)*100))
# # 1736 1225