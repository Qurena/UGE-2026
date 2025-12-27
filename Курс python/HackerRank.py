'''
if __name__ == '__main__':
    n = int(input())
    list = []

    for _ in range(n):
        command = input().split()

        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            list.insert(i, e)
        elif command[0] == "print":
            print(list)
        elif command[0] == "remove":
            e = int(command[1])
            list.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            list.append(e)
        elif command[0] == "sort":
            list.sort()
        elif command[0] == "pop":
            list.pop()
        elif command[0] == "reverse":
            list.reverse()
'''

'''
n = int(input())
t = tuple(map(int, input().split(' ')))
print(hash(t))
'''

N = int(input())
d = {}
s = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


for key in range(1, N+1):
    d[key] = s[key-1]

for key in d.keys():
    key = input()

print(d)


