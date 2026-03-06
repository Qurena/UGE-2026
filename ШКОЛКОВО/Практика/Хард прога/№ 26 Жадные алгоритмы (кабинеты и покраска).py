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
f = open("../Файлы к задачам/4_26_conf__3uzok.txt")
