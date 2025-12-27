'''Решение дз к вебинару https://3.shkolkovo.online/lesson/34214'''

# 1
'''
def f(n: int) -> str:
    s = ''
    while n != 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]

def ans(n: int) -> int:
    s = f(n)
    t = 1
    for i in s:
        if i != '0':
            t *= int(i)
    if t % 3 == 0:
        s += '21'
    else:
        s += '12'
    return int(s, 4)

mr = []
for i in range(1, 1000):
    if ans(i) <= 280:
        mr.append(ans(i))
print(max(mr))
'''

# 2
'''
def f(n: int) -> str:
    s = ''
    while n != 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]

def ans(n: int) -> int:
    s = f(n)
    if (n % 5) % 2 == 0:
        t = sum(int(i) for i in s)
        s += f(t)
    else:
        s = '21' + s
    return int(s, 5)

a =[]
for n in range(1, 10000):
    if ans(n) <= 320:
        a.append(n)
print(max(a))
'''

# 3
'''
mnr = []
for n in range(1, 100000):
    s = bin(n)[2:]
    s += s[-1]
    if s.count("1") % 2 == 0:
        s += '0'
    else:
        s += '1'

    if s.count("1") % 2 == 0:
        s += '0'
    else:
        s += '1'

    r = int(s, 2)
    if r > 204:
        mnr.append(r)
print(min(mnr))
'''

# 4
'''
mnr = 10000000
mn = 10000000

for n in range(1, 10000):
    s = bin(n)[2:]

    if n % 2 != 0:
        s = '0' + s + '1'
    else:
        s += str(bin(s.count('1'))[2:])

    r = int(s, 2)

    if r > 250:
        if r < mnr:
            mn = n
            mnr = r
print(mn)
'''

# 5
'''
mn = []
for n in range(1, 10000):
    s = bin(n)[2:]

    if n % 2 == 0:
        s += '01'
    else:
        s = '11' + s + '0'

    r = int(s, 2)

    if r > 1021:
        mn.append(n)
print(min(mn))
'''
# 6
'''
s = "3"*20 + "6"*26 + "9"*31
t = 0
while ('36' in s) or ('63' in s) or ('69' in s):
    if '69' in s:
        s = s.replace('69', '63', 1)
        t += 1
    if '36' in s:
        s = s.replace('36', '3', 1)
        t += 1
    if '63' in s:
        s = s.replace('63', '9', 1)
        t += 1
print(t)
'''

# 7
'''
s = "7"*16 + "3"*1600 + "8"*8

while '3' in s or '33' in s or '888' in s:
    if '7' in s:
        s = s.replace('7', '33', 1)
   
    if '33' in s:
        s = s.replace('33', '3', 1)

    if '888' in s:
        s = s.replace('888', '7', 1)


print(sum(int(i) for i in s), s)
'''

# 8
'''
def f(s: str) -> int:
    while '3966' in s or '6666' in s or '963' in s:
        if '3966' in s:
            s = s.replace('3966', '96', 1)

        if '6666' in s:
            s = s.replace('6666', '339', 1)

        if '963' in s:
            s = s.replace('963', '6', 1)
            
            
    return sum(int(i) for i in s)

ans = []
for n in range(5, 1000):
    s = '39' + n*'6'
    if f(s) == 60:
        ans.append(n)
        
print(max(ans))
'''



# 9
'''
def f(s: str) -> int:
    while '6666' in s or '9999' in s:
        if '6666' in s:
            s = s.replace('6666', '699', 1)

        if '9999' in s:
            s = s.replace('9999', '6', 1)

    return s.count('6') * 2 == s.count('9')


ans = 0
for n in range(151, 501):
    s = '6' * n
    if f(s):
        ans += n

print(ans)
'''




