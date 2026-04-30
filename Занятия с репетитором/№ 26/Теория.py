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

# f = open("../!Файлы для задач/26wlhf.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
#
# data.sort()
# result = []
#
# # выявляем интервалы из исходного массива
# start, end = data[0]
# for s, e in data[1:]:
#     if s <= end:
#         end = max(end, e)
#     else:
#         result.append([start, end])
#         start, end = s, e
#
# result.append([start, end])
#
# # считаем количество пустых интервалов и их длину
# ldist = 0
# count = 0
# if result[0][0] != 0:
#     ldist += result[0][0]
#     count += 1
# for i in range(len(result) - 1):
#     d = result[i+1][0] - result[i][1] - 1
#     ldist += d
#     count += 1
# if result[-1][-1] != 1440:
#     ldist += 1440 - result[-1][-1] - 1
#     count += 1
# print(count, ldist, sep='\t')
# # 5	303



# Тип 5: Бинарный поиск
'''https://leetcode.com/problems/binary-search/'''

# def bin_search(nums: list[int], target: int) -> int:
#     lt = 0
#     rt = len(nums) - 1
#     while rt - lt > 1:
#         midel = (rt + lt) // 2
#         if target == nums[midel]:
#             return midel
#         elif target > nums[midel]:
#             lt = midel
#         else:
#             rt = midel
#
#     if nums[rt] == target:
#         return rt
#     if nums[lt] == target:
#         return lt
#     return -1



# Тип 5: Музыкальные стулья
'''https://education.yandex.ru/ege/inf/task/a1b96fa1-7cf5-4a10-aa78-e933372024a2'''

# d = {}
# key = 54
# val = 23
# if key not in d:
#     d[key] = []
# d[key].append(val)
#
# from collections import defaultdict
# # d = defaultdict(int)
# d = defaultdict(list)
# key = 54
# val = 23
# d[key] += 1
#
# d.get(key, 0) # если ключ есть в словаре, то get вернет значение по этому ключу, а если нет - вернёт 0
#
# from collections import Counter
# l = [1, 1, 5, 5, 7, 8, 5]
# print(Counter(l)) # Counter({5: 3, 1: 2, 7: 1, 8: 1})
#
#
# bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)



# Тип 6: Комбайн
'''https://education.yandex.ru/ege/inf/task/b2dafbbb-9867-456d-9211-70dfb78deee9'''
# Ключевая идея: заменяем left и right. Главное в конце убрать площадь пересекающихся строк.

# f = open("26etery.txt")
# [s, w, n, k] = [int(i) for i in f.readline().split()]
# xi = []
# for i in range(n):
#     xi.append(int(f.readline()))
# yi = [int(i) for i in f.readlines()]
#
# # Сначала считаем убранные столбики:
# yi.sort()
# xi.sort()
#
# total_dx = 0
# left, right = [max(xi[0] - w//2, 0), min(s, xi[0] + w//2)] # min и max, чтобы не заходить за края поля
#
# for x in xi:
#     if x - w // 2 <= right:
#         right = min(s, x + w // 2)
#     else:
#         total_dx += (right - left)
#         left, right = [max(x - w//2, 0), min(s, x + w//2)]
#
# total_dx += (right - left)
#
#
# total_dy = 0
# left, right = [max(yi[0] - w//2, 0), min(s, yi[0] + w//2)] # min и max, чтобы не заходить за края поля
#
# for y in yi:
#     if y - w // 2 <= right:
#         right = min(s, y + w // 2)
#     else:
#         total_dy += (right - left)
#         left, right = [max(y - w//2, 0), min(s, y + w//2)]
#
# total_dy += (right - left)
#
# # total_dx * total_dy - площадь пересечения вертикальных и горизонтальных полосок
# ans = s * total_dx + s * total_dy - total_dx * total_dy
# print(ans)



# Тип 7: Гирьки

# with open('24dtwwe.txt') as file:
#     N = int(file.readline())
#     weights = [int(line) for line in file]
# weights.sort()
#
# possible = set() # 1 2 3
# for w in weights:
#     current = {w} # 1 2 3
#     for p in possible:
#         current.add(w + p) # 2 3 4 5
#     possible = possible.union(current)
#
# print(len(possible))
#
# for w in range(1, sum(weights) + 1):
#     if w not in possible:
#         print(w)
#         break
# # 4217


# Тип 8: Жилой дом с подъездами
'''https://alex-math.ru/gia/zadaniye-26-informatika-yege-2026-statgrad-23102025'''

# with open("../!Файлы для задач/26etery.txt") as file:
#     n = int(file.readline())
#     data = [list(map(int, i.split())) for i in file.readlines()]
# data.sort(key=lambda x: (x[1], x[2], x[0]))
#
# numhouse = [[0]]
# house = [[0]]
# current = []
# data.append([0, 1001, 0])
#
# for i in range(n):
#         if data[i][1] == data[i+1][1]:
#             current.append([data[i][0], data[i][2]])
#         else:
#             current.append([data[i][0], data[i][2]])
#             numhouse.append(current)
#             current = []
#
# def mxlfh(house):
#     res = []
#     ch = []
#     res.append(house[0])
#     for i in range(1, len(house)):
#         if i != len(house) - 1:
#             if house[i][1] == res[-1][1]:
#                 pass
#             if house[i][1] == res[-1][1] + 1:
#                 res.append(house[i])
#             if house[i][1] > res[-1][1] + 1:
#                 ch.append(res)
#                 res = [house[i]]
#         else:
#             if house[i][1] == res[-1][1]:
#                 ch.append(res)
#             if house[i][1] == res[-1][1] + 1:
#                 res.append(house[i])
#                 ch.append(res)
#             if house[i][1] > res[-1][1] + 1:
#                 ch.append(res)
#                 ch.append(house[i])
#     fin = []
#     mx = 0
#     for line in ch:
#         if len(line) > mx:
#             fin = [line]
#             mx = len(line)
#     for line in ch:
#         if len(line) == mx and [line] != fin:
#             fin.append(line)
#     return fin
#
# for i in range(1, len(numhouse)):
#     house.append(mxlfh(numhouse[i]))
#
# # mx = 0
# # for i in range(1, len(house)):
# #     for k in house[i]:
# #         if len(k) > mx:
# #             mx = len(k)
#
# mxhouse = []
# for i in range(1, len(house)):
#     for k in house[i]:
#         if len(k) == 7:
#             mxhouse.append([i, k])
# print(mxhouse)
# ans1 = mxhouse[0][0]
# ans2 = mxhouse[0][1][0][1]
# print(ans1, ans2)
# # 171 701


# Свободные места в кинотеатре
# f = open("26__86lva.htm")


