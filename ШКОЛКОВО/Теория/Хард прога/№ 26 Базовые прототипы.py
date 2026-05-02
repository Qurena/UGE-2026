"""Конспект по вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/34225"""


# 1 | Конференц-залы:

# f = open("26etery.txt")
# n = int(f.readline())
# a = [list(map(int, i.split())) for i in f]
#
# # Сортируем по времени окончания (второму значению в списке)
# a.sort(key=lambda x: x[1])
# schedule = [a.pop(0)]
#
# for i in a:
#     if i[0] > schedule[-1][1]:
#         schedule.append(i)
#
# # дальше уже смотрим само задание: бывают разные прототипы/вопросы
# mx = 0
# for i in a:
#     if i[0] > 1393:
#         mx = max(mx, i[0])
# print(mx)

'''---------------------------------------------------------------------------------------------------------------------'''

# 2 | Шлифовка и покраска (без подвохов):

# f = open("26etery.txt.")
# n = int(f.readline())
#
# l_start = []
# l_end = []
# for i in range(n):
#     g, p = map(int, f.readline().split()) # g - время шлифовки, p - время покраски, i - номер детали
#     if g > p:
#         l_start.append([p, i]) # добавляем минимальное время и номер детали
#     if g < p:
#         l_end.append([g, i])
# l_start.sort() # на покраску
# l_end.sort(reverse=True) # на шлифовку
# line = (l_start + l_end).sort()
#
# # номер последнего на покраску:
# num1 = l_start[-1][-1]
#
# # номер последнего на шлифовку - номер первой детали в списке шлифовки
# # (так как именно эта деталь имеет наибольшее время окрашивания и будет
# # размещена последней в своей группе):
# num2 = l_end[0][-1]
#
# # количество деталей на покраску, расположенных во второй половине ленты, - длина куска
# # между серединой и краем l_start:
# num = len(l_start) - len(line)//2 # (в задачах с таким вопросом длина line - четная)

'''---------------------------------------------------------------------------------------------------------------------'''

# 3 | Шлифовка и покраска (с общей лентой) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# f = open("../../Практика/Файлы к задачам/26_1M__3whph.txt")
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
# l.sort() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ans1 = l[-2][-1]
# print(ans1, 0) # Так как предпоследняя деталь была размещена с пометкой «grind»,
#                # а на ленте сначала идут отшлифованные, а потом окрашенные детали,
#                # то количество окрашенных деталей до нее – нулевое.
# # 798 0


# 4 | Покраска | [вр. шлиф, вр. окрас], 1. Кол-во отшлиф. дет.? 2. Номер последней размещ. на ленту детали?)
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
# # Последняя, размещ. на ленту деталь, - деталь с макс. временем: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# mx_time = 0
# for det in l:
#     if det[0] > mx_time:
#         mx_time = det[0]
#         mx_detail = det[1]
# print(len(l_start), mx_detail)
# # 484 544

'''---------------------------------------------------------------------------------------------------------------------'''

# 5 | Самолеты (самое позднее время взлета):
# f = open("../../Практика/Файлы к задачам/4_26_conf__3uzok.txt")
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

# 6 | Камеры наблюдения в магазине (1.Кол-во пиков? 2.Макс. кол-во клиентов?)
# f = open("../../Практика/Файлы к задачам/26-130__6qldf.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# day = [0 for _ in range(1440)]
#
# for person in data:
#     start, end = person
#     for sec in range(start, end + 1):
#         day[sec] += 1
# peak = max(day)
# for sec in range(1440):
#     if day[sec] == peak:
#         print(sec, day[sec])
# # 1 644