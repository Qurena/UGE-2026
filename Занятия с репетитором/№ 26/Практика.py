"""Дз по номеру 26"""

# 1
'''https://education.yandex.ru/ege/inf/task/42a401dc-944e-49e9-a5ea-83f180499221'''

# # f = open("../!Файлы для задач/test27.txt")
# f = open("../!Файлы для задач/26_2.txt")
# n = int(f.readline())
# a = [list(map(int, i.split())) for i in f]
#
# a = sorted(a, key = lambda x: x[-1])
#
# ev = [a[0]]
# for i in range(n):
#   if a[i][0] >= ev[-1][-1]:
#     ev.append(a[i])
#
#
# max_time = []
# r = sorted(a, key = lambda x: x[0])
# for i in range(n):
#   if r[i][0] >= ev[-2][-1]:
#     max_time.append(r[i])
#
# t = 0
# for i in range(len(max_time)):
#   if max_time[i][0] - ev[-2][-1] > t:
#     t = max_time[i][0] - ev[-2][-1]
# print(len(ev), t, sep='\t')
# # 32 15


# 2
'''https://education.yandex.ru/ege/inf/task/ea4c8f9d-4292-4fef-bd08-426ed0628ff2'''

# Первый вариант решения (от репетитора)
# f = open("../!Файлы для задач/26_2.txt")
# n, start, end = map(int, str(f.readline()).split())
# a = [list(map(int, i.split())) for i in f]
# s = start
# a.sort(key=lambda x: (x[0], x[1]))
# supvis = []
#
# max_end = 0
# for i in range(n):
#     if a[i][-1] <= end:
#         if a[i][0] <= start:
#             if max_end < a[i][-1]:
#                 max_end = a[i][-1]
#                 max_vis = a[i]
#         else:
#             supvis.append(max_vis)
#             start = max_end
#
#
# print(len(supvis), supvis[0][1] - s, sep='\t')
# # 59	290

# Второй вариант решения (мой)
# f = open("26_07a.txt")
# n, start, end = map(int, str(f.readline()).split())
# a = [list(map(int, i.split())) for i in f]
#
# eyes = []
# mxt = 0
# for i in range(n):
#   if a[i][0] <= start:
#     if a[i][-1] > mxt:
#       mxt = a[i][-1]
#       first_eye = a[i]
#
# eyes.append(first_eye)
#
# def e(eyes):
#   mxt = 0
#   for i in range(n):
#     if a[i][0] <= eyes[-1][-1]:
#       if a[i][-1] > mxt:
#         mxt = a[i][-1]
#         eye = a[i]
#   return eye
#
#
# while eyes[-1][-1] < end:
#   eyes.append(e(eyes))
#
# # print(eyes)
# print(len(eyes), eyes[0][-1] - start, sep='\t')
# # 59  290


# 3
'''https://education.yandex.ru/ege/inf/task/3279f3d4-7062-408a-add0-f583bc63cb5e'''

# f = open("../!Файлы для задач/26_07a.txt")
# # f = open("../!Файлы для задач/test_07a.txt")
# k = int(f.readline())
# n = int(f.readline())
# book = [list(map(int, i.split())) for i in f]
#
# rooms = [[0, 0] for _ in range(k)]
# book.sort(key=lambda x: x[0])
#
# count = 0
# for start, end in book:
#     for i in range(k):
#         if rooms[i][-1] <= start:
#             rooms[i] = [start, end]
#             count += 1
#             break
#
# last = 0
# latest_room = 0
# for i in range(k):
#     if rooms[i][-1] > last:
#         last = rooms[i][-1]
#         latest_room = i + 1
# print(count, latest_room, sep='\t')


# 4
'''https://education.yandex.ru/ege/inf/task/e9225026-ae6e-4bf3-bff5-240fe5b810e6'''

# f = open("../!Файлы для задач/26_07b.txt")
# k, n = map(int, f.readline().split())
# ord = [list(map(int, i.split())) for i in f]
# ord.sort(key=lambda x: (x[0], -x[1]))
#
# pr = [0]*k
# latest = 0
# count = 0
# for start, dur in ord:
#     min_val = min(pr)
#     id = pr.index(min_val)
#     if pr[id] <= start:
#         latest = max(latest, pr[id])
#         pr[id] = start + dur + 3
#     else:
#         pr[id] += dur + 3
#         if pr[id] <= start + 420:
#             count += 1
#
# print(count, latest)


# 5
'''https://alex-math.ru/gia/zadaniye-26-informatika-yege-2026-statgrad-16122025'''

# f = open("../!Файлы для задач/26hm19.02.txt")
# # f = open("testhm19.022.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f.readlines()]
#
# data.sort()
# result = []
#
# start, end = data[0]
# for s, e in data:
#     if s < end:
#         end = max(end, e)
#     else:
#         result.append([start, end])
#         start, end = s, e
# result.append([start, end])
#
# ld, c = 0, 0
# if result[0][0] != 0:
#     ld += result[0][0]
#     c += 1
#
# for i in range(len(result) - 1):
#     ld += result[i+1][0] - result[i][1]
#     c += 1
#
# if result[-1][1] != 86400000:
#     ld += 86400000 - result[-1][1]
#     c += 1
# print(c, ld, sep='\t')
# # 360	376359
