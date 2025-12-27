# 2
'''
print('x y w z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = y or (x and w) or (w == z)
                if F == 0:
                    print(x, y, w, z)
# ОТВЕТ: zxyw
'''

# 5
'''
def third(n: int) -> str:
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

def answer(n: int) -> int:
    s = third(n)
    if '2' in s:
        s += '0'
    else:
        last_dig = n % 10
        new = last_dig // 2
        s += third(new)
    return int(s, 3)

a = set()
for n in range(1, 1000):
    if answer(n) >= 202:
        a.add(answer(n))
print(min(a))
# ОТВЕТ: 204
'''

# 8
'''
def fith(n: int) -> str:
    s = ''
    while n != 0:
        s += str(n % 5)
        n //= 5
    return s[::-1] if len(s) == 5 else 0

def thr(n: list) -> bool:
    s = True
    for q in range(len(n)):
        if n[q] == 3:
            s = False
    return s

def oe(n: list) -> bool:
    s = True
    for q in range(len(n)):
        if q != len(n) - 1:
            if (n[q] % 2 == 0 and n[q+1] % 2 == 0) or (n[q] % 2 != 0 and n[q+1] % 2 != 0):
                s = False
    return s



a = 0
for i in range(1, 1_000_000):
    if fith(i) != 0:
        F = [int(k) for k in fith(i)]
        if thr(F) and oe(F):
            a += 1
print(a)

# ОТВЕТ: 27
'''


# 12
'''
for n in range(6, 1000):
    s = '3' + '1' * n
    while '31' in s or '11111' in s or '144' in s:
        if '31' in s:
            s = s.replace('31', '4', 1)
        if '11111' in s:
            s = s.replace('11111', '33', 1)
        if '144' in s:
            s = s.replace('144', '133', 1)
    k = sum(int(i) for i in s)
    if k == 160:
        print(n)

# ОТВЕТ: 135
'''


# 14
'''d = []
for x in range(0, 17):
    a = '0123456789ABCDEFG'
    s1 = '370' + a[x] + '102'
    k1 = int(s1, 17)
    s2 = '8' + a[x] + '3719'
    k2 = int(s2, 17)

    if (k1 + k2) % 11 == 0:
        d.append(int(a[x], 17))

p = max(d)
a = '0123456789ABCDEFG'
s1 = '370' + a[p] + '102'
k1 = int(s1, 17)
s2 = '8' + a[p] + '3719'
k2 = int(s2, 17)
print((k1 + k2) / 11)

# ОТВЕТ: 8633247'''
# БОЛЕЕ ПРОСТОЕ РЕШЕНИЕ:
'''
# Перебираем все возможные цифры x в 17-ричной системе
for x in "0123456789ABCDEFG":
    # Преобразуем первое число $370x102_{17}$ в десятичную систему
    s1 = int("370"+x+"102", 17)
    # Преобразуем второе число $8x3719_{17}$ в десятичную систему
    s2 = int("8"+x+"3719", 17)
    # Вычисляем сумму двух чисел
    s = s1 + s2
    # Проверяем, делится ли сумма на 11
    if s % 11 == 0:
        # Если делится, выводим текущее значение x и частное от деления суммы на 11
        print(x, s // 11)
        '''


# 16
'''
def F(n):
    if n < 100:
        return 5 + n + F(n+2)
    return n + 2

print(F(90) - F(101))

# ОТВЕТ: 494
'''

# 23
'''
def ans(start: int, end: int) -> int:
    d = {}

    for key in range(start, end + 1):
        d[key] = 0

    d[start] = 1

    if 12 in d:
        del d[12]

    for key in d.keys():
        if key + 1 in d:
            d[key + 1] += d[key]
        if key * 2 in d:
            d[key * 2] += d[key]
    return d[end]

print(ans(3, 18) * ans(18, 55))

# ОТВЕТ: 88
'''
# РЕШЕНИЕ ЧЕРЕЗ РЕКУРСИЮ:
'''
def f(a, b): # Функция для подсчета количества программ преобразования a -> b
    # Если число больше целевого или равно запрещённому 12, то есть нарушено условие задачи
    if a > b or a == 12:
        return 0
    # Если дошли до целевого числа, то есть получили подходящую траекторию
    if a == b:
        return 1
    # В остальных случаях, считаем все возможные переходы
    return f(a+1, b) + f(a*2, b)
# Вычисляем и выводим ответ, учитывая условие: траектория проходит через 18
print(f(3, 18) * f(18, 55))
'''

# 25
'''
start = 10_000
end = 15_000


def find_divs(n) -> list[int]:
    divs = []
    for i in range(2, n):
        if n % i == 0:
            divs += [i]
    return divs if divs else [0]



c = 0
for n in range(start, end + 1):
    if c != 5:
        if (int(find_divs(n)[0]) + int(find_divs(n)[-1])) % 256 == 6:
            print(n, int(find_divs(n)[0]) + int(find_divs(n)[-1]), sep=' ', end=' ')
            c += 1
    if c == 5:
        break
        
# ОТВЕТ: 10248 5126 10760 5382 10761 3590 11209 1030 11272 5638
'''
# ВТОРОЙ СПОСОБ РЕШЕНИЯ:
'''
c = 0
for i in range(10001, 15000):
    ds = set() # Создаём множество для хранения делителей
    # Пройдёмся по всем делителям, кроме 1 и самого числа. До корня мы сможем найти все возможные делители максимально быстро.
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0: # Если число является делителем
            ds.add(d) # Добавим в множество
            ds.add(i // d) # Найдём и добавим парный делитель в множество
    # Делаем из множества отсортированный список,
    # чтобы можно было по индексам найти делители
    ds = sorted(list(ds))
    # Если сумма наименьшего и наибольшего делителя при делении на 256 даёт остаток 6
    # И было найдено более одного делителя, чтобы был максимальный и минимальный
    if len(ds) > 1 and (ds[0] + ds[-1]) % 256 == 6:
        c += 1 # Увеличим счётчик
        print(i, ds[0]+ds[-1]) # Выводим само число и сумму делителей
    # Если уже накопилось 5 чисел, то прерываем цикл
    if c == 5:
        break
'''
