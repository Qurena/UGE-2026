'''Решение дз к вебинару https://3.shkolkovo.online/lesson/34217'''

'''
# 6
a = '0123456789AB'
m = 0
xa = 0
ya = 0
for x in a:
    for y in a:
        s = int(str(y) + '5'+str(x)+'5', 12) + int('3'+str(x)+'6' + str(y), 12)
        if s % 2 == 0 and s % 3 == 0:
            if m < int(x, 12) + int(y, 12):
                m = int(x, 12) + int(y, 12)
                xa = int(x, 12)
                ya = int(y, 12)
print(int(str(xa), 12), int(str(ya), 12))
'''







