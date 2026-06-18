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


'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/29327'''


# 6
# def f(n):
#     divs = set()
#     p = 0
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n // i)
#     if divs:
#         p = int(sum(divs) / len(divs))
#     return p
#
#
# stp = 0
# for n in range(750_001, 1_000_000):
#     if f(n) % 7 == 6:
#         stp += 1
#         print(n, f(n))
#     if stp == 5:
#         break
# # 750002 35482
# # 750007 16316
# # 750021 125005
# # 750022 29392
# # 750024 31919


# 7
# def is_prime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
# def f(n):
#     divs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     return divs
#
# stop = 0
# for n in range(8_712_014, 9_000_000):
#     p = f(n)
#     dvs = []
#     for el in p:
#         if is_prime(el):
#             dvs.append(el)
#     m = 0
#     if dvs:
#         m = max(dvs) - min(dvs)
#     if m > 50_000 and str(m) == str(m)[::-1]:
#         print(n, m)
#         stop += 1
#     if stop == 5:
#         break
# # 8713118 71417
# # 8713169 86168
# # 8716479 61816
# # 8717691 67576
# # 8718316 70307


# 8
# def good11(n):
#     divs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     if divs:
#         d = sorted(divs)
#         for el in d:
#             if el % 100 == 11 and el != 11:
#                 return el
#     return False
#
# stop = 0
# for i in range(1_350_051, 1_600_000):
#     if good11(i):
#         print(i, good11(i))
#         stop += 1
#     if stop == 5:
#         break
# # 1350051 311
# # 1350055 270011
# # 1350062 511
# # 1350063 40911
# # 1350066 225011


# 9
# def d(n):
#     divs = set()
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     odd = even = 0
#     for el in sorted(divs):
#         if el % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     if even == odd and sum(divs) % 2 != 0:
#         return True
#     return False
#
# ans = 0
# for i in range(312_322, 486_712):
#     if d(i):
#         ans += 1
# print(ans)
# # 49


# 10
# def d(n):
#     divs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     even = odd = 0
#     if len(divs) == 4:
#         for el in sorted(divs):
#             if el % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1
#         if even == odd:
#             return True
#     return False
#
# count = sm = 0
# for i in range(90_000, 147_001):
#     if d(i):
#         count += 1
#         sm += i
# print(count, sm)
# # 11 1334422



# Задача с ЕГЭ
'''Найдите такое м, что м >90_000 и простое и содержит в своей записи ровно одну последовательность «489».
М - сумма Макс и мин простого натурального делителя числа, не считая само число. 
Первые 5 чисел и м, им соответсвующие, чтобы каждое из них было больше 8_007_504_024'''
# def prime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
# def mn_prime_divisor(x):
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0 and prime(i):
#             return i
#     return 0
#
# def mx_prime_divisor(x):
#     for i in range(int(x**0.5), 1, -1):
#         if x % i == 0 and prime(i):
#             return i
#     return 0
#
# for x in range(8_010_000_000, 8_050_000_000):
#     m1 = mn_prime_divisor(x)
#     m2 = mn_prime_divisor(x)
#     m = m1 + m2
#     if m > 90_000 and prime(m) and str(m).count('489') == 1:
#         print(x, m)


















