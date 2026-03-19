"""12 марта, 19 марта"""


# 1
'https://education.yandex.ru/ege/inf/task/37e7362a-fc21-4cc7-acb1-3859dde6d2ef'
# f = open("")
# s = f.readline()
#
# digits = []
# letters = []
#
# # заполним списки, сколько цифр и букв располагается в строке s[:i+1]
# count_d, count_l = 0, 0
# for l in s:
#     if l in '123':
#         count_d += 1
#     else:
#         count_l += 1
#     digits.append(count_d)
#     letters.append(count_l)
#
# max_len = 0
# # создаем скользящее окно
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if 2 * (digits[j + 1] - digits[i]) == letters[j + 1] - letters[i]:
#             max_len = max(max_len, j - i + 1)
# print(max_len)
# # 333


# 2
'''https://alex-math.ru/gia/zadaniye-24-informatika-yege-yegkr-19042025'''

from re import *
f = open('../!Файлы для задач/24dtwwe.txt')
s = f.readline()
s = s.replace('RSQ', 'AAA')
pattern = r"(?=(AAA([FGQRSW]*AAA){129}[Q]*[^Q]))"

mn = 10**10
for i in finditer(pattern, s):
    g = i.group(1)
    mn = min(mn, len(g))
print(mn)
# 497





