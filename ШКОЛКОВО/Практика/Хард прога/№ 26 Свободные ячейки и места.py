"""Решение задач на свободные ячейки и места"""

'''https://3.shkolkovo.online/my/course/7259/materials/lesson/34226'''

# 1 | Ячейки в магазине
# f = open("26.txt")
# k = int(f.readline())
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
# data.sort()
# cells = [[] for i in range(k)]
#
# c = 0
# mx = 0
# for i in data:
#     for j in range(k):
#         if (not cells[j] or (i[0] > cells[j][-1][1])):
#             cells[j].append(i)
#             c += 1
#             # mx = max(mx, i[0])
#             if i[0] == 1439:
#                  print(j + 1)# номер ячейки
#             break
#
# # print(mx) # 1439
#
# print(c)

'''---------------------------------------------------------------------------------------------------------------------'''

# 2 | Парковочные места
# f = open("26.txt")
# n = int(f.readline())
# a = []
# for s in f:
#     el = s.split()
#     a.append([int(el[0]), int(el[1]) + int(el[0]), el[2]]) # [время начала, время конца, тип автомобиля]
#
# a.sort()
# park = [[] for i in range(100)]
# cars = buses = 0
#
# for car in a:
#     if car[2] == 'A':
#         for j in range(100):
#             if ((not park[j]) or (car[0] >= park[j][-1][1])):
#                 cars += 1
#                 park[j].append(car)
#                 break
#     else:
#         for j in range(80, 100):
#             if ((not park[j]) or (car[0] >= park[j][-1][1])):
#                 buses += 1
#                 park[j].append(car)
#                 break
#
# print(cars, n - buses - cars)
# # 713 23

'''---------------------------------------------------------------------------------------------------------------------'''

# 3 (# 1 из ДЗ к вебу)
# f = open("../Файлы к задачам/26-2__2yr4z.txt")
# k, n = map(int, f.readline().split())
# data = [list(map(int, i.split())) for i in f]
#
# data.sort()
# cells = [[] for i in range(k)]
# ans1 = num = 0
# mx = 0
# for bag in data:
#     for j in range(k):
#         if (not cells[j]) or (bag[0] > cells[j][-1][1]):
#             ans1 += 1
#             cells[j].append(bag)
#             if bag[0] == 1439:
#                 num = max(mx, j + 1)
#             break
# print(ans1, num)
# # 5894 119

'''---------------------------------------------------------------------------------------------------------------------'''

# 4 (# 2 из ДЗ к вебу)
# f = open("../Файлы к задачам/26__1ux52.txt")
# n = int(f.readline())
# data = []
# for s in f:
#     el = s.split()
#     data.append([int(el[0]), int(el[0]) + int(el[1]), el[2]])
#
# data.sort()
# cars = buses = 0
# parking = [[] for i in range(100)]
#
# for car in data:
#     if car[-1] == 'A':
#         for j in range(100):
#             if (not parking[j]) or (car[0] >= parking[j][-1][1]):
#                 cars += 1
#                 parking[j].append(car)
#                 break
#     else:
#         for j in range(80, 100):
#             if (not parking[j]) or (car[0] >= parking[j][-1][1]):
#                 buses += 1
#                 parking[j].append(car)
#                 break
# print(cars, n - cars - buses)
# # 717 19


'''---------------------------------------------------------------------------------------------------------------------'''
'''https://3.shkolkovo.online/my/course/7259/materials/4093/lesson/39670'''

# 1 | Парковочные места (легковые авто и автобусы)
# f = open("../Файлы к задачам/26__1ux58.txt")
# vehicle = int(f.readline())
# type = {'A': 0, 'B': 80}
#
# data = []
# for v in f:
#     start, time, t = v.split()
#     data.append([int(start), int(time) + int(start), type[t]])
# data.sort()
#
# parking = [[] for _ in range(100)] # 0-79 - легковые автомобили, 80-99 - автобусы
#
# ans1 = 0
# c = 0
# for car in data:
#     type = car[-1]
#     for place in range(type, 100):
#         if (not parking[place]) or (parking[place][-1][1] <= car[0]):
#             parking[place].append(car)
#             if type == 0:
#                 ans1 += 1
#             c += 1
#             break
#
# print(ans1, vehicle - c)
# # 713 23

'''---------------------------------------------------------------------------------------------------------------------'''

# 2 | Отель и этажи
# f = open("../Файлы к задачам/2__9snie.txt")
# workers = int(f.readline())
# k = int(f.readline())
# rooms = [[] for _ in range(7*k + 1)]
# rooms[0] = ['.']
#
# data = []
# for cl in f:
#     start, time, type = map(int, cl.split())
#     data.append([start, time + start, type])
#
# data.sort()
#
# cnt = 0
# mx = 0
# for family in data:
#     type = family[-1]
#     for num_room in range((type - 1) * k + 1, type * k):
#         if (not(rooms[num_room])) or (rooms[num_room][-1][1] < family[0]):
#             rooms[num_room].append(family)
#             mx = max(mx, family[0])
#             if family[0] == 274:
#                 print(family, num_room)
#             cnt += 1
#             break
# print(cnt)
# # 274 60

'''---------------------------------------------------------------------------------------------------------------------'''

# 3 | Школа и посадочные места (как парковка)
# f = open("../Файлы к задачам/26_7__1vv36.txt")
# peoples = int(f.readline())
# type = {'A': 20, 'B': 0}
#
# data = []
# for v in f:
#     start, time, t = v.split()
#     data.append([int(start), int(time) + int(start), type[t]])
# data.sort()
#
# lunch = [[] for _ in range(270)] # 0-19 - сотрудники, 20-269 - дети
#
# c = 0
# for p in data:
#     type = p[-1]
#     for place in range(type, 270):
#         if (not lunch[place]) or (lunch[place][-1][1] <= p[0]):
#             lunch[place].append(p)
#             c += 1
#             break
#
# print(c, peoples - c)
# # 740 0
