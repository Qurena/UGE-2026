""" Теория по решению задачи № 26"""

'''
Правила для обучения: 
• написать код, который будет работать для произвольных данных (рассмотреть граничные, краевые ситуации)
• подобрать набор небольших тестов на граничные и краевые данные, чтобы можно было как ручным способом отладить код
• дописать код, который будет работать для произвольных данных (рассмотреть граничные, краевые ситуации) 
• подобрать набор небольших тестов, которые как раз и будут содержать эти граничные, краевые ситуации
• прогнать каждый их этих тестов через код ручным способом, предполагая, что код решения написан на листочке,
и мы его не можем запустить
• прогнать код решения через эти тесты уже запустив его в среде разработки
'''

# Тип 1: Жадный алгоритм (конференц-залы)
'''https://education.yandex.ru/ege/inf/task/1e8269f4-e912-4cb5-a75a-468ce40cc16d'''

# # сортируем список по времени окончания меро
# # чем раньше закончится меро, тем лучше
#
# f = open("../!Файлы для задач/26_07a.txt")
# n = int(f.readline())
# ev = [list(map(int, line.split())) for line in f]
#
# ev = sorted(ev, key=lambda x: x[1])
# # ev.sort(key=lambda x: x[1])
# # 480, 600
# ap_ev = [ev[0]]
#
# for i in range(n):
#     if ap_ev[-1][1] <= ev[i][0]:
#         ap_ev.append(ev[i])
#
# ap_ev.pop(-1)
#
# for k in range(n - 1, -1, -1):
#     if ev[k][0] >= ap_ev[-1][-1]:
#         ap_ev.append(ev[k])
#         break
#
# print(len(ap_ev), ap_ev[-1][-1], sep='\t')
# # 16 1345


# Тип 2: Хронология. Живая очередь (багаж)
'''https://education.yandex.ru/ege/inf/task/150c0498-2a71-452d-9522-6eb0bb37d260'''

# k = 2
# n = 5
# regs = [[30, 60], [40, 1000], [59, 60], [61, 1000], [1010, 1440]]
# regs.sort()
#
# lockers = [[0, 0] for _ in range(k)] # Номер ячеек от 0
#
# count = 0
# for start, end in regs:
#     for i in range(len(lockers)):
#         if lockers[i][-1] <= start:
#             lockers[i] = [start, end + 1]
#             count += 1
#             break
#
# latest = 0
# latest_num = None
# for i in range(len(lockers)):
#     if lockers[i][0] > latest:
#         latest = lockers[i][0]
#         latest_num = i + 1
# print(count, latest_num)
# # 4     1




# Тип 3: Посещаемость | Час-пик
'''https://education.yandex.ru/ege/inf/task/e05939fa-2be0-410f-9a67-e8ab0c5b9bb9'''
'''https://education.yandex.ru/ege/inf/task/e05939fa-2be0-410f-9a67-e8ab0c5b9bb9'''

# Быстрый вариант решения (чтобы его хорошо понять, нужно визуализировать код на бумажке)
# f = open("../!Файлы для задач/26htgjdyrtjr.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# visitors = [0]*1441
#
# for start, end in data:
#   visitors[start] += 1
#   visitors[end + 1] -= 1
#
# # current - количество посетителей в момент времени t. current = sum(visitors[:(t+1)])
# current = 0
# mxc = 0
# for v in visitors:
#   current += v
#   mxc = max(mxc, current)
#
# # Рассчитываем количество час-пиков
# count = 0
# current = 0
# for v in visitors:
#     if current != mxc and current + v == mxc:
#         count += 1
#     current += v
# print(count, mxc)
# # 2	643


# Медленный вариант решения (более примитивный)
# f = open("../!Файлы для задач/26htgjdyrtjr.txt")
# n = int(f.readline())
# a = [list(map(int, i.split())) for i in f]
#
# flow = []
# for m in range(24 * 60 + 1):
#     q = 0
#     for k in range(n):
#         if a[k][0] <= m <= a[k][1]:
#             q += 1
#     flow.append(q)
# print(max(flow), sep='\t')
# # 643




# Тип 4: Посещаемость | Нули (нулевая посещаемость)
'''https://education.yandex.ru/ege/inf/task/4e43bee7-572c-4e2e-8805-22fd8a9b50c2'''

f = open("../!Файлы для задач/26wlhf.txt")
n = int(f.readline())
data = [list(map(int, i.split())) for i in f]

data.sort()
    intervals.sort()
    result = []

    start, end = intervals[0]
    for s, e in intervals[1:]:
        if s <= end:
            end = max(end, e)
        else:
            result.append([start, end])
            start, end = s, e

    result.append([start, end])






