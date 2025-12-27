"""Пробник: https://3.shkolkovo.online/my/course/7259/dz/25863"""

# 2
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= x) or (not(z) and w)) == (w == x)
                if F:
                    print(x, y, z, w)
# xwyz
'''

# 3
'''
print(int(20794000/12))
'''

# 5
'''
def f(n: int) -> int:
    s = bin(n)[2:]
    for _ in range(2):
        if s.count('1') == s.count('0'):
            s += s[-1]
        else:
            if s.count('1') < s.count('0'):
                s += '1'
            else:
                s += '0'
    return int(s, 2)

a = set()
for n in range(2, 300):
    r = f(n)
    if r % 3 == 0 and r % 2 != 0:
        a.add(n)
print(max(a))
# 297
'''

# 6
'''
from turtle import *
screensize(200*200)
k = 10
tracer(0)
lt(90)

for _ in range(12):
    for _ in range(15):
        fd(2*k)
        rt(90)
    fd(5*k)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, 'red')
done()
# 25
'''

# 8
'''
def egg(n: int) -> str:
    s = ''
    while n != 0:
        s += str(n % 8)
        n //= 8

    return s[::-1]

def good(n: str) -> bool:
    a = set()
    for i in range(7):
        a.add(n[i])
    if len(a) == 7:
        if (int(n[0]) % 2 == 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 != 0 and int(n[4]) % 2 == 0 and int(n[5]) % 2 != 0 and int(n[6]) % 2 == 0)    or   (int(n[0]) % 2 != 0 and int(n[1]) % 2 == 0 and int(n[2]) % 2 != 0 and int(n[3]) % 2 == 0 and int(n[4]) % 2 != 0 and int(n[5]) % 2 == 0 and int(n[6]) % 2 != 0):
            return True
    return False
ans = 0
for n in range(1, 10000000):
    if len(egg(n)) == 7:
        t = egg(n)
        if good(t):
            ans += 1
print(ans)
# 1008
'''

# 14
'''
from functools import lru_cache
@lru_cache(None)
def f(n: int) -> int:
    s = ''
    a = 'ABCDEFGHIJKLMNOPQ'
    while n != 0:
        if n % 27 < 10:
            s += str(n % 27)
        else:
            s += a[n % 27 - 10]
        n //= 27
    return s[::-1]

x = 6 * (3 ** 1520) + 9 ** 321 + 3 ** 407 - 2022
print(f(x).count('0'))
# 370
'''

# 16
'''
def f (n: int):
    if n >= 2025:
        return n
    return n + f(n + 2)

print(f(2022) - f(2023))
# 2024
'''

# 17
'''
with open('9__1vf5f.txt') as file:
    f = file.readlines()
    
a = [int(el) for el in f]

ans = 0
mx = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 134 == 0:
            ans += 1
            if a[i] + a[j] > mx:
                mx = a[i] + a[j]
print(ans, mx)
# 372713 19966
'''

# 19-21
'''
def f(a: int) -> int:
    if a >= 55:
        return 0
    t = [f(a+2), f(a*2)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    return -max(t)

for i in range(1, 55):
    if (f(i) == -1 or f(i) == -2) and f(i) != -1:
        print(i)
# 2223
'''

# 23
'''
def f(a, b, c=0):
    if a > b or c > 6:
        return 0
    if a == b and c == 6:
        return 1
    return f(a + 1, b, c + 1) + f(a + 10, b, c + 1) + f(a * 3, b, c + 1)

a = 0
for i in range(1, 10000):
    if f(8, i) != 0:
        a += 1
print(a)
# 313
'''

# 24
'''
f = open("24__3ns0t.txt")
s = f.readline()

start = mx = cb = 0

for end in range(len(s)):
    if s[end] == 'B':
        cb += 1
    while cb > 53:
        if s[start] == 'B':
            cb -= 1
        start += 1
    if cb == 53:
        mx = max(mx, end - start + 1)
print(mx)
# 515
'''
# 25
'''
def divs(n: int) -> list[int]:
    divs = set()
    for div in range(1, int(n**0.5) + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    return sorted(list(divs))

for n in range(100_812, 100_924):
    if len(divs(n)) == 6:
        print(divs(n)[-2], divs(n)[-1])
# 5933 100861
# 50438 100876
# 50458 100916
# 33639 100917
'''

# 27
'''
from math import dist
f = open("B__5xipg.txt")
a = [list(map(float, i.replace(",", ".").split())) for i in f if 'X' not in i]
clusters = [[], [], []]
for i in a:
    x, y, z, = i
    if y > 7:
        clusters[1].append(i)
    else:
        if x < 0:
            clusters[0].append(i)
        else:
            clusters[2].append(i)

centers = []
for n in range(3):
    mn = 10**10
    for star in clusters[n]:
        s = 0
        for k in clusters[n]:
            s += dist(star, k)
        if s < mn:
            mn = s
            mn_star = star
    centers.append(mn_star)
px = (centers[0][0] + centers[1][0] + centers[2][0])/3
py = (centers[0][1] + centers[1][1] + centers[2][1])/3
pz = (centers[0][2] + centers[1][2] + centers[2][2])/3
print(int(abs(px) * 1000), int(abs(py)*1000), int(abs(pz)*1000))
'''






