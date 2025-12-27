"""Решение дз к вебу: https://3.shkolkovo.online/lesson/36565"""

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





