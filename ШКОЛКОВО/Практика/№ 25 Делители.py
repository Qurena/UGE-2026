"""Дз к вебу: https://3.shkolkovo.online/my/course/7259/materials/lesson/37103 (начиная с номера 6)"""



# 6
# def prime(x):
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return x > 1
#
# def s(x):
#     divs = set()
#     s = 0
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0 and prime(i):
#             s += i
#             divs.add(i)
#             if prime(x // i):
#                 s += x // i
#                 divs.add(x//i)
#     return s
#
#
# stop = 0
# for x in range(1325000 - 1, 1, -1):
#     if 0 < s(x) <= 30000 and s(x) % 5 == 0:
#         print(x)
#         stop += 1
#     if stop == 5:
#         break
# 1324994 1324992 1324991 1324986 1324980


# 7
# for x in range(11110, 55557):
#     divs = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             divs.add(i)
#             divs.add(x // i)
#     if len(divs) == 3:
#         print(*sorted(divs))
# # 11 121 1331 13 169 2197


# 8
# def d(x):
#     divs = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             divs.add(i)
#             divs.add(x // i)
#     return len(divs)
#
# mx = 0
# mx_x = []
# for x in range(28454, 28599):
#     if d(x) > mx:
#         mx = d(x)
#         mx_x.append(x)
# print(max(mx_x), d(max(mx_x)))
# # 2856080


# 9
# def d(x):
#     divs = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             divs.add(i)
#             divs.add(x // i)
#     return divs
#
#
# for x in range(412500, 412671):
#     if len(d(x)) == 6:
#         print(*sorted(d(x)))
# # 1 13 169 2441 31733 412529 1 7 49 8419 58933 412531 1 2 4 103141 206282 412564 1 3 9 45841 137523 412569


# 10
# stop = 0
# for x in range(850000, 10**7):
#     f = 0
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             f = x // i - i
#             break
#     if f > 0 and f % 13 == 0:
#         print(x, f)
#         stop += 1
#     if stop == 6:
#         break
# # 850022 425009 850048 425022 850053 283348 850074 425035 850099 7410 850100 425048


# 11
# def prime(x):
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return x != 1
#
#
# ans = []
#
# for x in range(182_635, 453_733 + 1):
#     flag = 0
#     for i in range(2, int(x ** 0.5) + 1):
#         if (x % i == 0) and prime(i) and prime(x // i) and (i != x // i):
#             flag = 1
#             break
#
#     if flag == 1:
#         ans.append(x)
#
# print(len(ans), max(ans) + min(ans))
# # 57221 636366


# 12
# def prime(x: int) -> bool:
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return x > 1
#
# def count(x: int) -> list[int]:
#     div = []
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             div.append(i)
#             div.append(x//i)
#     if div == []:
#         return [0]
#     return div
#
#
# for x in range(650_001, 655_000):
#     if prime(max(count(x))) == False:
#         print(x, max(count(x)))