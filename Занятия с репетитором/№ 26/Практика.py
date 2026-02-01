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

# f = open("../!Файлы для задач/26_2.txt")
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
# # 59	290



