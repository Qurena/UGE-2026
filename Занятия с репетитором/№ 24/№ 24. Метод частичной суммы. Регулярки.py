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

# from re import *
# f = open('../!Файлы для задач/24dtwwe.txt')
# s = f.readline()
# s = s.replace('RSQ', 'AAA')
# pattern = r"(?=(AAA([FGQRSW]*AAA){129}[Q]*[^Q]))"
#
# mn = 10**10
# for i in finditer(pattern, s):
#     g = i.group(1)
#     mn = min(mn, len(g))
# print(mn)
# # 497


# 3
'''https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=8840'''

# f = open("../!Файлы для задач/24-371.txt")
# s = f.readline()
# c = 0
# s = s.split('.')
#
# for el in s:
#     d = [i for i in el]
#     if d[-1] == ' ':
#         s.remove(el)
# for el in s:
#     f = el.split(' ')
#     for k in f:
#         if k == '':
#             f.remove(k)
#
#     w = [len(i) for i in f]
#
#     for i in range(0, len(w), -1):
#         f = 1
#         while f == 1:
#             if w[i]


# 4
'''https://education.yandex.ru/ege/inf/training/24/task/1?examTaskId=083910a9-6d5d-45d9-bfe6-1ae5a008abf2&examTaskNumber=24&taskId=a24ce8b0-6d3c-4963-af6e-dfbc118b2d1c&categoryId=34289ff9-4b4d-4d32-8378-b44d98d85090'''

# from re import *
# f = open('../!Файлы для задач/24-1_1759952073.txt')
# s = f.readline()
#
# pattern = r'[02468]([^S02468]*S){35}[^S02468]*'
# mx = 0
# for i in finditer(pattern, s):
#   g = i.group(0)
#   mx = max(mx, len(g))
# print(mx)
# # 292







