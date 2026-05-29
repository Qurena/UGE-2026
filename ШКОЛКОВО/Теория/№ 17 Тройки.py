""" 12 марта.
Конспект к вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/37103"""

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ДВА РАЗЛИЧНЫХ ЭЛЕМЕНТА ПОСЛЕДОВАТЕЛЬНОСТИ != ДВА РАЗЛИЧНЫХ ЧИСЛА
то есть индексы должны быть различные, а что внутри - не имеет значения. 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

В решении этого номера мы будем часто использовать генераторы (например, sum(1 for i in t if abs(i) % 100 == 34) )
'''

# 2 | Тройка
# f = open("../Практика/Файлы к задачам/17_2024__7bymt.txt")
# a = [int(i) for i in f]
# mx13 = max(i for i in a if abs(i) % 100 == 13) # исполь-м abs(i), так как оператор % работает с отрицательными числами по-другому
#
# c = mx = 0
# for i in range(len(a) - 2):
#     t = a[i:i+3]
#     correct = sum(1 for el in t if len(str(abs(el))) == 3)
#     if correct == 2 and sum(t) <= mx13:
#         c += 1
#         mx = max(mx, sum(t))
# print(c, mx)
# # 959 97471


# 4 | Четверка
# f = open("../Практика/Файлы к задачам/17_1__8cp34.txt")
# a = [int(i) for i in f]
# mx23 = max(i for i in a if abs(i) % 100 == 23)
#
# c = mx = 0
# for i in range(len(a) - 3):
#     t = a[i:i+4]
#     plus = sum(1 for i in t if i > 0)
#     minus = sum(1 for i in t if i < 0)
#     if sum(t) > mx23 and plus == minus:
#         c += 1
#         mx = max(mx, sum(t))
# print(c, mx)
# # 140 8291


# 5 | Семерка
# from math import *
# f = open("../Практика/Файлы к задачам/17_3__8cu84.txt")
# a = [int(i) for i in f]
#
# def odd(x):
#     s = [int(i) for i in str(abs(x))]
#     f = True
#     for el in s:
#         if el in [0, 2, 4, 6, 8]:
#             f = False
#     return f
#
# def even(x):
#     s = [int(i) for i in str(abs(x))]
#     f = True
#     for el in s:
#         if el in [1, 3, 5, 7, 9]:
#             f = False
#     return f
#
# mx = c = 0
# for i in range(len(a) - 6):
#     t = a[i:i+7]
#     odds = sum(1 for i in t if odd(i))
#     evens = sum(1 for i in t if even(i))
#     if prod(t) % 23 == 0 and odds > evens:
#         c += 1
#         mx = max(mx, max(t) - min(t))
# print(c, mx)
# # 367 49348