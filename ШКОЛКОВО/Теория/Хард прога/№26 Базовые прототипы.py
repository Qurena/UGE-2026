"""Конспект по вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/34225"""


# 1 | Конференц-залы:

# f = open("26.txt")
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


# 2 | Шлифовка и покраска (без подвохов):

f = open("26.txt.")
n = int(f.readline())

l_start = []
l_end = []
for i in range(n):
    g, p = map(int, f.readline().split()) # q - время шлифовки, p - время покраски, i - номер детали
    if g > p:
        l_start.append([g, p, i])
    if g < p:
        l_end.append([g, p, i])
l_start.sort()
l_end.sort(reverse=True)
line = l_start + l_end

