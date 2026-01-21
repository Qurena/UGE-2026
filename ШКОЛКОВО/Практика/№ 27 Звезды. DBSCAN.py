"""Решение дз к вебу: https://3.shkolkovo.online/lesson/36565
+ https://3.shkolkovo.online/my/course/7259/materials/lesson/37135"""

# 1
'''
from math import dist
# from turtle import *
# tracer(0)
# m = 30
# up()
f = open("Файлы к задачам/1_B__5qgt7.txt")
b = f.readline()
a = [list(map(float, i.replace(",", ".").split())) for i in f if "X" not in i]
clusters = []
r = 0.1

while a:
    clusters.append([a.pop(0)])
    for i in clusters[-1]:
        for j in a[:]:
            if dist(i, j) <= r:
                # x, y = i
                # goto(x*m, y*m)
                # dot(5)
                clusters[-1].append(j)
                a.remove(j)

px = py = 0
for i in clusters:
        if len(i) > 5:
            mx = -1
            for star in i:
                s = 0
                for j in i:
                    s += dist(star, j)
                if s > mx:
                    mx = s
                    max_star = star
            px += max_star[0]
            py += max_star[1]
print(int((px/5)*100), int((py/5)*100))
# 1179 946
'''


# 2
# КОД ДЛЯ ФАЙЛА "A"
'''
from math import dist
# from turtle import *
# tracer(50)
# m = 15
# up()

f = open("2_A__5qgu0.txt")
a = [list(map(float, i.replace(",", ".").split())) for i in f if 'X' not in i]
clusters = []
r = 0.2

while a:
    clusters.append([a.pop(0)])
    for i in clusters[-1]:
        for j in a[:]:
            if dist(i, j) <= r:
                # x, y = i
                # goto(x*m, y*m)
                # dot(5)
                clusters[-1].append(j)
                a.remove(j)
                
clusters.remove(clusters[2]) # понял это с помощью визуализации

# for j in range(3):
#     for i in clusters[j]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5)
# done()

px = py = 0

for i in clusters:
    mn = 10 ** 10
    for star in i:
        s = 0
        for j in i:
            s += dist(star, j)
        if s < mn:
            mn = s
            center = star
    px += center[0]
    py += center[1]
    
print(int( (abs(px)/3) * 1000 ), int( (abs(py)/3) * 1000 ))
# 1042 1688
'''

# КОД ДЛЯ ФАЙЛА "B"
'''
from math import dist
# from turtle import *
# tracer(50)
# m = 15
# up()

f = open("2_B__5qgu2.txt")
a = [list(map(float, i.replace(",", ".").split())) for i in f if 'X' not in i]
clusters = []
r = 0.2

while a:
    clusters.append([a.pop(0)])
    for i in clusters[-1]:
        for j in a[:]:
            if dist(i, j) <= r:
                # x, y = i
                # goto(x*m, y*m)
                # dot(5)
                clusters[-1].append(j)
                a.remove(j)

clusters.remove(clusters[-1])
# for j in range(6):
#     for i in clusters[j]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(5)
# done()

px = py = 0

for i in clusters:
    mn = 10 ** 10
    for star in i:
        s = 0
        for j in i:
            s += dist(star, j)
        if s < mn:
            mn = s
            center = star
    px += center[0]
    py += center[1]
print(int( (abs(px/6)) * 1000 ), int( (abs(py/6)) * 1000 ))
# 280 200
'''


# 3
# КОД ДЛЯ ФАЙЛА "A"
'''
from math import dist
# from turtle import *
# tracer(50)
# m = 25
# up()

f = open("3A__5qkte.txt")
a = [list(map(float, i.replace(",", ".").split())) for i in f if 'X' not in i]
clusters = []
new_clusters = []
r = 0.45

while a:
    clusters.append([a.pop(0)])
    for i in clusters[-1]:
        for j in a[:]:
            if dist(i, j) < r:
                # x, y = i
                # goto(x*m, y*m)
                # dot(4)
                clusters[-1].append(j)
                a.remove(j)
for i in clusters:
    if len(i) > 30:
        new_clusters.append(i)

# for k in range(4):
#     for i in new_clusters[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3)
# done()

new_clusters.remove(new_clusters[2])
new_clusters.remove(new_clusters[-1])

# Рисуем нужные нам кластеры
# for k in range(len(new_clusters)):
#     for i in new_clusters[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3)
# done()

px = py = 0
for i in new_clusters:
    mn = 10**10
    for star in i:
        s = 0
        for j in i:
            s += dist(star, j)
        if s < mn:
            mn = s
            center = star
    px += center[0]
    py += center[1]

zx = px/2
zy = py/2
print(int(abs(zx)*100), int(abs(zy)*100))
# 484 97
'''

# КОД ДЛЯ ФАЙЛА "B"
'''
from math import dist
# from turtle import *
# tracer(50)
# m = 25
# up()

f = open("3B__5qktg.txt")
a = [list(map(float, i.replace(",", ".").split())) for i in f if 'X' not in i]
clusters = []
new_clusters = []
r = 0.4

while a:
    clusters.append([a.pop(0)])
    for i in clusters[-1]:
        for j in a[:]:
            if dist(i, j) < r:
                # x, y = i
                # goto(x*m, y*m)
                # dot(4)
                clusters[-1].append(j)
                a.remove(j)


for i in clusters:
    if len(i) > 30:
        new_clusters.append(i)

# Узнаем индексы кластеров
# for k in range(6):
#     for i in new_clusters[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3)
# done()


super_new_clusters = []
super_new_clusters.append(new_clusters[0])
super_new_clusters.append(new_clusters[1])
super_new_clusters.append(new_clusters[3])

px = py = 0
for i in super_new_clusters:
    mn = 10**10
    for star in i:
        s = 0
        for j in i:
            s += dist(star, j)
        if s < mn:
            mn = s
            center = star
    px += center[0]
    py += center[1]

zx = px/3
zy = py/3
print(int(abs(zx)*1000), int(abs(zy)*1000))
# 870 2128
'''

# 4
# КОД ДЛЯ ФАЙЛА "A"
# from math import dist
# f = open("txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
# r = 0.1
# tr = 2.2
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(j, i) < r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# px = py = 1
# for k in clusters:
#     if len(k) > 10:
#         mn = 10**10
#         for star in k:
#             s = 0
#             for i in k:
#                 s += dist(i, star)
#             if s < mn:
#                 mn = s
#                 mn_star = star
#         px *= mn_star[0]
#         py *= mn_star[1]
#
# print(int(px*py*100))
# #220



# 5 (Циклы и прямые)
# КОД ДЛЯ ФАЙЛА "A"
# from math import dist
# f = open("Файлы к задачам/27_4_A__51uc4.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[], []]
# trash = []
#
# for i in a:
#     x, y = i
#     if x**2 + y ** 2 <= 9:
#         clusters[1].append(i)
#     elif (x + 5)**2 + (y - 4)**2 <= 4:
#         clusters[0].append(i)
#     else:
#         trash.append(i)
#
#
# px = py = 0
# for k in clusters:
#     mn = 10**10
#     for star in k:
#         s = 0
#         for i in k:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
# print(int(abs(px/2)*333), int(abs(py/2)*666))
# # from turtle import *
# # tracer(0)
# # m = 20
# # screensize(200*200)
# # up()
# #
# # for i in clusters[2]:
# #     x, y = i
# #     goto(x*m, y*m)
# #     dot(3, 'blue')
# # done()
#
# # 800 1274

# КОД ДЛЯ ФАЙЛА "B"
# from math import dist
# f = open("Файлы к задачам/27_4_B__51uc6.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = [[], [], []]
# trash = []
#
# for i in a:
#     x, y = i
#     if (x - 1)**2 + (y + 1)**2 <= 9:
#         clusters[1].append(i)
#     elif (x + 5)**2 + (y + 5)**2 <= 16:
#         clusters[0].append(i)
#     elif (x + 6)**2 + (y - 3)**2 <= 4:
#         clusters[2].append(i)
#     else:
#         trash.append(i)
#
#
# px = py = 0
# for k in clusters:
#     mn = 10**10
#     for star in k:
#         s = 0
#         for i in k:
#             s += dist(star, i)
#         if s < mn:
#             mn = s
#             mn_star = star
#     px += mn_star[0]
#     py += mn_star[1]
# print(int(abs(px/3)*321), int(abs(py/3)*123))
#
# # from turtle import *
# # tracer(0)
# # m = 20
# # screensize(200*200)
# #
# # for _ in range(4):
# #     fd(100*m)
# #     bk(100*m)
# #     lt(90)
# #
# # up()
# # for i in clusters[2]:
# #     x, y = i
# #     goto(x*m, y*m)
# #     dot(3, 'blue')
# # done()
#
# # 1081 120



# 6 (DBSCAN)
# КОД ДЛЯ ФАЙЛА "A"
# from math import *
# f = open("Файлы к задачам/1A__5qktn.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
#
# ncluser = [[]]
# for i in a:
#     x, y = i
#     if y < -3 and -3 > x > -7.1:
#         ncluser[0].append(i)
#
# r = 0.15
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) < r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# px = py = 0
# mn1 = 10**10
# for star in clusters[0]:
#     s1 = 0
#     for i in clusters[0]:
#         s1 += dist(star, i)
#     if s1 < mn1:
#         mn1 = s1
#         mn_star1 = star
# px += mn_star1[0]
# py += mn_star1[1]
#
# mn2 = 10**10
# for star in ncluser[0]:
#     s2 = 0
#     for i in ncluser[0]:
#         s2 += dist(star, i)
#     if s2 < mn2:
#         mn2 = s2
#         mn_star2 = star
# px += mn_star2[0]
# py += mn_star2[1]
# print(int(abs(px/2)*100), int(abs(py/2)*100))
#
# # from turtle import *
# # tracer(0)
# # m = 35
# # screensize(2000*2000)
# # for _ in range(4):
# #     fd(100*m)
# #     bk(100*m)
# #     lt(90)
# #
# # colors = ['blue', 'green', 'purple', 'pink']
# # up()
# # for k in range(1):
# #     for i in clusters[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, colors[k])
# #
# #     for i in ncluser[k]:
# #         x, y = i
# #         goto(x*m, y*m)
# #         dot(3, 'pink')
# #
# # done()
#
# # 721 12

# КОД ДЛЯ ФАЙЛА "B"
# from math import *
# f = open("Файлы к задачам/1B__5qktp.txt")
# a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
# clusters = []
# clustersp = [[], [], []]
#
# for i in a:
#     x, y = i
#     if x < -6 and y < -5.8:
#         clustersp[0].append(i)
#         a.remove(i)
#     if x > 7 and y < -6:
#         clustersp[1].append(i)
#         a.remove(i)
#     if x > 4 and y > 7:
#         clustersp[2].append(i)
#         a.remove(i)
#
# r = 0.5
# while a:
#     clusters.append([a.pop(0)])
#     for i in clusters[-1]:
#         for j in a[:]:
#             if dist(i, j) < r:
#                 clusters[-1].append(j)
#                 a.remove(j)
#
# # px = py = 0
# # mn1 = 10**10
# # for star in clusters[0]:
# #     s1 = 0
# #     for i in clusters[0]:
# #         s1 += dist(star, i)
# #     if s1 < mn1:
# #         mn1 = s1
# #         mn_star1 = star
# # px += mn_star1[0]
# # py += mn_star1[1]
#
#
# from turtle import *
# tracer(0)
# m = 35
# screensize(2000*2000)
# for _ in range(4):
#     fd(100*m)
#     bk(100*m)
#     lt(90)
#
# colors = ['blue', 'green', 'purple', 'pink']
# up()
# # for i in clustersp[1]:
# #     x, y = i
# #     goto(x*m, y*m)
# #     dot(3, colors[2])
#
# for k in range(3):
#     for i in clusters[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3, colors[k])
# done()
#
# # ????