"""Практика по номеру №26"""

'''https://3.shkolkovo.online/my/course/7259/dz/28545'''
# 1
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

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 2 | Своб. соседние места в одном ряду, чтобы ПЕРЕД ними было занято НЕ БОЛЕЕ 2-х кресел с такими же номерами. | 1.Макс. номер ряда? 2.Макс номер места в этом ряду?
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