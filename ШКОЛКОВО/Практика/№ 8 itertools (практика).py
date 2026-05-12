'''Решения задач'''

'''
---------------------------------------------------------------------------
Арез составляет шестибуквенные слова из букв слова НАКОВАЛЬНЯ.
Каждая буква может встречаться в слове только один раз, на первом месте не
может стоять буква Ь, а буква Л может стоять только в окружении гласных.
Сколько слов может составить Арез?
---------------------------------------------------------------------------

from itertools import *

a = set('НАКОВАЛЬНЯ')
c = 0

bad = ['ЛН', 'ЛК', 'ЛВ', 'ЛЬ', 'НЛ', 'КЛ', 'ВЛ', 'ЬЛ']  # Список запрещённых сочетаний букв

for i in permutations(a, r=6):  # Перебираем все возможные перестановки из 6 букв слова a
    s = ''.join(i)  # Склеиваем буквы в слово

    t = [not j in s for j in bad]  # Проверяем, что ни одно запрещённое сочетание не встречается в слове
    if (s[0] != 'Ь') and all(t) and (s[0] != 'Л') and (s[-1] != 'Л'):
        c += 1
print(c)

# 5544
'''

# 2
'''
---------------------------------------------------------------------------
Определите количество шестеричных пятизначных чисел,
в записи которых не менее двух цифр 5 и не более трёх нечетных цифр,
меньших 4.
---------------------------------------------------------------------------

from itertools import *

a = '012345'
c = 0

for i in product(a, repeat=5):
    s = ''.join(i)

    if s[0] != '0' and s.count('5') >= 2 and ((s.count('1') + s.count('3')) <= 3):
        c += 1
print(c)

#1355
'''

# 3
'''
---------------------------------------------------------------------------
Гоша составляет восьмизначные числа. Причём рядом не должны стоять цифры с
одинаковым остатком от деления на 5, а также на последнем месте может быть только чётная цифра.
Сколько чисел может составить Гоша?
---------------------------------------------------------------------------
from itertools import *


bad = ['05', '16', '27', '38', '49', '50', '61', '72', '83', '94', '00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
c = 0

for i in product('0123456789', repeat=8):
    s = ''.join(i)
    t = [not k in s for k in bad]
    if s[0] != '0' and s[-1] in '02468' and all(t):
        c += 1
print(c)

# 9437184
'''

# 4
'''
---------------------------------------------------------------------------
Демид составляет пятибуквенные слова из букв КРОВАТЬ, содержащие букву Р,
но не более четырех раз. Остальные буквы не могут повторяться.
Сколько различных слов может составить Демид?
---------------------------------------------------------------------------

from itertools import *

a = set('КРОВАТЬ')
c = 0

for i in product(a, repeat=5):
    s = ''.join(i)
    if 1 <= s.count('Р') <= 4 and all(s.count(i) == 1 for i in s if i != 'Р'):
        c += 1

print(c)

# 3330
'''

# 5
'''
---------------------------------------------------------------------------
Максим составляет 5-буквенные слова перестановкой букв слова САПОГ.
При этом в слове не могут стоять рядом две гласные и две согласные буквы.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько слов может составить Максим?
---------------------------------------------------------------------------

from itertools import *

a = set('САПОГ')
bad = ['АА', 'АО', 'ОА', 'ОО', 'СС', 'ПП', 'ГГ', 'СП', 'ПС', 'ПГ', 'ГП', 'СГ', 'ГС']
c = 0

for p in permutations(a, 5):
    s = ''.join(p)
    t = [not k in s for k in bad]

    if all(t):
        print(s)
        c += 1

print(c)

# 12
'''

# 6
'''
---------------------------------------------------------------------------
Сколько слов из шести символов может составить Петя перестановкой букв слова БАОБАБ?
---------------------------------------------------------------------------

from itertools import *

a = set('БАОБАБ')
c = 0

for i in product(a, repeat=6):
    s = ''.join(i)
    if s.count('Б') == 3 and s.count('А') == 2 and s.count('О') == 1:
        print(s)
        c += 1

print(c)

# 60
'''

# from itertools import *
#
# a = 'МАШИН'
# c = 0
# q = set()
#
# for i in permutations(a):
#     s = ''.join(i)
#     if s[0] not in 'НСТ':
#         q.add(s)
# print(len(q))

"""ДЗ: https://3.shkolkovo.online/my/course/7259/dz/28533"""

# 2
# from itertools import *
# s = 'ПРОГА'
# ans = set()
# for i in product(s, repeat=5):
#     g = ''.join(i)
#     if g.count('Г') <= 2:
#        ans.add(g)
# print(len(ans))
# # 2944


# 3
# from itertools import *
# s = 'КВАС'
# ans = set()
# for i in product(s, repeat=6):
#     g = ''.join(i)
#     if g.count('А') == 1:
#        ans.add(g)
# print(len(ans))
# # 1458


# 4
# from itertools import *
# s = 'ЖАСМИН'
# ans = set()
# for i in product(s, repeat=5):
#     g = ''.join(i)
#     if g.count('М') >= 2:
#        ans.add(g)
# print(len(ans))
# # 1526


# 5
# from itertools import *
# s = 'ЖЕМЧУГ'
# ans = set()
# for i in product(s, repeat=6):
#     g = ''.join(i)
#     if g.count('Ч') == 2:
#        ans.add(g)
# print(len(ans))
# # 9375


# 6
# from itertools import *
# s = 'ПАРЕК'
# ans = set()
# bad = ['ПР', 'РП', 'КР', 'РК', 'КП', 'ПК', 'АЕ', 'ЕА']
# for i in permutations(s):
#     g = ''.join(i)
#     flag = 1
#     for el in bad:
#         if el in g:
#             flag = 0
#     if flag == 1:
#         ans.add(g)
# print(len(ans))
# # 12


# 7
# from itertools import *
# s = 'КАПКАН'
# ans = set()
# bad = ['КК', 'АА']
# for i in permutations(s):
#     g = ''.join(i)
#     flag = 1
#     for el in bad:
#         if el in g:
#             flag = 0
#     if flag == 1:
#         ans.add(g)
# print(len(ans))
# # 84


# 8
# from itertools import *
# s = 'АНДРЕЙ'
# ans = set()
# for i in product(s, repeat=7):
#     g = ''.join(i)
#     if g.count('А') == 1 and g.count('Й') == 1 and g[0] != 'Й':
#         ans.add(g)
# print(len(ans))
# # 36864


# 9
# from itertools import *
# s = 'ПОЧЕМУ'
# ans = set()
# for i in product(s, repeat=9):
#     g = ''.join(i)
#     if g.count('П') <= 6:
#         ans.add(g)
# print(len(ans))
# # 10076750


# 10
# from itertools import *
# s = 'ТАРУХ'
# ans = set()
# bad = ['ТР', 'РТ', 'ТХ', 'ХТ', 'АУ', 'УА', 'РХ', 'ХР']
# for i in permutations(s):
#     g = ''.join(i)
#     flag = 1
#     for el in bad:
#         if el in g:
#             flag = 0
#     if flag == 1:
#         ans.add(g)
# print(len(ans))
# # 12


'-----------------------------------------------------------------------------------------------------------------------'

# 1
# from itertools import *
#
# s = 'ИСКАНДЕР'
#
# ans = 0
# for i in product(s, repeat=6):
#     g = ''.join(i)
#     glscnt = sum(1 for el in g if el in 'ИАЕ')
#     if glscnt == 1 and (g[0] in 'ИАЕ' or g[-1] in 'ИАЕ'):
#         st = set([el for el in g])
#         if len(st) == len([el for el in g]):
#             ans += 1
# print(ans)
# # 720