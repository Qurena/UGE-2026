""" Теория по решению задач № 19-21"""

# РЕШЕНИЕ номера 19
'''
# https://education.yandex.ru/ege/inf/task/4eca9f6e-1537-425f-94ef-3c3f3851b73d

def next_steps(p):
  return p + 7, p * 3

def play(p, remaining): # remaining - шаги до победы
  if p >= 342 and remaining == 0:  # условие победы (если количество камней уменьшается - p <= 342)
    return True

  if p >= 342 and remaining == 1:  # условие поражения, так как остался еще 1 ход, а кол-во камней уже победное
    return False

  if remaining == 0: # условие поражения (ходы кончились, а кол-во камней в кучке не выигрышное
    return False

  next_plays = []
  for step in next_steps(p):
    next_plays.append(play(step, remaining - 1))

  # next_plays = [play(step, remaining - 1) for step in next_steps(p)]


  if remaining - 1 == 1: # Петя (когда (remaining - 1) % 2 == 0)
    # Первый ход Пети
    return all(next_plays) # Здесь all выдает True только тогда, когда ВСЕ ходы выигрышные (True)
                           # Каждый ход Пети не приводит к выполнению условий

  # Победная ситуация - ВСЕГДА any
  if remaining - 1 == 0: # Всегда у победителя должен быть выигрышный ход
    # Первый ход Вани (но здесь не всегда Ваня - зависит от игры)
    return any(next_plays) # Здесь any выдает True из хотя бы одного True
                           # (если есть ХОТЯ БЫ ОДИН выигрышный ход - тогда True)

# Если в условии написано, что есть такой ход Вани, при котором он выиграет после любого хода Пети, то
# пишем all на Петю (так как ПРИ ЛЮБОМ ХОДЕ ПЕТИ) и any на Ваню (так как ЕСТЬ ХОТЯ БЫ ОДИН ТАКОЙ ХОД У ВАНИ).


for s in range(1, 301):
  if play(s, 2):
    print(s)
'''



# РЕШЕНИЕ номера 20
'''
def next_steps(p):
  return p + 7, p * 3

def play(p, remaining): # remaining - шаги до победы
  if p >= 342 and remaining % 2 == 0:  # условие победы (если количество камней уменьшается - p <= 342)
    return True                    # для номера 21 пишем (remaining == 0 or remaining == 2)

  if p >= 342 and remaining % 2 != 0:  # условие поражения, так как остался еще 1 ход, а кол-во камней уже победное
    return False                   # для номера 21 пишем (remaining == 1 or remaining == 3)

  # Совместили верхние условия
  # if p >= 342:
  #   return remaining % 2 == 0

  if remaining == 0: # условие поражения (ходы кончились, а кол-во камней в кучке не выигрышное
    return False

  next_plays = []
  for step in next_steps(p):
    next_plays.append(play(step, remaining - 1))

  # next_plays = [play(step, remaining - 1) for step in next_steps(p)]

  if remaining - 1 == 3:
    return all(next_plays)

  if remaining - 1 == 2: # remaining - 1 чётный у ПОБЕДИТЕЛЯ
    return any(next_plays)

  if remaining - 1 == 1:
    # Первый ход Пети
    return all(next_plays) # Здесь all выдает True только тогда, когда ВСЕ ходы выигрышные (True)
                           # Каждый ход Пети не приводит к выполнению условий

  if remaining - 1 == 0: # Победитель (Ваня)
    # Первый ход Вани
    return any(next_plays) # Здесь any выдает True из хотя бы одного True
                           # (если есть ХОТЯ БЫ ОДИН выигрышный ход - тогда True)

# Если в условии написано, что есть такой ход Вани, при котором он выиграет после любого хода Пети, то
# пишем all на Петю (так как ПРИ ЛЮБОМ ХОДЕ ПЕТИ) и any на Ваню (так как ЕСТЬ ХОТЯ БЫ ОДИН ТАКОЙ ХОД У ВАНИ).
# При этом в номере 20 и 21 мы добавляем условия сверху (remaining - 1 == 2, 3, и тд). В таком случае мы
# НЕ МОЖЕМ писать разные функции (any или all) у условий на одного человека:
#   if remaining - 1 == 2:
#     return any(next_plays) # мы не можем написать здесь all
#
#   if remaining - 1 == 1:
#     return all(next_plays)
#
#   if remaining - 1 == 0:
#     return any(next_plays) # any ВСЕГДА при remaining - 1 == 0

for s in range(1, 301):
  if play(s, 2):
    print(s)
'''

# У второго игрока есть стратегия победить первым или вторым ходом, но он не может гарантом выиграть первым
'''Так, мы устанавливаем первое условие (наличие стратегии на 1 и 2 ходах) в первом условии функции: r in (0, 2).
При этом второе условие мы учитываем в начале условия в цикле: if not(play(s, 2)).
Поскольку в условии play(s, 4) r рано или поздно будет равна 2. И именно когда r == 2 мы защитываем победу, учитывая в r in (2, 4).'''

# def steps(p):
#     return p - 2, p - 3, p//3
#
# def play(p, r):
#     if p <= 26 and r in (2, 4):
#         return True
#
#     if p <= 26 or r == 0:
#         return False
#
#     next_steps = [play(step, r - 1) for step in steps(p)]
#
#     return any(next_steps) if r % 2 != 0 else all(next_steps)
#
# for s in range(27, 201):
#     if not(play(s, 2)) and play(s, 4):
#         print(s)
# # 87




# ВАЖНАЯ ДЕТАЛЬ В № 19:
'''Если прописано " при неудачном ходе Пети", то пишем ANY(NEXT_STEPS) И ANY(NEXT_STEPS) БЕЗ ALL!!!'''



