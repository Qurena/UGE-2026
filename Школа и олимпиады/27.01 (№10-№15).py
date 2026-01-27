# 12
# a = {
#     'q0.':['.', 'L', 'q1'],
#     'q1.':['.', 'S', 'q1'],
#     'q11':['0', 'L', 'q1'],
#     'q10':['1', 'L', 'q1']
# }
# s1 = '01111'
# s = list('..' + s1 + '..')
# i = -2
# c = 0
# p = 'q0'
# while c != 'S':
#     s[i], c, p = a[p + s[i]]
#     i -= 1
# print(''.join(s))
# # 250

# 13
# from ipaddress import *
#
# net = ip_network('200.33.100.0/255.255.248.0', 0)
#
# ans = 0
# for s in net:
#     p = bin(int(s))[2:].zfill(32)
#     if p.count('1') % 7 != 0:
#         ans += 1
# print(ans)
# # 1717

# 14
# def t(n: int) -> str:
#     s = ''
#     while n != 0:
#         s += str(n % 5)
#         n //= 5
#     return s[::-1]
#
# for x in range(1, 2736):
#     n = 5**2025 + 5**1500 - x
#     tn = t(n)
#     if tn.count('0') == 527:
#         print(x)
# # 2734

