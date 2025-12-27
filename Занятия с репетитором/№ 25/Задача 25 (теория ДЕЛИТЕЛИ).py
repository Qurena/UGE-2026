"""Здесь располагается теория по №25: Решето Эратосфена и поиск простых делителей N"""

# РЕШЕТО ЭРАТОСФЕНА - поиск делителей числа с интервала [start; end], больших 1
'''
start = _
end = _

d = {}
for num in range(start, end + 1):
    d[num] = []

for div in range(2, end//2 + 1): # ЕСЛИ МЫ ХОТИМ УБРАТЬ САМО ЧИСЛО ИЗ СПИСКА ДЕЛИТЕЛЕЙ, ЗАМЕНЯЕМ end//2 + 1 на int(end**0.5) + 1
    for num in range(start // div * div, end + 1, div):  # Либо мы получим start, либо ближайшее четное число к start)
        if num in d:
            d[num].append(div)
            # d[num] += [div]
'''

# ПОИСК ПРОСТЫХ ЧИСЕЛ ДО N И ПРОСТЫХ ДЕЛИТИЛЕЙ N
'''
# Вводится число n.
# a) Вывести все простые числа до n
# b) Вывести список простых делителей числа n

n = int(input())

def find_primes(n: int) -> list[int]:
  primes = []
  d = [True] * n # Индексы - сами числа от 0 до N - 1
  d[0] = False
  d[1] = False
  for i in range(2, n):
    if d[i] == True:
      primes.append(i)
    for num in range(i * 2, n, i): # вычеркиваем числа от div*2 до N - 1 с шагом div
      d[num] = False
  return primes

primes_list = find_primes(n)
def prime_divs(n: int) -> list:
    divs = []
    for div in primes_list:
      if div >= n:
        break
      if n % div == 0:
        divs.append(div)
    return divs

print(find_primes(n)) # Список простых чисел от 2 до n

print(prime_divs(n)) # Список простых делителей числа n
'''

