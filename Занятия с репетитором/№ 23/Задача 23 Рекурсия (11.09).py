# Решение с помощью рекурсии (затронется в теории игр)

'''

https://education.yandex.ru/ege/task/39eeb25c-0466-483b-a006-f54308098120

def next_steps(start):
    return (start + 1, start + 2, start * 2)

print(next_steps(4)) # мы проверяем, правильно ли записаны команды

def count(start: int, end: int) -> int:

    # УСЛОВИЯ ОСТАНОВКИ
    if start == end:
        return 1

    if start > end:
        return 0

    if start == 8:
        return 0

    return count(start + 1, end) + count(start + 2, end) + count(start * 2, end)

print(count(3, 14) * count(14, 18))

18 
17 (+1) 16 (+2) 9 (*2)
16 (+1) 15(+2) -(*-) | 15(+1) 14(+2) 8(*2) | 8(+1) 7(+2) -(*-) 

'''

'''
Исполнитель преобразует число на экране. У исполнителя есть три команды, которым присвоены буквы 
латинского алфавита:

A. Вычесть 1
B. Найти целую часть от деления на 3
C. Найти целую часть от деления на 4

Программа для исполнителя — это последовательность команд.

Сколько программ преобразуют число 2025 в число 25, при этом их траектория вычислений содержит число 250,
но не содержит 42?

Траектория вычислений программы — это последовательность результатов выполнения всех команд программы. Например,
для программы ACB при исходном числе 250 траектория состоит из чисел 249, 83, 20.

# Рекурсия
def count(start: int, end: int) -> int:
    if start == end:
        return 1

    if start < end:
        return 0

    if start == 42:
        return 0

    return count(start -1, end) + count(start // 3, end) + count(start // 4, end)

print(count(2025, 250) * count(250, 25))
'''

# Примеры задач:
# 1
'''
Ходы:
1. + 1
2. * 2
Из числа 1 в 30, без 10.
'''
# def count(start, end):
#     if start == end: # если start совпал с end, это нам подходит
#         return 1
#
#     if start > end: # условие перескока
#         return 0
#
#     if start == 10:
#         return 0
#
#     return count(start + 1, end) + count(start * 2, end) # двигаем start к end
#
# print(count(1, 30))
# # 68


# 2
'''
Ходы:
1. + 3
2. * 3
Начинаем с 10, сколько нечетных чисел, меньших 100, существует?
'''

# res = set()
# def count(start):
#     if start < 100:
#         if start % 2 != 0:
#             res.add(start)
#     else:
#         return # точка завершения рекурсии
#
#     count(start + 3)
#     count(start * 3)
#
# count(10)
# print(len(res))
# # 27


# 3
'''
Ходы:
1. + 1
2. + 2
3. * 3
Сколько нечетных чисел можно получить, начиная с 4, используя не более 3-х команд?
'''

# values = [4]
#
# for _ in range(3):
#     new_values = set()
#     for value in values:
#         new_values.add(value + 1)
#         new_values.add(value + 2)
#         new_values.add(value * 3)
#     values = new_values
#
# ans = 0
# for v in values:
#     if v % 2 == 0:
#         ans += 1
# print(ans)
# # 11


# 4 | ДО 3 команд, исходное число 4,
'''
Ходы:
1. + 1
2. + 2
3. * 3
Сколько существует программ, состоящих не более чем из 3 команд, для которых при исходном числе 4 результатом является четное число.
'''

# def count(start, r):
#     if r == 0: # если мы сделали 3 хода
#         if start % 2 == 0: # и достигли четного числа
#             return 1 # выводим единичку
#         else:
#             return 0
#
#     return count(start + 1, r - 1) + count(start + 2, r - 1) + count(start * 3, r - 1)
#
# # Если ходов 0 и начальное число, то этот вариант нам подходит. Поскольку команд до 3-х, суммируем функции с r = 0, 1, 2, 3
# print(count(4, 0) + count(4, 1) + count(4, 2) + count(4, 3))
# # 22


# 5
'''
Ходы:
1. + 2
2. * 3
Сколько чисел можно получить с помощью программы из 4 команд при исходном числе 1.
'''

# def count(start, r):
#     if r == 0:
#         return {start}
#
#     return count(start + 2, r - 1) | count(start * 3, r - 1) # объединяем множества, каждое из которых {start}
#
# print(len(count(1, 4)))
# # 8


# 6
'''
Ходы:
1. + 2
2. + 5
3. * 2
Сколько существует программ из 8 в 40, а последняя команда первая или вторая?
'''
# def count(start, end, cmd):
#     if start == end:
#         if cmd != 3:
#             return 1
#         return 0
#
#     if start > end:
#         return 0
#
#     return count(start + 2, end, 1) + count(start + 5, end, 2) + count(start * 2, end, 3)
#
# print(count(8, 40, 0))
# # 409


# 7
'''
Ходы:
1. + 2
2. + 5
3. * 2
Сколько существует программ из 8 в 40, а последние 3 команды это 1.2.1.?
'''

# def count(start, end, cmd):
#     if start == end and cmd[-3:] == [1, 2, 1]:
#         return 1
#
#     if start > end:
#         return 0
#
#     return (count(start + 2, end, cmd + [1]) +
#             count(start + 5, end, cmd + [2]) +
#             count(start * 2, end, cmd + [3]))
#
# print(count(8, 40, []))
# # 59


# 8
'''
Ходы:
1. - 3
2. смена десятков и единиц, если единицы меньше десятков
Сколько существует программ из 43 в 13?
'''

# def count(start, end):
#     if start == end:
#         return 1
#
#     if start < end:
#         return 0
#
#     res = count(start - 3, end)
#     if start % 10 < start // 10:
#         res += count(int(str(start % 10) + str(start // 10)), end)
#
#     return res
#
# print(count(43, 13))
# # 4


# 9 !!! Новое условие
'''
Ходы:
1. - 1
2. * 2
3. * 3
Сколько существует программ из 3 в 15 и не содержат двух команд 1. подряд?
'''
# def f(start, end, cA):
#     if start > end + 1: # !!!!!!!!!!!!!!!!!!!! так как из 16 мы можем прийти в 15 (16 - 1 = 15)
#         return 0
#     if start == end and cA != 2:
#         return 1
#
#     if cA == 1:
#         return f(start * 2, end, 0) + f(start * 3, end, 0)
#
#     return f(start - 1, end, cA + 1) + f(start * 2, end, cA) + f(start * 3, end, cA)
#
# print(f(3, 15, 0))
# # 6