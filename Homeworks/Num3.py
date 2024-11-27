# Num 1
# g = []
# for p in range (16, 150):
#     a = 10 * p ** 6 + 11 * p ** 5 + 2 * p ** 4 + 6 * p ** 3 + 7 * p ** 2 + 13 * p ** 1 + 1
#     b = 15 * p ** 6 + 0 * p ** 5 + 2 * p ** 4 + 4 * p ** 3 + 10 * p ** 2 + 8 * p ** 1 + 9
#     if (a + b) % (p-1)==0:
#         g.append(p)
# print(min(g))

# Num 2

# a = 4 ** 2018 + 2 ** 2017 -5
# s = bin(a)[2:]
# print(s.count('1'))

# Num 3

# for x in '0123456789ABC':
#     t = int('4C' + x + '4', 15) + int(x + '62A', 13)
#     if t % 121 == 0:
#         print(t // 121)

# Num 4

# for x in '01234567':
#     for y in '01234567':
#         t = int(y + '04' + x + '5', 11) + int('253' + x + y, 8)
#         if t % 117 == 0:
#             print(t // 117)

# Num 5

# a = 4 ** 16 + 2 ** 34 - 8
# s = bin(a)[2:]
# print(s.count('1'))

# Num 6 (отдельно)

# Num 8

# Num 9

# Num 10

# Num 12
# print(len('YYYYYYYYYY'))

# Num 16
# from fnmatch import *
# for n in range (0, 10 ** 10, 3013):
#     if fnmatch(str(n), '1?3948*5'):
#         print(n)

# Num 17
# for n in range (210235, 210301):
#     k = 0
#     g = []
#     for d in range (2, n // 2 + 1):
#         if n % d == 0:
#             k += 1
#             g.append(d)
#             if k > 4:
#                 break
#     if k == 4:
#         print(g)

# Num 18
# from fnmatch import *
# for n in range (0, 10 ** 10, 1917):
#     if fnmatch(str(n), '3?12?14*5'):
#         print(n, n//1917)

# Num 20

# from fnmatch import *
# for n in range (0, 10 ** 10, 3147):
#     if fnmatch(str(n), '1*4302?1'):
#         print(n)