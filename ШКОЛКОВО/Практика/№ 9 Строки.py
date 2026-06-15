"""https://3.shkolkovo.online/my/course/7259/dz/28544"""

# 4
# f = open("Файлы к задачам/9_12345.txt")
# count = 0
# for st in f:
#     d = []
#     for el in map(int, st.split()):
#         d.append(el)
#
#     flag = 1
#     for i in range(len(d)):
#         for j in range(i + 1, len(d)):
#             if (d[i] + d[j]) % 2 != 0:
#                 flag = 0
#                 break
#     if flag == 1:
#         count += 1
# print(count)
# # 464


# 5
# f = open("Файлы к задачам/9_0987.txt")
# count = 0
# for st in f:
#     d = []
#     for e in map(int, st.split()):
#         d.append(e)
#
#     povtorki = []
#     for i in range(len(d)):
#         p = 1
#         for j in range(i + 1, len(d)):
#             if d[i] == d[j]:
#                 p += 1
#         povtorki.append(p)
#     flag3 = 0
#     flag1 = 0
#     for i in povtorki:
#         if i >= 3:
#             flag3 = 1
#         if i == 1:
#             flag1 = 1
#     if flag1 == 1 and flag3 == 1:
#         dig_povt = []
#         for i in range(len(povtorki)):
#             p = 0
#             if povtorki[i] != 1:
#                 p = d[i]
#                 for _ in range(povtorki[i]):
#                     dig_povt.append(p)
#                 break
#         for i in range(len(povtorki)):
#             p = 0
#             if povtorki[i] != 1 and d[i] not in dig_povt:
#                 p = d[i]
#                 for _ in range(povtorki[i]):
#                     dig_povt.append(p)
#                 break
#
#         srar_povt = sum(dig_povt)/len(dig_povt)
#         if len(dig_povt) != 6:
#             srar_ntpovt = (sum(d) - sum(dig_povt))/(len(d) - len(dig_povt))
#         if len(dig_povt) == 6:
#             srar_ntpovt = 0
#         if srar_povt > srar_ntpovt:
#             count += 1
#
# print(count)
# # 35

