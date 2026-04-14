"""Конспект по вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/34227"""

# 1
# f = open("../../Практика/Файлы к задачам/26_8__1kubw.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
#
# # создаем двумерный список
# row = [[] for _ in range(100_001)]
#
# for i in data:
#     x, y = i
#     row[x].append(y) # индекс списка - ряд
#
# for i in range(100001):
#     if row[i]:
#         row[i].sort()
#         for j in range(len(row[i]) - 1):
#             if row[i][j+1] - row[i][j] == 3:
#                 print(i, row[i][j]+1)
#                 break
# # 136 115


# 2
# f = open("../../Практика/Файлы к задачам/task26__5z1ta.txt")
# n, m, k = map(int, f.readline().split())
# data = [list(map(int, i.split())) for i in f]
#
# hall = [[0] for _ in range(k+1)]
# for i in data:
#     x, y = i
#     hall[y].append(x)
#
# for i in range(k+1):
#     if hall[i]:
#         hall[i].sort(reverse=True)
#
# res1 = 10**10
# for i in range(1, k):
#     p1 = hall[i][0] + 1
#     p2 = hall[i+1][0] + 1
#     if max(p1, p2) < res1:
#         res1 = max(p1, p2)
#         res2 = i
# print(res1, res2)
# # 627 503


'''ДЗ к вебу: https://3.shkolkovo.online/my/course/7259/dz/26342'''

# 1
# f = open("../../Практика/Файлы к задачам/Задание_26__mixo__t7qt.txt")
# # f = open("test.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
#
# row = [[] for _ in range(100_001)]
#
# for sit in data:
#     x, y = sit
#     row[x].append(y)
#
# for i in range(len(row)):
#     if row[i]:
#         row[i].sort()
#         for j in range(len(row[i]) - 1):
#             t = row[i][j:j+2]
#             if t[-1] - t[0] == 5:
#                 # print(i, row[i][j+1] - 1)
#                 print(i, row[i][j+1] - 1, row[i])
#                 break
# # 2 12


# 2
# f = open("../../Практика/Файлы к задачам/Задание_26__o4nj__rs6l.txt")
# # f = open("test.txt")
# n = int(f.readline())
# data = [list(map(int, i.split())) for i in f]
#
# row = [[] for _ in range(100_001)]
#
# for tree in data:
#     r, p = tree
#     row[r].append(p)
#
# for i in range(len(row)):
#     if row[i]:
#         row[i].sort()
#         for j in range(len(row[i]) - 1):
#             t = row[i][j:j+2]
#             if t[1] - t[0] == 8:
#                 print(i, row[i][j] + 1)
#                 break
# # 1536 134


# 3
f = open("../../Практика/Файлы к задачам/26__86lva.txt")
# f = open("test.txt")
n, m, k = map(int, f.readline().split())
data = [list(map(int, i.split())) for i in f]
hall = [[] for _ in range(k + 1)]

for sit in data:
    row, place = sit
    hall[place].append(row)
print('1')

new_hall = []
for _ in range(k+1):
    cur = []
    for _ in range(m):
        cur.append([0])
    new_hall.append(cur)
print('2')

for i in range(len(hall)):
    places = hall[i]
    for num in places:
        new_hall[i][num-1] = [1]
print('3')

for place in new_hall[1:]:
    p = place[::-1]
    for i in range(len(p)):
        deep = 0
        for j in range(i+1, len(p)):
            if p[j] == [1]:
                deep += 1
            if deep > 2:
                break
        p[i].append(deep)
print('4')

new_hall = new_hall[1:]
ans = []
for i in range(k-1):
    for k in range(m):
        if new_hall[i][k][0] == [0] and new_hall[i+1][k][0] == [0] and new_hall[i][k][1] <= 2 and new_hall[i+1][k][1] <= 2:
            ans.append([i+1, i+2, k+1])

print(ans)
ans.sort(key=lambda x:(-x[-1]))
mx = ans[0][-1]
for a in ans:
    if a[-1] == mx:
        print(a)