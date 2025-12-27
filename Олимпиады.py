'''import matplotlib.pyplot as plt
# Генерация случайных данных для прибыли компании за 5 лет
profit = [1.5, 1.9, 2.7, 2.2, 2.8]

# Создание графика
fig, ax2 = plt.subplots(figsize=(6, 4))

# Настройка графика
ax2.plot(profit, color='darkgreen')
ax2.set_title('Динамика прибыли компании за 2016–2020 гг. (млн рублей)')
ax2.set_xlabel('Год')
ax2.set_ylabel('Прибыль (млн рублей)')
ax2.set_xticks(range(len(profit)))
ax2.set_xticklabels(['2016', '2017', '2018', '2019', '2020'])
# Искусственное завышение диапазона оси OY от 1.3 до 3 млн
# Если этого не сделать – данные по последнему столбцу будут выше
# границы графика
ax2.set_ylim(1.3, 3)

# Добавление значений прибыли на графике
for i, txt in enumerate(profit):
    ax2.annotate(f'{txt:.1f}', (i, profit[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()
'''

'''
from math import factorial
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            if x != y and x != z and y != z:
                if (factorial(x) + factorial(y) + factorial(z)) % 10 == 7:
                    print(x, y, z)
'''


'''
from sys import *

setrecursionlimit(10000)

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci_iterative(2024))
'''





