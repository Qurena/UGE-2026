"""
Решение ДЗ к вебу https://3.shkolkovo.online/lesson/34219
+ веб: https://3.shkolkovo.online/my/course/7259/materials/lesson/36569
+ дз к вебу: https://3.shkolkovo.online/my/course/7259/dz/27119
+ веб: https://3.shkolkovo.online/my/course/7259/materials/lesson/38917
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

f = open('24dtwwe.txt')
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

f = open('24dtwwe.txt')
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


# ----------------------------------------------------------------------------------------------------------------------
'''https://3.shkolkovo.online/my/course/7259/materials/lesson/38917'''

# 4 | Посл-ть, ограниченная точками с двух сторон
# from string import ascii_uppercase
# f = open("Файлы к задачам/24_M3__42ngp.txt")
# s = f.readline()
# mx = 0
# cp = 0
# c1 = c2 = 0
# start = s.find('.')
# for end in range(len(s)):
#     if s[end] == '.':
#         cp += 1
#     elif s[end] in ascii_uppercase[:13]:
#         c1 += 1
#     else:
#         c2 += 1
#
#     while cp > 4:
#         start += 1
#         if s[start] == '.':
#             cp -= 1
#         elif s[start] in ascii_uppercase[:13]:
#             c1 -= 1
#         else:
#             c2 -= 1
#
#     if s[start] == '.' and s[end] == '.' and cp <= 4 and c1 > c2:
#         mx = max(mx, end - start + 1)
# print(mx)
# # 378


# ----------------------------------------------------------------------------------------------------------------------
'''https://3.shkolkovo.online/my/course/7259/dz/29319'''

# 3
# from string import *
# f = open("Файлы к задачам/24-7__8ag28.txt")
# s = f.readline()
# start = cz = cg = ck9 = 0
# mn = 10**10
# bad = ascii_uppercase[:10] + ascii_uppercase.lower()
#
# for end in range(len(s)):
#     if s[end] in bad:
#         cg += 1
#     if s[end] == 'Z':
#         cz += 1
#
#     while cz > 28 or cg != 0:
#         if s[start] in bad:
#             cg -= 1
#         if s[start] == 'Z':
#             cz -= 1
#         start += 1
#
#     if cg == 0 and cz == 28 and (s[start] == 'K' or s[start] == '9'):
#         mn = min(mn, end - start + 1)
#         for n_start in range(start, start + 100):
#             if s[n_start] in bad:
#                 cg -= 1
#             if s[n_start] == 'Z':
#                 cz -= 1
#             if (s[n_start] == 'K' or s[n_start] == '9') and cg == 0 and cz == 28:
#                 mn = min(mn, end - n_start + 1)
# print(mn)
# # 990

'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/31901'''

# 1 | max(len), 'CD' <= 220 и 'BE' >= 55

# 1 решение через УКАЗАТЕЛИ:
# f = open("Файлы к задачам/24__9gm2o.txt")
# s = f.readline()
# mx = start = ccd = cbe = 0
# for end in range(len(s)):
#     if s[end - 1:end + 1] == 'CD': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         ccd += 1
#     if s[end - 1:end + 1] == 'BE': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         cbe += 1
#     while ccd > 220:
#         if s[start:start + 2] == 'CD': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             ccd -= 1
#         if s[start:start + 2] == 'BE': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             cbe -= 1
#         start += 1
#
#     if ccd <= 220 and cbe >= 55:
#         mx = max(mx, end - start + 1)
# print(mx)
# # 2752


# 2 решение через ЦИКЛЫ:
# f = open("Файлы к задачам/24__9gm2o.txt")
# s = f.readline()
# mx = 0
#
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j+1]
#         if t.count('CD') <= 220:
#             if t.count('BE') >= 55:
#                 mx = max(mx, len(t))
#         else:
#             break
# print(mx)
# 2752

# ----------------------------------------------------------------------------------------------------------------------

# 2 | max(len), без 'M', 'A', 'T', 'H'

# 1 решение через УКАЗАТЕЛИ:
# f = open("Файлы к задачам/24_8__3b9ul.txt")
# s = f.readline()
# mx = start = cbad = 0
# for end in range(len(s)):
#     if s[end] in 'MATH':
#         cbad += 1
#
#     if cbad > 0:
#         if s[start] in 'MATH':
#             cbad -= 1
#         start += 1
#
#     if cbad == 0:
#         mx = max(mx, end - start + 1)
#
# print(mx)
# # 88


# 2 решение через ЦИКЛЫ:
# f = open("Файлы к задачам/24_8__3b9ul.txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j+1]
#         c = sum(1 for el in t if el in 'MATH')
#         if c == 0:
#             mx = max(mx, len(t))
#         else:
#             break
# print(mx)
# # 88

# ----------------------------------------------------------------------------------------------------------------------

# 3 | max(len), 'D' <= 100

# 1 решение через УКАЗАТЕЛИ:
# f = open('Файлы к задачам/24_4__3b9tg.txt')
# s = f.readline()
#
# mx = start = cd = 0
#
# for end in range(len(s)):
#     if s[end] == 'D':
#         cd += 1
#     while cd > 100:
#         if s[start] == 'D':
#             cd -= 1
#         start += 1
#     if cd <= 100:
#         mx = max(mx, end - start + 1)
#
# print(mx)
# # 838


# 2 решение через ЦИКЛЫ:
# f = open('Файлы к задачам/24_4__3b9tg.txt')
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j+1]
#         if t.count('D') <= 100:
#             mx = max(mx, len(t))
#         else:
#             break
# print(mx)
# # 838

# ----------------------------------------------------------------------------------------------------------------------

# 4 | max(len), без 'A'

# 1 решение через УКАЗАТЕЛИ:
# f = open("Файлы к задачам/8__2pp7a.txt")
# s = f.readline()
#
# mx = start = ca = 0
#
# for end in range(len(s)):
#     if s[end] == 'A':
#         ca += 1
#     while ca > 0:
#         if s[start] == 'A':
#             ca -= 1
#         start += 1
#     if ca == 0:
#         mx = max(mx, end - start + 1)
#
# print(mx)
# # 51


# 2 решение через ЦИКЛЫ:
# f = open("Файлы к задачам/8__2pp7a.txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j+1]
#         if 'A' not in t:
#             mx = max(mx, len(t))
#         else:
#             break
# print(mx)
# # 51

# ----------------------------------------------------------------------------------------------------------------------

# 5 | max(len), 'DF' и 'LE' нет одновременно

# 1 решение через УКАЗАТЕЛИ:
# f = open("Файлы к задачам/7__2pp79.txt")
# s = f.readline()
# s = s.replace('DF', '**')
# s = s.replace('LE', '&&')
# mx = start = cdf = cle = 0
#
# for end in range(len(s)):
#     if s[end-1:end + 1] == '**':  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         cdf += 1
#     if s[end-1: end + 1] == '&&': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         cle += 1
#     while cdf > 0 and cle > 0:
#         if s[start: start + 2] == '**': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             cdf -= 1
#         if s[start: start + 2] == '&&': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             cle -= 1
#         start += 1
#
#     t = s[start:end + 1]
#     if not (t.count('**') > 0 and t.count('&&') > 0):
#         mx = max(mx, len(t))
# print(mx)
# # 6197


# 2 решение через ЦИКЛЫ:
# f = open("Файлы к задачам/7__2pp79.txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j + 1]
#         if ('DF' not in t) or ('LE' not in t):
#             mx = max(mx, len(t))
#             if mx == 3143:
#                 print(t.count('DF'), t.count('LE'))
#         if 'DF' in t and 'LE' in t:
#             break
# print(mx)
# # 6197

# ----------------------------------------------------------------------------------------------------------------------

# 6 | max(len), без 'CEDA'

# 1 решение через УКАЗАТЕЛИ:
# f = open("Файлы к задачам/4__2pp6x.txt")
# s = f.readline()
# mx = start = cbad = 0
#
# for end in range(len(s)):
#     if s[end-3:end + 1] == 'CEDA':
#         cbad += 1
#     while cbad > 0:
#         if s[start:start + 4] == 'CEDA':
#             cbad -= 1
#         start += 1
#
#     if cbad == 0:
#         mx = max(mx, end - start + 1)
#
# print(mx)
# 4151


# 2 решение через ЦИКЛЫ:
# f = open("Файлы к задачам/4__2pp6x.txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j+1]
#         if t.count('CEDA') == 0:
#             mx = max(mx, len(t))
#         else:
#             break
# print(mx)
# # 4151

'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/29318'''

# 3
# 1 решение:
# f = open("Файлы к задачам/8__1vq2j.txt")
# s = f.readline()
# start = cAE = mx = 0
#
# for end in range(len(s)):
#     if s[end-1:end+1] == 'AE':
#         cAE += 1
#     while cAE > 0:
#         if s[start:start + 2] == 'AE':
#             cAE -= 1
#         start += 1
#     if cAE == 0:
#         mx = max(mx, end + 1 - start)
# print(mx)
# # 1743

# 2 решение:
# f = open("Файлы к задачам/8__1vq2j.txt")
# s = f.readline()
#
# mx = 0
# for i in range(len(s)):
#     for j in range( i + mx, len(s)):
#         t = s[i:j + 1]
#         if t.count('AE') == 0:
#             mx = max(mx, len(t))
#         if t.count('AE') > 0:
#             break
# print(mx)
# # 1743


# 4
# f = open("Файлы к задачам/24_16__3b9u2.txt")
# s = f.readline()
#
# start = cy = 0
# mn = 10**10
# for end in range(len(s)):
#     if s[end] == 'Y':
#         cy += 1
#     while cy > 100:
#         if s[start] == 'Y':
#             cy -= 1
#         start += 1
#     if cy == 100:
#         mn = min(mn, end + 1 - start)
# print(mn)
# # 108


# 5
# 1 решение:
# f = open("Файлы к задачам/24_18__3b9tx.txt")
# s = f.readline()
#
# start = cf = cl = mx = 0
# for end in range(len(s)):
#     if s[end] == 'F':
#         cf += 1
#     if s[end] == 'L':
#         cl += 1
#     while cf > 3 or cl > 3: # !!!!!!!!!!!!!!!!!!!!!!!!!!!
#         if s[start] == 'F':
#             cf -= 1
#         if s[start] == 'L':
#             cl -= 1
#         start += 1
#     if cf == 3 and cl == 3:
#         mx = max(mx, end + 1 - start)
# print(mx)
# # 292

# 2 решение:
# f = open("Файлы к задачам/24_18__3b9tx.txt")
# s = f.readline()
#
# mx = 0
# for i in range(len(s)):
#     for j in range(mx + i, len(s)):
#         t = s[i:j + 1]
#         if t.count('F') == 3 and t.count('L') == 3:
#             mx = max(mx, len(t))
#         if t.count('F') > 3 or t.count('L') > 3:
#             break
# print(mx)
# # 292


'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/29327'''

# 1
# f = open("Файлы к задачам/24-5__8ag1l.txt")
# s = f.readline()
# ans = 0
#
# for start in range(len(s)):
#     if s[start] == 'B':
#         c = 0
#         for end in range(start + 1, len(s)):
#             if s[end] in '13579':
#                 c += 1
#             if s[end] in 'AEIOU':
#                 break
#             if c == 15:
#                 ans += 1
# print(ans)
# # 94

# 4.1
# f = open("Файлы к задачам/24__7h75n.txt")
# s = f.readline()
#
# ca = cb = start = mx = 0
#
# for end in range(len(s)):
#     if s[end] == 'A':
#         ca += 1
#     if s[end] == 'B':
#         cb += 1
#     while cb > 2 or ca > 2:
#         if s[start] == 'A':
#             ca -= 1
#         if s[start] == 'B':
#             cb -= 1
#         start += 1
#
#     if ca <= 2 and cb <= 2:
#         mx = max(mx, end - start + 1)
# print(mx)
# # 222


# 4.2
# f = open("Файлы к задачам/24__7h75n.txt")
# s = f.readline()
# mx = 0
#
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j + 1]
#         if t.count('A') > 2 or t.count('B') > 2:
#             break
#         if t.count('A') <= 2 and t.count('B') <= 2:
#             mx = max(mx, len(t))
# print(mx)
# # 222


'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/30078'''


# 1
# Решение 1. Указатели:
# f = open("Файлы к задачам/24__7h77f.txt")
# s = f.readline()
# start = cc = cd = mx = 0
# for end in range(len(s)):
#     if s[end] == 'C':
#         cc += 1
#     if s[end] == 'D':
#         cd += 1
#     while cc > 2 or cd > 2:
#         if s[start] == 'C':
#             cc -= 1
#         if s[start] == 'D':
#             cd -= 1
#         start += 1
#     if cc <= 2 and cd <= 2:
#         mx = max(mx, end + 1 - start)
# print(mx)
# # 253

# Решение 2. Циклы:
# f = open("Файлы к задачам/24__7h77f.txt")
# s = f.readline()
# mx = 0
# for i in range(len(s)):
#     for j in range(i + mx, len(s)):
#         t = s[i:j + 1]
#         if t.count('C') > 2 or t.count('D') > 2:
#             break
#         if t.count('C') <= 2 and t.count('D') <= 2:
#             mx = max(mx, len(t))
# print(mx)
# # 253

# ----------------------------------------------------------------------------------------------------------------------

# 2
# f = open("Файлы к задачам/24__7h6ti.txt")
# s = f.readline()
# cu = cv = cw = cx = cy = cz = start = mx = 0
# for end in range(len(s)):
#     if s[end] == 'U':
#         cu += 1
#     if s[end] == 'V':
#         cv += 1
#     if s[end] == 'W':
#         cw += 1
#     if s[end] == 'X':
#         cx += 1
#     if s[end] == 'Y':
#         cy += 1
#     if s[end] == 'Z':
#         cz += 1
#     while max(cu, cv, cw, cx, cy, cz) > 100:
#         if s[start] == 'U':
#             cu -= 1
#         if s[start] == 'V':
#             cv -= 1
#         if s[start] == 'W':
#             cw -= 1
#         if s[start] == 'X':
#             cx -= 1
#         if s[start] == 'Y':
#             cy -= 1
#         if s[start] == 'Z':
#             cz -= 1
#         start += 1
#     if max(cu, cv, cw, cx, cy, cz) <= 100:
#         mx = max(mx, end + 1 - start)
# print(mx)
# # 2844

# ----------------------------------------------------------------------------------------------------------------------

# 3
# f = open("Файлы к задачам/24_M3__42ngp.txt")
# s = f.readline()
# first_eq = 'ABCDEFGHIJKLM'
# second_eq = 'NOPQRSTUVWXYZ'
# cf = cs = cdot = start = mx = 0
#
# for end in range(len(s)):
#     if s[end] == '.':
#         cdot += 1
#     if s[end] in first_eq:
#         cf += 1
#     if s[end] in second_eq:
#         cs += 1
#
#     while cdot >= 4: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         if s[start] == '.' and cf > cs:
#             mx = max(mx, end + 1 - start)
#         if s[start] == '.':
#             cdot -= 1
#         if s[start] in first_eq:
#             cf -= 1
#         if s[start] in second_eq:
#             cs -= 1
#         start += 1
# print(mx)
# # 378


