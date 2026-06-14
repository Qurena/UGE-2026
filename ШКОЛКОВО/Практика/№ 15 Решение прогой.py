"""ДЗ к вебу: https://3.shkolkovo.online/my/course/7259/dz/28531"""

# 1
# from turtle import *
# tracer(0)
# lt(90)
# screensize(2000*2000)
# m = 20
#
# for _ in range(3):
#     fd(8*m)
#     rt(90)
#     fd(6*m)
#     rt(90)
# up()
# fd(5*m)
# rt(90)
# fd(1*m)
# lt(90)
# down()
# for _ in range(5):
#     fd(6*m)
#     rt(90)
#     fd(8*m)
#     rt(90)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 102


# 2
# from turtle import *
# tracer(0)
# lt(90)
# screensize(2000*2000)
# m = 20
#
# for _ in range(2):
#     fd(7*m)
#     rt(90)
#     fd(7*m)
#     rt(90)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 36


# 3
# from turtle import *
# tracer(0)
# lt(90)
# screensize(2000*2000)
# m = 20
#
# for _ in range(24):
#     rt(45)
#     fd(2*m)
#     rt(45)
#     fd(2*m)
#     rt(315)
#     fd(2*m)
#     rt(45)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 29


# 4
# from turtle import *
# # tracer(0)
# lt(90)
# screensize(2000*2000)
# m = 20
#
# for _ in range(3):
#     fd(8*m)
#     rt(90)
#     fd(6*m)
#     rt(90)
# up()
# fd(5*m)
# rt(90)
# fd(1*m)
# lt(90)
# down()
# for _ in range(4):
#     for _ in range(4):
#         fd(5*m)
#         rt(120)
#     fd(5*m)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# done()
# # 5


# 5
# def f(x, a):
#     return ((x % 19 != 0) or (x % 13 != 0)) <= (x % a != 0)
#
# for a in range(1, 10000):
#     t = [f(x, a) for x in range(1, 10000)]
#     if all(t):
#         print(a)
#         break
# # 247


# 6
# def f(x, a):
#     return (x % a == 0) <= ((x % 14 == 0) and (x % 21 == 0))
#
# for a in range(1, 10000):
#     t = [f(x, a) for x in range(1, 10000)]
#     if all(t):
#         print(a)
#         break
# # 42


# 7
# def f(a, x, y):
#     return (((x - 10 < a) <= (y + 28 >= 4*a)) or (x + y != 17))
#
# for a in range(100000):
#     t = [f(a, x, y) for x in range(1, 10000) for y in range(1, 1000)]
#     if all(t):
#         print(a)
# # 7


# 8
# def f(a, x, y):
#     return ((y**2 <= a) <= (y <= 10)) and ((x <= 9) <= (x**2 < a))
#
#
# for a in range(1000):
#     t = [f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)]
#     if all(t):
#         print(a)
# # 82


# 9
# def f(a, x):
#     return ((x & 35 != 0) or (x & 23 != 0)) <= ((x & 26 != 0) or (x & a == 0))
#
# for a in range(1, 100000):
#     t = [f(a, x) for x in range(10000)]
#     if all(t):
#         print(a)
#         break
# # 2


# 10
# def f(x, a):
#     return ((((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0)))
#
# for a in range(1, 100):
#     t = 0
#     for x in range(1, 101):
#         if f(x, a) == False:
#             t = 1
#             break
#     if t == 0:
#         print(a)
# # 13


'-----------------------------------------------------------------------------------------------------------------------'
'''https://3.shkolkovo.online/my/course/7259/dz/30089'''

# 2
# ans = set()
# for x in range(100):
#     for y in range(100):
#         if 2*x + y == 99:
#             ans.add(max(x, y) - 1)
# print(min(ans))
# # 32




# 3
# def f(a, x):
#     return (x & a != 0) <= ((x & 25 == 0) <= (x & 17 != 0))
#
# for a in range(100):
#     t = (f(a, x) for x in range(100000))
#     if all(t):
#         print(a)
# # 25


# 4
# def f(a, x):
#     return ( ((x&38 != 0) or (x&45 != 0)) <= ((x&34 == 0) <= (x&a != 0)) )
#
# for a in range(1, 1000):
#     t = (f(a, x) for x in range(1000))
#     if all(t):
#         print(a)
# # 13


# 5
