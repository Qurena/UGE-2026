"""Веб: https://3.shkolkovo.online/my/course/7259/dz/26331"""


# 1
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


# 2
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


# 3
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

# 4
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




