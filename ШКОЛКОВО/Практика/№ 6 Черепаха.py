'''Решение дз к вебинару https://3.shkolkovo.online/lesson/34217'''

# 5
'''
from turtle import *

tracer(0)
screensize(2000*2000)
lt(90)
k = 20

for _ in range(2):
    fd(10*k)
    rt(90)
    fd(20 * k)
    rt(90)

up()

fd(5*k)
rt(90)
fd(7*k)
lt(90)

down()

for _ in range(2):
    fd(20*k)
    rt(90)
    fd(40*k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4, 'blue')

done()
'''