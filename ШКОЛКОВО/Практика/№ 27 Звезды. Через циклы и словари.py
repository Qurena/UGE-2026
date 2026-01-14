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
from math import dist
from turtle import *
f = open("27_A__8vcrw.txt")
a = [list(map(float, i.replace(',','.').split())) for i in f if 'X' not in i]
clusters = [[], []]

c0 = 0
c1 = 0
for i in a:
    x, y = i
    if y > 90 and x < 40:
        clusters[0].append(i)
        c0 += 1
    if y > 80 and x > 60:
        c1 += 1
        clusters[1].append(i)
print(c0, c1)

p1 = p2 = 0
for k in range(2):
    if k != 0:
        mn = 10**10
        for star in clusters[k]:
            s = 0
            for j in clusters[k]:
                s += dist(star, j)
            if s < mn:
                mn = s
                mn_star = star
        p1 += mn_star[0] + mn_star[1]
print(p1)
ans1 = 117.11175644254592
ans2 = 153.21673240650313
print(int(ans1*10000), int(ans2*10000))
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