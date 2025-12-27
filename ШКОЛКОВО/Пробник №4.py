"""Решение пробника №4: https://3.shkolkovo.online/my/course/7259/dz/26329"""

# 2
'''
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = ((y <= (not(w) and y)) <= ((z==y) and not(z==w))) and x
                if F == 1:
                    print(x, y, w, z)
# yxzw
'''

# 5
'''
def f(n: int) -> int:
    s = bin(n)[2:]
    for _ in range(2):
        l = sum(int(i) for i in s)
        s += str(l % 2)
    r = int(s, 2)
    return r

a = []
for n in range(10000):
    if f(n) > 73:
        a.append(f(n))
print(min(a))
# 78
'''

# 6
'''
from turtle import *

tracer(0)
screensize(200*200)
lt(90)
m = 15

for _ in range(2):
    fd(14*m)
    lt(270)
    back(12*m)
    rt(90)

up()

fd(9*m)
rt(90)
back(7*m)
lt(90)

down()

for _ in range(2):
    fd(13*m)
    rt(90)
    fd(6*m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(3, 'blue')
done()
# 251
'''

# 8
'''
from itertools import *

s = 'ПРОГА'
c = 0

for i in product(s, repeat=6):
    s = ''.join(i)
    if s.count('Р') >= 3:
        c += 1
print(c)
# 1545
'''

# 13
'''
from ipaddress import *

net = ip_network('162.115.138.246/255.255.252.0', 0)
ip = ip_address('162.115.138.246')

nm = int(ip)-int(net.network_address)

print(nm)
# 758
'''

# 14
'''
def sev(n):
    s = ''
    while n != 0:
        s += str(n%7)
        n //= 7
    return s[::-1]

ans = []
for x in range(1, 2031):
    f = 7**170 + 7**100 - x
    s = sev(f)
    if s.count('0') == 71:
        ans.append(x)
print(max(ans))
# 2029
'''

# 16
'''
def f(n):
    if n > 2024:
        return n
    return n * f(n+1)
print(f(2022)/f(2024))
# 4090506
'''

# 17
'''
f = open('Файлы для пробников/17_6__2j8pw.txt')
a = f.readlines()

s = []
for el in a:
    s.append(int(el[:-1]))

mel = []
for el in s:
    if el % 16 == 0:
        mel.append(el)

m = min(mel)

mn = []
c = 0
for i in range(len(s)-1):
    t = [s[i], s[i+1]]
    if s[i] % m == 0 or s[i+1] % m == 0:
        if sum(t) % 6 == 0:
            c += 1
            mn.append(sum(t))
print(c, min(mn))
'''

# 19
'''
def steps(p):
    next_steps = [p + 3, p + 5, p * 2]
    return next_steps

def play(p, r):
    if p >= 67:
        return r % 2 == 0
    if p >= 67 or r == 0:
        return False

    next_plays = [play(step, r-1) for step in steps(p)]

    return any(next_plays) if (r-1)%2 == 0 else all(next_plays)

for s in range(1, 67):
    if play(s, 2):
        print(s)
# 31
        
# Проверка (второй вариант кода) 
# def f(a):
#     if a >= 67:
#         return 0
# 
#     t = [f(a + 3), f(a + 5), f(a * 2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
# 
# for s in range(1, 67):
#     if f(s) == -1:
#         print(s)
'''

# 20
'''
def steps(p):
    next_steps = [p + 3, p + 5, p * 2]
    return next_steps

def play(p, r):
    if p >= 67:
        return r % 2 == 0
    if p >= 67 or r == 0:
        return False

    next_plays = [play(step, r-1) for step in steps(p)]

    return any(next_plays) if (r-1)%2 == 0 else all(next_plays)

for s in range(1, 67):
    if not play(s, 1) and play(s, 3):
        print(s)
# 16 30

# Проверка (второй вариант кода)
# def f(a):
#     if a >= 67:
#         return 0
# 
#     t = [f(a + 3), f(a + 5), f(a * 2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
# 
# for s in range(1, 67):
#     if f(s) != 1 and f(s) == 2:
#         print(s)
'''

# 21
# def steps(p):
#     next_steps = [p + 3, p + 5, p * 2]
#     return next_steps
#
# def play(p, r):
#     if p >= 67 and r in (0, 2):
#         return True
#     if p >= 67 or r == 0:
#         return False
#
#     next_plays = [play(step, r-1) for step in steps(p)]
#
#     return any(next_plays) if (r-1)%2 == 0 else all(next_plays)
#
# for s in range(1, 67):
#     if not play(s, 2) and play(s, 4):
#         print(s)
# 23

# Проверка (второй вариант кода)
# def f(a):
#     if a >= 67:
#         return 0
#
#     t = [f(a + 3), f(a + 5), f(a * 2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n) + 1
#     return -max(t)
#
# for s in range(1, 67):
#     if (f(s) == -1 or f(s) == -2) and f(s) != -1:
#         print(s)

# 24
'''
from re import *

f = open('Файлы для пробников/24_5__6ao1t.txt')
s = f.readline()

pattern = r'(?=((0|[1-9]+[0-9]*)([*](0|[1-9]+[0-9]*))+))'

mx = -1
for i in finditer(pattern, s):
    t = i.group(1)
    k = eval(t)
    mx = max(mx, k)
print(str(mx)[-10:])
# 3389404980
'''

# 25
'''
from fnmatch import *

pattern = r'1[0-9]*3577[0-9]0'

for n in range(1, 10**9):
    if n % 1975 == 0:
        if fnmatch(str(n), '1*3577?0'):
            print(n, n//1975)
# 106357700 53852
# 112357750 56890
# 185357700 93852
# 191357750 96890
'''
# 27 (для файла A)
'''
from math import dist
f = open('Файлы для пробников/5A__4vld4.txt')
a = [list(map(float, i.replace(',', '.').split())) for i in f if 'X' not in i]
clusters = [[], []]

for i in a:
    x, y = i
    if y < 0 and x < 0:
        clusters[0].append(i)
    if -20 < x < 20 and 0 < y < 24:
        clusters[1].append(i)

centers = []
for k in range(2):
    mn = 10**10
    for star in clusters[k]:
        s = 0
        for i in clusters[k]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)
px = (centers[0][0] + centers[1][0])/2
py = (centers[0][1] + centers[1][1])/2
print(int(abs(px)*1000), int(abs(py)*1000))
# 2526 705

# from turtle import *
#
# tracer(0)
# screensize(200*200)
# m = 10
#
# up()
# for k in range(2):
#     for i in clusters[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
'''

# 27 (для файла B)
'''
from math import dist
f = open('Файлы для пробников/5B__4vld6.txt')
a = [list(map(float, i.replace(',', '.').split())) for i in f if 'X' not in i]
clusters = [[], [], [], [], []]

for i in a:
    x, y = i
    if y < -25 and x < -23:
        clusters[0].append(i)
    if -24 < x < 0 and 15 < y < 35:
        clusters[1].append(i)
    if 0 < x < 22 and -21 < y < 0:
        clusters[2].append(i)
    if 0 < x < 27 and -40 < y < -21:
        clusters[3].append(i)
    if 17 < x < 36 and -1 < y < 20:
        clusters[4].append(i)

centers = []
for k in range(5):
    mn = 10**10
    for star in clusters[k]:
        s = 0
        for i in clusters[k]:
            s += dist(star, i)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)
px = (centers[0][0] + centers[1][0] + centers[2][0] + centers[3][0] + centers[4][0])/5
py = (centers[0][1] + centers[1][1] + centers[2][1] + centers[3][1] + centers[4][1])/5
print(int(abs(px)*1000), int(abs(py)*1000))
# 1155 8441

# from turtle import *
#
# tracer(0)
# screensize(200*200)
# m = 5
#
# up()
# for k in range(5):
#     for i in clusters[k]:
#         x, y = i
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
'''
