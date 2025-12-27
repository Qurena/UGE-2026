"""Решение пробника №3: https://3.shkolkovo.online/my/course/7259/dz/26326"""

# 2

print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (not(x <= y)) or z or (not(w))
                if F == 0:
                    print(x, y, w, z)
# zyxw


# 5
'''
def f(n):
    s = bin(n)[2:]
    for _ in range(3):
        if s.count("0") == s.count("1"):
            s += s[-1]
        else:
            if s.count("0") > s.count("1"):
                s += '1'
            else:
                s += '0'
    r = int(s, 2)
    return r

for n in range(94, 160):
    if f(n) % 6 == 0:
        print(n)
        break
# 111
'''


# 6
'''
from turtle import *

tracer(0)
lt(90)
m = 20
screensize(200*200)

fd(10*m)
down()
for _ in range(5):
    fd(-6 * m)
    lt(180)
    fd(4*m)
    rt(90)
# lt(180)
# fd(5*m)
# lt(180)
back(5*m)
for _ in range(8):
    fd(3*m)
    rt(135)
    back(5*m)
    rt(45)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(3, 'blue')
done()

# 87
'''


# 7
'''
from itertools import *
s = 'ЕПРЮ'

c = 0
for i in product(s, repeat=5):
    k = ''.join(i)
    c += 1

    if k[:2] == 'ЮР':
        print(k, c)
        break
# 897
'''


# 14
# from string import *
# print(ascii_uppercase)
# def f(n):
#     a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     s = ''
#     while n != 0:
#         if n % 45 < 10:
#             s += str(n % 45)
#         if n % 45 < 36 and n % 45 >= 10:
#             s += a[n%45 - 10]
#         if n % 45 >= 36:
#             s += str(n % 45)
#
#         n //= 45
#
#     return s[::-1]


# 17
'''
f = open("Файлы для пробников/5__1vf59.txt")
s = f.readlines()
c = 0
k = []

for el in s:
    k.append(int(el[:-1]))

sums = []
for i in range(len(k)-2):
    if (k[i] % 2 == 0 and k[i+1] % 2 != 0 and k[i+2] % 2 != 0) or (k[i] % 2 != 0 and k[i+1] % 2 == 0 and k[i+2] % 2 != 0) or (k[i] % 2 != 0 and k[i+1] % 2 != 0 and k[i+2] % 2 == 0):
        if min(k[i], k[i+1], k[i+2]) + max(k[i], k[i+1], k[i+2]) < sum(k)/len(k):
            c += 1
            sums.append(k[i] + k[i+1] + k[i+2])
print(c, max(sums))
# 1581 9154
'''


# 19
'''
# 1 решение
# def f(a):
#     if a >= 29:
#         return 0
#
#     t = [f(a+1), f(a*2)]
#     n = [i for i in t if i <= 0]
#
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 29):
#     if f(s) != 1 and f(s) == -1:
#         print(s)

# 2 решение (для проверки)
def steps(p):
    return p + 1, p * 2

def play(p, r):
    if p >= 29:
        return r % 2 == 0
    if r == 0:
        return False
    next_plays = []
    for step in steps(p):
        next_plays.append(play(step, r - 1))

    if r - 1 == 1:
        return all(next_plays)
    if r - 1 == 0:
        return any(next_plays)

for p in range(1, 29):
    if play(p, 2):
        print(p)
# 14
'''


# 21
'''
def f(a):
    if a >= 29:
        return 0

    t = [f(a+1), f(a*2)]
    n = [i for i in t if i <= 0]

    if n:
        return -max(n) + 1
    return -max(t)

for s in range(1, 29):
    if (f(s) == -1 or f(s) == -2) and f(s) != -1:
        print(s)
# 12
'''


# 23
'''
def f(start: int, end: int) -> int:
    d = {}
    for i in range(start, end + 1):
        d[i] = 0

    d[start] = 1

    if 18 in d:
        del d[18]

    for key in d.keys():
        if key + 4 in d:
            d[key + 4] += d[key]
        if key * 2 in d:
            d[key * 2] += d[key]
        if key * 3 in d:
            d[key * 3] += d[key]
    return d[end]

print(f(2, 6) * f(6, 296))
# 6320
'''


# 24
'''
from re import *

f = open("Файлы для пробников/24_1__6ba37.txt")
s = f.readline()

pattern = r'(0|[1-6][0-6]*)([+*](0|[1-6][0-6]*))+'

mx = 0
for i in finditer(pattern, s):
    t = i.group()
    mx = max(mx, len(t))
print(mx)
# 33
'''


# 25
'''
from functools import *
@lru_cache(None)
def f(n: int):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return f(n - 1) + f(n - 2)

fib = []
for n in range(28, 36):
    print(f(n))

start = 235_121
end = 1_004_523
# 317811 514229 832040
'''


# 27

# Код для файла A
'''
from math import dist
f = open('Файлы для пробников/1A__5gsno.txt')
s = [list(map(float, i.replace(',', '.').split())) for i in f if 'X' not in i]
clusters = [[],[]]

for star in s:
    x, y = star
    if x < -60 and y < -10:
        clusters[0].append(star)
    else:
        clusters[1].append(star)

centers = []
for k in range(2):
    mx = -1
    for star in clusters[k]:
        s = 0
        for i in clusters[k]:
            s += dist(star, i)
        if s > mx:
            mx = s
            per_star = star
    centers.append(per_star)
px = centers[0][0] * centers[1][0]
py = centers[0][1] * centers[1][1]
print(int( abs(px)/100 ), int( abs(py)/100 ))
# 38 7


# from turtle import *
#
# tracer(0)
# lt(90)
# screensize(200*200)
# m = 10
#
# up()
# for k in range(2):
#     for star in clusters[k]:
#         x, y = star
#         goto(x*m, y*m)
#         dot(3, 'blue')
#
# done()
'''

# Код для файла B
'''
from math import dist
f = open('Файлы для пробников/1B__5gsnq.txt')
s = [list(map(float, i.replace(',', '.').split())) for i in f if 'X' not in i]
clusters = [[], [], [], []]

for star in s:
    x, y = star
    if x < -35 and y < -30:
        clusters[0].append(star)
    if x < -10 and (0 > y > -30):
        clusters[1].append(star)
    if x < 0 and y > 10:
        clusters[2].append(star)
    if x > 0 and y > 0:
        clusters[3].append(star)

centers = []
for k in range(4):
    mx = -1
    for star in clusters[k]:
        s = 0
        for i in clusters[k]:
            s += dist(star, i)
        if s > mx:
            mx = s
            per_star = star
    centers.append(per_star)
px = centers[0][0] * centers[1][0] * centers[2][0] * centers[3][0]
py = centers[0][1] * centers[1][1] * centers[2][1] * centers[3][1]
print(int( abs(px)/100 ), int( abs(py)/100 ))
# 7106 41705


# from turtle import *
#
# tracer(0)
# lt(90)
# screensize(200*200)
# m = 3
#
# fd(100*m)
# back(200*m)
# fd(100*m)
# lt(90)
# fd(100*m)
# back(200*m)
# fd(100*m)
#
# up()
# for k in range(4):
#     for star in clusters[k]:
#         x, y = star
#         goto(x*m, y*m)
#         dot(3, 'blue')
#
# done()
'''