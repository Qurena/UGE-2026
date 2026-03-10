"""Веб: https://3.shkolkovo.online/my/course/7259/dz/26331"""
import locale

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