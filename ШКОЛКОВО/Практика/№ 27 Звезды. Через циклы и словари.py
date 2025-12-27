"""Решение дз к вебу: https://3.shkolkovo.online/lesson/34223"""

# 1
'''
# Построил диаграмму в либре по файлу Б
# Код для файла A:
from math import *
f = open("27_A_1__4uxdd.txt")
a = [list(map(float, i.replace(",", '.').split())) for i in f if 'X' not in i]


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
