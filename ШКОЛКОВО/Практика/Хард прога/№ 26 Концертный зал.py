"""Практика по номеру №26"""
from hmac import new

'''https://3.shkolkovo.online/my/course/7259/dz/28545'''
# 1 | Конц. зал
# f = open("../Файлы к задачам/26__t72u.txt")
# n = int(f.readline())
#
# # mx_r = 0
# # for i in f:
# #     row, sit = map(int, i.split())
# #     mx_r = max(mx_r, row)
# # print(mx_r)
# # max_row = 9999 -> берем 1100
#
# hall = [[] for _ in range(11000)]
#
# for i in f:
#     row, sit = map(int, i.split())
#     hall[row].append(sit)
#
# for i in range(len(hall)):
#     r = hall[i]
#     if r:
#         r.sort()
#         for s in range(len(r) - 1):
#             if r[s + 1] - r[s] == 3:
#                 print(r, i)
# ans1 = 8631
# ans2 = 7310 + 1
# print(ans1, ans2)
# # 8631 7311

# ----------------------------------------------------------------------------------------------------------------------

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 2 | Конц. зал | Своб. соседние места в одном ряду, чтобы ПЕРЕД ними было занято НЕ БОЛЕЕ 2-х кресел с такими же номерами. | 1.Макс. номер ряда? 2.Макс номер места в этом ряду?
# f = open("../Файлы к задачам/26__86lva.txt")
# n, c_rows, c_sits = map(int, f.readline().split())
# hall = [[] for _ in range(c_sits + 1)]
#
# for i in f:
#     row, sit = map(int, i.split())
#     hall[sit].append(row)
#
#
# for i in range(len(hall)):
#     if hall[i]:
#         hall[i].sort()
#         # print(i, hall[i])
#
# good_rows = []
# for i in range(len(hall) - 1):
#     n_row1 = hall[i]
#     n_row2 = hall[i+1] # рассматриваем два соседних места
#     if n_row1 and n_row2:
#         for num_row in range(max(n_row1[-1], n_row2[-1]), 0, -1): # определяем максимальный номер ряда
#             if num_row not in n_row1 and num_row not in n_row2:
#                 fulls1 = sum(1 for sit in n_row1 if sit < num_row)
#                 fulls2 = sum(1 for sit in n_row2 if sit < num_row) # cколько занятых рядов до взятого ряда
#                 if fulls1 + fulls2 <= 2: # если в сумме не больше двух, то мы нашли максимальный номер ряда для двух соседних мест
#                     good_rows.append(num_row)
#                     break
# print(max(good_rows)) # первый ответ готов
#
# for i in range(len(hall) - 1):
#     n_row1 = hall[i]
#     n_row2 = hall[i+1]
#     if n_row1 and n_row2:
#         for num_row in range(max(n_row1[-1], n_row2[-1]), 0, -1):
#             if num_row not in n_row1 and num_row not in n_row2:
#                 fulls1 = sum(1 for sit in n_row1 if sit < num_row)
#                 fulls2 = sum(1 for sit in n_row2 if sit < num_row)
#                 if fulls1 + fulls2 <= 2:
#                     if num_row == 4484: # если макс. номер ряда - 4484, выводим номера мест (из них выбираем максимальное)
#                         ans2 = i + 1
# ans1 = max(good_rows)
# print(ans1, ans2)
# # 4484 356

'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/materials/4093/lesson/39671'''

# 1 | Саженцы | Между посаженными ровно 13 непосаженных
# f = open("../Файлы к задачам/m4_26_18_04__3u8wm.txt")
# n = int(f.readline())
# forest = [[] for _ in range(1001)]
#
# for tree in f:
#     row, place = map(int, tree.split())
#     forest[row].append(place)
#
# for i in range(1001):
#     forest[i].sort()
#
# for i in range(len(forest)):
#     for j in range(len(forest[i]) - 1):
#         t = forest[i][j:j+2]
#         if t[1] - t[0] == 14:
#             print(i, forest[i][j] + 1)
#             break
# # 977 858

# ----------------------------------------------------------------------------------------------------------------------

# 2 | Конц. зал | Макс. ряд и макс. место на нём, чтобы перед парой соседних не более 2-х занятых кресел.
# f = open("../Файлы к задачам/26__86lva.txt")
# full, rws, plcs = map(int, f.readline().split())
# hall = [[] for _ in range(plcs + 1)]
#
# for el in f:
#     row, sit = map(int, el.split())
#     hall[sit].append(row)
#
# for i in range(len(hall)):
#     if hall[i]:
#         hall[i].sort()
#
# for i in range(len(hall) - 1):
#     if hall[i]:
#         st1 = hall[i]
#         st2 = hall[i+1]
#         for num in range(max(st1[-1], st2[-1]), 0, -1):
#             if num not in st1 and num not in st2:
#                 first_par = sum(1 for el in st1 if el < num)
#                 second_par = sum(1 for el in st2 if el < num)
#                 if first_par + second_par <= 2:
#                     if num == 4484:
#                         print(i+1) # тк макс. номер места
#                     break
# # 4484 356

'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/30082'''

# 1 | Саженцы
# f = open("../Файлы к задачам/264__1vi92__4jqay.txt")
# n = int(f.readline())
# forest = [[] for _ in range(100_000)]
#
# for tree in f:
#     row, sit = map(int, tree.split())
#     forest[row].append(sit)
#
# for i in range(len(forest)):
#     if forest[i]:
#         forest[i].sort()
#
# for i in range(len(forest)):
#     t = forest[i]
#     for j in range(len(t) - 1):
#         if t[j+1] - t[j] == 12:
#             print(i, t[j]+1)
#             break
# # 59966 81345


# 2 | Конц. зал
# f = open("../Файлы к задачам/Задание_26__tsb3.txt")
# n = int(f.readline())
# hall = [[] for _ in range(100_000)]
#
# for ticket in f:
#     row, sit = map(int, ticket.split())
#     hall[row].append(sit)
#
# for i in range(len(hall)):
#     hall[i].sort()
#
# for i in range(len(hall)):
#     if len(hall[i]) >= 5:
#         for j in range(len(hall[i]) - 4):
#             t = hall[i][j:j+5]
#             print(t)
#             if t[1] - t[0] >= 1 and t[2] - t[1] == 1 and t[3] - t[2] == 1 and t[4] - t[3] >= 1:
#                 print(i, t[3])
# # 71157 24744


# 3 | Конц. зал | Наим номер ряда и места в нем, чтобы за парой своб. мест было все свободно.
# f = open("../Файлы к задачам/task26__5z1ta.txt")
# full, rws, plcs = map(int, f.readline().split())
# hall = [[] for _ in range(plcs + 1)]
#
# for ticket in f:
#     row, sit = map(int, ticket.split())
#     hall[sit].append(row)
#
# for i in range(len(hall)):
#     if hall[i]:
#         hall[i].sort()
#
# for i in range(len(hall) - 1):
#     if hall[i]:
#         st1 = hall[i]
#         st2 = hall[i+1]
#         good_row = max(st1[-1], st2[-1]) + 1
#         if good_row == 627:
#             print(i)
# # 627 503

'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/27823'''

# 1
# f = open("../Файлы к задачам/Задание_26__lood__rjlq (2).txt")
# n = int(f.readline())
#
# data = [[] for _ in range(10_100)]
# for el in f:
#     row, sit = map(int, el.split())
#     data[row].append(sit)
#
# lines = []
# for i in range(len(data)):
#     r = data[i]
#     if r:
#         r.sort()
#         l = 1
#         for k in range(len(r)-1):
#             if r[k+1] - r[k] == 1:
#                 l += 1
#             if r[k+1] - r[k] == 0:
#                 pass
#             if r[k+1] - r[k] > 1:
#                 if l == 2:
#                     print(i)
#                 l = 1
# # 2 29


# 2
# f = open("../Файлы к задачам/Задание_26__wxju.txt")
# n = int(f.readline())
#
# data = [[] for _ in range(100_100)]
# for ticket in f:
#     row, sit = map(int, ticket.split())
#     data[row].append(sit)
#
# for i in range(len(data)):
#     r = data[i]
#     if r:
#         r.sort()
#         for k in range(len(data[i])-1):
#             if r[k+1] - r[k] == 4:
#                 break
#
# ans1 = 136
# ans2 = 0
# q = data[136]
# for sit in range(len(q) - 1):
#     if q[sit+1] - q[sit] == 4:
#         print(q[sit], q[sit+1])
#         ans2 = q[sit] + 2
# print(ans1, ans2)
# # 136 297


# 3
# f = open("../Файлы к задачам/task26__5z1ta.txt")
# n_sits, n_rows, n_sits_per_row = map(int, f.readline().split())
# data = [[]for _ in range(n_sits+1)]
#
# for ticket in f:
#     row, sit = map(int, ticket.split())
#     data[sit].append(row)
#
# for i in range(len(data)):
#     r = data[i]
#     if r:
#         r.sort()
# ans1 = ans2 = 0
# rs = []
# for i in range(1, len(data) - 1):
#     if data[i] and data[i+1]:
#         first = data[i]
#         second = data[i+1]
#         good_row = max(first[-1]+1, second[-1]+1)
#         if good_row == 627:
#             print(i)
#         rs.append(good_row)
# print(min(rs))
# # 627 503












