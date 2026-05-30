"""Решение задач на "жадные алгоритмы" и не только"""

'''https://3.shkolkovo.online/my/course/7259/materials/lesson/34225'''
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
# # (так как именно эта деталь имеет наибольшее время шлифовки и будет
# # размещена последней в своей группе):
# num2 = l_end[0][-1]
#
# # количество деталей на покраску, расположенных во второй половине ленты, - длина куска
# # между серединой и краем l_start:
# num = len(l_start) - len(line)//2 # (в задачах с таким вопросом длина line - четная)

# ----------------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------------

# 4 | Покраска | [вр. шлиф, вр. окрас], 1. Кол-во отшлиф. дет.? 2. Номер последней размещ. на ленту детали?)
# f = open("../../Практика/Файлы к задачам/26_1__3whs4.txt")
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
# l.sort()
# print(len(l_start), l[-1][-1])
# 484 544

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

'''---------------------------------------------------------------------------------------------------------------------'''
'''https://3.shkolkovo.online/my/course/7259/materials/4093/lesson/39670'''

# 1 | Камеры хранения с доп. условиями (размеры вещей)
# f = open("../../Практика/Файлы к задачам/26_3__3cjvp.txt")
# k = int(f.readline())
# n = int(f.readline())
# x_size = [[[]for _ in range(n)] for _ in range(3)]
#
# categories = {'A': 0, 'B': 1, 'C': 2}
# data = []
# for customer in f:
#     start, end, size = customer.split()
#     bag = [int(start), int(end), categories[size]] # если size == 'A', то добавляем 0, если 'B' - 1, если 'C' - 2
#     data.append(bag)
#
# data.sort()
#
# cnt = 0
# mx = 0
# for customer in data:
#     ct = customer[2]
#     for cell in range(len(x_size[ct])):
#         if x_size[ct][cell] == [] or x_size[ct][cell][-1][1] < customer[0]:
#             x_size[ct][cell].append(customer)
#             cnt += 1
#             mx = max(mx, customer[0])
#             if customer[0] == 999:
#                 print(customer)
#             break
# print(cnt)
# # 271 1

# ----------------------------------------------------------------------------------------------------------------------

# 2 | Камеры хранения с доп. условиями (отель БУ)
# f = open("../../Практика/Файлы к задачам/26_6__3ck48__3t75n.txt")
# n = int(f.readline())
# k = int(f.readline())
# rooms = [[] for _ in range(k*3)] # индекс - номер комнаты (№0-19 - 1 этаж; №20-39 - 2 этаж; №40-59 - 3 этаж)
# data = [list(map(int, i.split())) for i in f]
# data.sort(key=lambda x: (x[0], -x[1]))
#
# for i in range(n):
#     if data[i][2] < 200:
#         data[i] += [20] # 1 этаж за 100 баксов
#     elif data[i][2] < 300:
#         data[i] += [40] # 2 этаж за 200 баксов
#     else:
#         data[i] += [60] # 3 этаж за 300 баксов
#
# customers_money = 0
# profit = 0
# for customer in data:
#     balance = customer[3]
#     for num_of_room in range(balance-20, balance):
#         if (not(rooms[num_of_room])) or rooms[num_of_room][-1][1] < customer[0]:
#             rooms[num_of_room].append(customer)
#             customers_money += customer[2] - balance * 5
#             profit += balance * 5
#             break
#
# print(customers_money, profit)
# # 14040 39700

