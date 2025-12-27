def s1(N):
    s1 = 0
    while N != 0:
        if (N % 10) % 2 == 0:
            s1 += N % 10
        else:
            s1 += 0
        N //= 10
    return s1

def s2(N):
    a = []
    s2 = 0
    while N != 0:
        a.append(N%10)
        N //= 10

    for i in range(len(a)):
        if i % 2 == 0:
            s2 += int(a[i])
    return s2

def answer(N):
    return abs(s1(N) - s2(N))


for N in range(1, 10000000):
    if answer(N) == 26:
        print(N)
        break