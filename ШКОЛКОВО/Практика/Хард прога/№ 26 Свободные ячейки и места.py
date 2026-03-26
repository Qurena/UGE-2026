"""Конспект по вебу + дз: https://3.shkolkovo.online/my/course/7259/materials/lesson/34226"""

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
