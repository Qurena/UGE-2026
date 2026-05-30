"""Веб: https://3.shkolkovo.online/my/course/7259/dz/26331"""

'''---------------------------------------------------------------------------------------------------------------------'''

# Расписание вылетов (1)
# f = open("../Файлы к задачам/3_26_conf__3uznv.txt")
# n = int(f.readline())
# a = [list(map(int, i.split())) for i in f]
# a.sort(key = lambda x: x[1])
# schedule = [a.pop(0)]
# for i in a:
#     if i[0] >= schedule[-1][1]:
#         schedule.append(i)
#
# mn = 10**10
# for i in a:
#     if i[0] >= schedule[-2][1]:
#         mn = min(mn, i[0])
# print(len(schedule), mn)
# # 38 1288

# ----------------------------------------------------------------------------------------------------------------------

# Расписание вылетов (1)
# f = open("../Файлы к задачам/4_26_conf__3uzok.txt")
# a, b = map(int, f.readline().split())
# data = [list(map(int, i.split())) for i in f.readlines()]
# data.sort(key=lambda x: (x[1], x[0]))
# schedule = [data.pop(0)]
# mx_start = []
# for el in data:
#     if el[0] >= schedule[-1][-1] and el[-1] <= a:
#         schedule.append(el)
#
# # поиск самого последнего взлета
# for el in data:
#     if el[-1] <= a and el[0] >= schedule[-2][-1]:
#         mx_start.append(el[0])
#
# print(len(schedule), max(mx_start))
# # 135 7978

'''---------------------------------------------------------------------------------------------------------------------'''

# Покраска (1)
# f = open("../Файлы к задачам/26_1M__3whph.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# conveyor = []
# current_data = []
# l_start, l_end = [], []
#
# num = 0
# for el in data:
#     num += 1
#     el.append(num)
#     g, p, i = el
#     if g not in current_data and p not in current_data:
#         if g < p:
#             l_start.append([g, 'grind', i])
#             current_data.append(g)
#         if g > p:
#             l_end.append([p, 'paint', i])
#             current_data.append(p)
# l_start.sort()
# l_end.sort(reverse=True)
# l = l_start + l_end
# l.sort()
# ans1 = l[-2][-1]
# print(ans1, 0) # Так как предпоследняя деталь была размещена с пометкой «grind»,
#                # а на ленте сначала идут отшлифованные, а потом окрашенные детали,
#                # то количество окрашенных деталей до нее – нулевое.
# # 798 0

# ----------------------------------------------------------------------------------------------------------------------

# Покраска (2)
# f = open("../Файлы к задачам/26_4M__63amv.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# current_data, num, l_start, l_end, conveyor = [], 0, [], [], []
#
# for el in data:
#     num += 1
#     el.append(num)
#     g, p, i = el
#     if p not in current_data and g not in current_data:
#         current_data.append(el)
#         if i % 5 != 0:
#             if g < p:
#                 l_start.append([g, i])
#             if g > p:
#                 l_end.append([p, i])
#         else:
#             if g < p:
#                 l_end.append([p, i])
#             if g > p:
#                 l_start.append([g, i])
#     else:
#         pass
# l_start.sort()
# l_end.sort(reverse=True)
# l = l_start + l_end
# print(l_end[0][-1], len(l_start) - len(l)//2)
# # 895 17

'''---------------------------------------------------------------------------------------------------------------------'''

# Интервалы
# 1 (https://3.shkolkovo.online/my/course/7259/dz/30727)
# f = open("Файлы для пробников/26__8lb2q.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
# data.sort(key=lambda x: x[0])
#
# intervals = []
# cend = data[0][1]
# cstart = data[0][0]
#
# for start, end in data[1:]:
#     if start <= cend:
#         cend = max(end, cend) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     else:
#         intervals.append([cstart, cend])
#         cstart, cend = start, end
# intervals.append([cstart, cend])
#
# sm = 0
# for k in intervals:
#     sm += k[1] - k[0]
# print(len(intervals), sm)
# # 359 86023641

'''---------------------------------------------------------------------------------------------------------------------'''

# Камеры хранения | №1 https://3.shkolkovo.online/my/course/7259/dz/27116
# f = open("../Файлы к задачам/26_9__3ck5k.txt")
# k = int(f.readline())
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# data.sort(key=lambda x: (x[0], -x[1]))
#
# safe = []
# for i in range(k):
#     safe.append([])
#
# ans1 = 0
# ans2 = 0
# count = 0
# for i in range(k):
#     for j in range(n):
#         if not safe[j] or data[i][0] >= safe[j][-1][1] + 1:
#             safe[j].append(data[i])
#             ans1 += 1
#             count += 1
#             if count == 100:
#                 ans2 = j + 1
#             break
#
# print(ans1, ans2)
# # 256 4

'''---------------------------------------------------------------------------------------------------------------------'''

# Конференц-залы | №2 https://3.shkolkovo.online/my/course/7259/dz/27116
# f = open("../Файлы к задачам/1_26_conf__3uznj.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# data.sort(key=lambda x: x[1])
# conf = [data[0]]
#
# for event in data[1:]:
#     if conf[-1][-1] <= event[0]:
#         conf.append(event)
#
# ans1 = len(conf)
#
# mx = 0
# for last_event in data:
#     if last_event[0] >= conf[-2][-1]:
#         mx = max(mx, last_event[0])
# ans2 = mx - conf[-2][-1]
# print(ans1, ans2)
# # 40 26

'''---------------------------------------------------------------------------------------------------------------------'''

# Покраска (детали) | №3 https://3.shkolkovo.online/my/course/7259/dz/27116
# f = open("../Файлы к задачам/26_2M__3whpt.txt")
# n, k = map(int, f.readline().split())
# # 1. Создаем две "коробки"
# l_start = [] # шлифовка
# l_end = [] # покраска
#
# # 2. Рассматриваем детали: если время шлифовки меньше, кладем в первую "коробку" (l_start),
# # если окрашивания - во вторую (l_end).
# for i in range(n):
#     a, b = map(int, f.readline().split())
#     if a < b:
#         l_start.append([a, i + 1]) # одно из значений не нужно (в данном случае время окрашивания)
#     else:
#         l_end.append([b, i + 1]) # i + 1, так как нумерация идет с 1
#
# # 3. Сортировка элементов в двух "коробках"
# l_start.sort()
# l_end.sort(reverse=True)
# # !!!! в l_start - эл-ты в порядке возрастания, а в l_end - в порядке убывания !!!!!
# ans1 = len(l_start)
# l_all = l_start + l_end
# ans2 = l_all[k-1][-1]
# print(ans1, ans2)
# # 489 924

'''---------------------------------------------------------------------------------------------------------------------'''

# Коробки + СТРАННАЯ СОРТИРОВКА | №1 https://3.shkolkovo.online/my/course/7259/dz/29328
# f = open("../Файлы к задачам/26__7a6rm.txt")
# n = int(f.readline())
# boxes = [int(i) for i in f]
# boxes.sort(reverse=True) # тк требуют макс длину стороны самой маленькой коробки
# # если бы просили макс длину большой, то сортировали по возрастанию
#
# present = [boxes.pop(0)]
# for box in boxes:
#     if abs(box - present[-1]) >= 3:
#         present.append(box)
#
# print(len(present), present[-1])
# # 2767 51

'''---------------------------------------------------------------------------------------------------------------------'''

# Камеры наблюдения на участках (столбы)
# f = open("../Файлы к задачам/26_2__6gp6f.txt")
# n = int(f.readline())
# cameras = [int(i) for i in f]
# cameras.sort(reverse=True)
#
# places = [cameras.pop(0)]
# for cam in cameras:
#     if abs(cam - places[-1]) >= 10:
#         places.append(cam)
# print(len(places), places[-1])
# # 946 2

# ----------------------------------------------------------------------------------------------------------------------

# Столбы
# f = open("../Файлы к задачам/26_1__6gp5h.txt")
# n = int(f.readline())
# data = [int(i) for i in f]
# data.sort(reverse=True)
# places = [data.pop(0)]
#
# for el in data:
#     if abs(el - places[-1]) >= 8:
#         places.append(el)
# print(len(places), places[-1])
# # 1214 6

'''---------------------------------------------------------------------------------------------------------------------'''

# Покраска | ([вр. шлиф, вр. окрас], 1. Сколько дет. будет отшлиф.? 2. Номер дет. на позиции K на ленте?)
# f = open("../Файлы к задачам/26_2M__3whpt.txt")
# n, k = map(int, f.readline().split())
# data = [list(map(int, i.split())) for i in f]
# l_start, l_end = [], []
#
# num = 0
# for el in data:
#     num += 1
#     sh, p = el
#     if p < sh:
#         l_end.append([p, num])
#     else:
#         l_start.append([sh, num])
#
# l_start.sort()
# l_end.sort(reverse=True)
# l = l_start + l_end
# print(len(l_start))
# print(l[k - 1][1])
# # 489 924

# ----------------------------------------------------------------------------------------------------------------------

# Покраска | [вр. шлиф, вр. окрас], 1. Номер предпоследней детали на общей ленте? 2. Кол-во дет., окраш. до неё?
# f = open("../Файлы к задачам/26_1M__3whph (1).txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# l_start, l_end = [], []
#
# num = 0
# for el in data:
#     num += 1
#     g, p = el
#     if g < p:
#         l_start.append([g, num])
#     else:
#         l_end.append([p, num])
#
# l_start.sort()
# l_end.sort(reverse=True)
# l = l_start + l_end
# l.sort()
# print(l[-2][1], 0)
# # 1. 798
# # 2. 0, так как деталь с этим номером на шлифовке, то до нее не будет ни одной окраш. детали
# # 798 0

# ----------------------------------------------------------------------------------------------------------------------

# Покраска | [вр. шлиф, вр. окрас], 1. Кол-во отшлиф. дет.? 2. Номер последней размещ. на ленту детали?)
# f = open("../Файлы к задачам/26_1__3whs4.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# l_start, l_end = [], []
#
# num = 0
# for el in data:
#     num += 1
#     g, p = el
#
#     if g < p:
#         l_start.append([g, num])
#     else:
#         l_end.append([p, num])
#
# l_start.sort()
# l_end.sort(reverse=True)
# l = l_start + l_end
#
# # Последняя, размещ. на ленту деталь, - деталь с макс. временем: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# mx_time = 0
# for det in l:
#     if det[0] > mx_time:
#         mx_time = det[0]
#         mx_detail = det[1]
# print(len(l_start), mx_detail)
# # 484 544


'''---------------------------------------------------------------------------------------------------------------------'''

# Камеры наблюдения в магазине | 1.Кол-во пиков? 2.Макс. кол-во клиентов?
# f = open("../Файлы к задачам/26_6__4103i.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# day = [0 for _ in range(1440)]
#
# for person in data:
#     start, end = person
#     for sec in range(start, end + 1):
#         day[sec] += 1
#
# peak = max(day)
#
# ans2 = peak
# ans1 = set()
# for i in range(1440):
#     if day[i] == peak:
#         ans1.add(i)
# print(len(ans1), ans2)
# # 1 3716


'''---------------------------------------------------------------------------------------------------------------------'''
'''https://3.shkolkovo.online/my/course/7259/materials/4093/lesson/39673'''

# 1 | Покраска | [вр. шлиф, вр. окраш], 1. Кол-во отшлиф. дет.? 2. Номер детали на позиции K на ленте?
# f = open("../Файлы к задачам/26_2M__3whpt.txt")
# n, k = map(int, f.readline().split())
#
# l_start = []
# l_end = []
#
# num = 0
# for el in f:
#     grind, paint = map(int, el.split())
#     num += 1
#     if grind < paint:
#         l_start.append([grind, num])
#     if grind > paint:
#         l_end.append([paint, num])
#
# l_start.sort()
# l_end.sort(reverse=True)
#
# line = l_start + l_end
# print(len(l_start), line[k-1][1])
# # 489 924

# ДЗ -------------------------------------------------------------------------------------------------------------------
'''https://3.shkolkovo.online/my/course/7259/dz/31127'''

#157985 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1 | Покраска | [вр. ожид., вр. акт.], 1. Номер последнего на ленте? 2. Кол-во уст-в с позициями ниже?
# f = open("../Файлы к задачам/26task__8k9oc.txt")
# n = int(f.readline())
#
# l_start = []
# l_end = []
# num = 0
# for phone in f:
#     wait, act = map(int, phone.split())
#     num += 1
#     if wait < act:
#         l_start.append([wait, num, 'w'])
#     if act < wait:
#         l_end.append([act, num, 'a'])
# l_start.sort()
# l_end.sort(reverse=True)
# line = l_start + l_end
# line.sort()
#
# position = l_start + l_end
# fnd = line[-1]
# last_num = fnd[1]
# downs = len(position) - 1 - position.index(fnd)
# print(last_num, downs)
# # 667 517

# ----------------------------------------------------------------------------------------------------------------------

# 2 | Покраска | [вр. хран., срок годн.], 1. Номер последнего на ленте? 2. Кол-во тов-в с позициями ниже?
# f = open("../Файлы к задачам/DEMO_26__7atk3.txt")
# n = int(f.readline())
#
# check = []
# l_start = []
# l_end = []
# num = 0
# for product in f:
#     safe, use = map(int, product.split())
#     num += 1
#     if safe not in check and use not in check:
#         if safe < use:
#             l_start.append([safe, num])
#             check.append(safe)
#         if use < safe:
#             l_end.append([use, num])
#             check.append(use)
#
# l_start.sort()
# l_end.sort(reverse=True)
# line = l_start + l_end
# position = l_start + l_end
# line.sort()
# fnd = line[-1]
# print(fnd[1], len(position) - 1 - position.index(fnd))
# # 564 444

# ----------------------------------------------------------------------------------------------------------------------

# 3 | Покраска | [вр. шлиф., срок окраш.], 1. Время обработки дет. на месте 168? 2. Суммарное время окраш. дет.?
# f = open("../Файлы к задачам/26_3__3whrj.txt")
# n = int(f.readline())
#
# check = []
# l_start = []
# l_end = []
# num = 0
#
# for detail in f:
#     grind, paint = map(int, detail.split())
#     num += 1
#     if grind not in check and paint not in check:
#         if grind > paint:
#             l_start.append([grind, num])
#             check.append(grind)
#         if paint > grind:
#             l_end.append([paint, num])
#             check.append(paint)
#
# l_start.sort(reverse=True)
# l_end.sort()
# line = l_start + l_end
#
# sm = 0
# for el in l_end:
#     sm += el[0]
#
# print(line[168-1][0], sm)
# # 1475 616262
