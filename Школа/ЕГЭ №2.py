'''# 7912
print('x y w z')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = not( ((not(x)) or y) and (not(w))) or not(z and (not(y and w)))
                if F == 0:
                    print(x, y, w, z)

#yxwz'''

'''
Алгоритм решения для заданий с неоднозначным F:
1. Если значения F не одинаковые (таблица a,b,c,F),
тогда мы выводим всю таблицу и смотрим на строки со значением F,
которое встречается реже всего.
2. Немножко думаем и получаем ответ)
'''

# Тест 2 - Таблицы истинности логической функции (https://kpolyakov.spb.ru/school/egetest/b2.htm)

'''
# 1 вид

print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (not(z)) and x or x and y
            print(x, y, z, F)

# zyx


# 2 вид

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (y and z or y and (not(w)) or (not(w)) and (not(z)))
                if F == 1:
                    print(x, y, z, w)
# ywzx                   
'''

'''
print('a b c d F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = ((not(a)) <= b) and (b == (not(c)) and (not(d)))
                if F == 1:
                    print(a, b, c, d, int(F))

#b a c d
'''