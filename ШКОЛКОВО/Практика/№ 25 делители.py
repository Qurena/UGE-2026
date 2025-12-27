"""Решения 25-ых задач"""
# 1
'''
Среди целых чисел, принадлежащих числовому отрезку [182635;453733],
найдите числа, которые представляют собой
произведение двух различных простых делителей,
не считая единицы и простого числа. Запишите в ответе через
пробел количество таких чисел и сумму минимального и максимального из них.


def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return x != 1


ans = []

for x in range(182_635, 453_733 + 1):
    flag = 0
    for i in range(2, int(x ** 0.5) + 1):
        if (x % i == 0) and prime(i) and prime(x // i) and (i != x // i):
            flag = 1
            break

    if flag == 1:
        ans.append(x)

print(len(ans), max(ans) + min(ans))
# 57221 636366
'''

# 2
def prime(x: int) -> bool:
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return x > 1

def count(x: int) -> list[int]:
    div = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            div.append(i)
            div.append(x//i)
    if div == []:
        return [0]
    return div


for x in range(650_001, 655_000):
    if prime(max(count(x))) == False:
        print(x, max(count(x)))
