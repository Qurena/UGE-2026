"""
Решение ДЗ к вебу https://3.shkolkovo.online/lesson/34219
+ конспект к вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/36569
+ дз к вебу: https://3.shkolkovo.online/my/course/7259/dz/27119
"""

# 1
'''
f = open("24_M3__42nfh.txt")
s = f.readline()

g = 'EYUIOA'


cdot = cg = mx = start = 0

for end in range(len(s)):
    if s[end] in g:
        cg += 1
    if s[end] == '.':
        cdot += 1

    while cdot > 6:
        if s[start] in g:
            cg -= 1
        if s[start] == '.':
            cdot -= 1
        start += 1

    if cg > 15 and cdot <= 6:
        mx = max(mx, end - start + 1)
print(mx)
# 592
'''

# 2
'''
f = open("24_2024__7aiiq.txt")
s = f.readline()

ct = start = mx = 0

for end in range(len(s)):
    if s[end] == 'T':
        ct += 1
    while ct > 100:
        if s[start] == 'T':
            ct -= 1
        start += 1
    if ct == 100:
        mx = max(mx, end - start + 1)
print(mx)
# 133 
'''

# 3
'''
f = open("24_18__3b9tx.txt")
s = f.readline()

cf = cl = start = mx = 0

for end in range(len(s)):
    if s[end] == 'F':
        cf += 1
    if s[end] == 'L':
        cl += 1
    while cl > 3 or cf > 3:
        if s[start] == 'F':
            cf -= 1
        if s[start] == 'L':
            cl -= 1
        start += 1
    if cf <= 3 and cl <= 3:
        mx = max(mx, end - start + 1)
print(mx)
# 292
'''

# 4
'''
f = open("24_16__3b9u2.txt")
s = f.readline()

mn = 10**10

start = cy = 0

for end in range(len(s)):
    if s[end] == 'Y':
        cy += 1
    while cy >= 100:
        mn = min(mn, end - start + 1)
        if s[start] == 'Y':
            cy -= 1
        start += 1

print(mn)
# 108
'''

# 5
'''
f = open("24_4__3b9tg.txt")
s = f.readline()

mx = 0

start = cd = 0

for end in range(len(s)):
    if s[end] == 'D':
        cd += 1
    while cd > 100:
        if s[start] == 'D':
            cd -= 1
        start += 1
    if cd <= 100:
        mx = max(mx, end - start + 1)

print(mx)
# 838
'''

# 6
'''
---------------------------------------------------------------------------------------------------
Текстовый файл состоит из символов A,B,C,D,E,F.
Определите в прилагаемом файле максимальное количество идущих подряд символов
(длину непрерывной подпоследовательности), среди которых символ B встречается ровно 53 раза.
---------------------------------------------------------------------------------------------------

f = open('24.txt')
s = f.readline()

start = cb = mx = 0

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
'''


# 7
'''
---------------------------------------------------------------------------------------------------
Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
Определите в прилагаемом файле максимальное количество идущих подряд символов,
среди которых подстрока 2025 встречается не менее 90 раз и при этом содержится ровно 80 букв Y.
В ответе запишите число – количество символов в найденной последовательности.
---------------------------------------------------------------------------------------------------

f = open('24.txt')
s = f.readline()
s = s.replace('2025', '*')
start = cy = cp = mx = 0

for end in range(len(s)):
    if s[end] == 'Y':
        cy += 1
    if s[end] == '*':
        cp += 1
    while cy > 80:
        if s[start] == 'Y':
            cy -= 1
        if s[start] == '*':
            cp -= 1
        start += 1
    if cy == 80 and cp >= 90:
        mx = max(mx, end - start + 1 + cp*3)
print(mx)
'''

# 8
'''
---------------------------------------------------------------------------------------------------
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
Определите максимальное количество идущих подряд символов,
среди которых ровно по одному разу встречаются буквы X и Y.
---------------------------------------------------------------------------------------------------

f = open("24__7h7ej.txt")
s = f.readline()

mx = cx = cy = start = 0

for end in range(len(s)):
    if s[end] == 'X':
        cx += 1
    if s[end] == 'Y':
        cy += 1
    while cx > 1 or cy > 1:
        if s[start] == 'X':
            cx -= 1
        if s[start] == 'Y':
            cy -= 1
        start += 1
    if cx == 1 and cy == 1:
        mx = max(mx, end - start + 1)
print(mx)
# 224
'''

# 9
'''
---------------------------------------------------------------------------------------------------
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
Определите максимальное количество идущих подряд символов,
среди которых каждая из букв C и D встречается не более двух раз.
---------------------------------------------------------------------------------------------------

f = open("Файлы к задачам/24__7h77f.txt")
s = f.readline()

mx = cc = cd = start = 0

for end in range(len(s)):
    if s[end] == 'C':
        cc += 1
    if s[end] == 'D':
        cd += 1
    while cc > 2 or cd > 2:
        if s[start] == 'C':
            cc -= 1
        if s[start] == 'D':
            cd -= 1
        start += 1
    if cc <= 2 and cd <= 2:
        mx = max(mx, end - start + 1)
print(mx)
# 253
'''

# 10
'''
---------------------------------------------------------------------------------------------------
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
Определите максимальное количество идущих подряд символов,
среди которых каждая из букв UVWXYZ встречается не более ста раз.
---------------------------------------------------------------------------------------------------

f = open("Файлы к задачам/24__7h6ti.txt")
s = f.readline()

mx = cu = cv = cw = cx = cy = cz = start = 0

for end in range(len(s)):
    if s[end] == 'U':
        cu += 1
    if s[end] == 'V':
        cv += 1
    if s[end] == 'W':
        cw += 1
    if s[end] == 'X':
        cx += 1
    if s[end] == 'Y':
        cy += 1
    if s[end] == 'Z':
        cz += 1
    while cu > 100 or cv > 100 or cw > 100 or cx > 100 or cy > 100 or cz > 100:
        if s[start] == 'U':
            cu -= 1
        if s[start] == 'V':
            cv -= 1
        if s[start] == 'W':
            cw -= 1
        if s[start] == 'X':
            cx -= 1
        if s[start] == 'Y':
            cy -= 1
        if s[start] == 'Z':
            cz -= 1
        start += 1
    if cu <= 100 and cv <= 100 and cw <= 100 and cx <= 100 and cy <= 100 and cz <= 100:
        mx = max(mx, end - start + 1)
print(mx)
# 2844
'''

# 11
'''
---------------------------------------------------------------------------------------------------
Текстовый файл содержит строку из заглавных латинских букв и точек,
всего не более 106 символов. Определите максимальное количество идущих подряд символов,
среди которых не более шести точек и более 15 гласных букв.
---------------------------------------------------------------------------------------------------

f = open("24_M3__42nfh.txt")
s = f.readline()

mx = cg = cd = start = 0

for end in range(len(s)):
    if s[end] in 'AEIOUY':
        cg += 1
    if s[end] == '.':
        cd += 1
    while cd > 6:
        if s[start] in 'AEIOUY':
            cg -= 1
        if s[start] == '.':
            cd -= 1
        start += 1
    if cg > 15 and cd <= 6:
        mx = max(mx, end - start + 1)
print(mx)
# 592
'''

