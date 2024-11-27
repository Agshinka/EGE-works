# Num 1
# a = 4 ** 2016 + 2 ** 2015 - 7
# a = bin(a)[2:]
# print(a.count('1'))

# Num 2
# a = '0123456789abc'
# for x in a:
#     b = int('26' + x + '98', 13) + int('4' + x + '296', 13)
#     if b % 34 == 0:
#         print(int(b//34))

# Num 3
# a = '0123456789abc'
# for x in a:
#     b = int('8' + x + '71', 13) + int('3' + x + 'DF', 17)
#     if b % 197 == 0:
#         print(int(b//197))

# Num 4
# a = '0123456'
# for x in a:
#     for y in a:
#         b = int(y + x + '320', 7) + int('1' + x + '3' + y + '3', 9)
#         if b % 181 == 0:
#             print(int(b//181))

# Num 5
# a = 36 ** 7 + 6 ** 19 - 18
# s = ''
# while a != 0:
#     s = str(a%6) + s
#     a = a//6
# print(s.count('5'))

# Num 6
# for p in range (9, 30):
#     for x in range (0, p):
#         for y in range (0,p):
#             for z in range (0, p):
#                 for w in range (0, p):
#                     a = z * p ** 4 + x * p ** 3 + y * p ** 2 + x * p ** 1 + 4
#                     b = x * p ** 4 + y * p ** 3 + 6 * p ** 2 + 5 * p ** 1 + 8
#                     c = w * p ** 4 + z * p ** 3 + x * p ** 2 + 7 * p ** 1 + 3
#                     if a + b == c:
#                         print(x * p ** 3 + y * p ** 2 + z * p ** 1 + w * p ** 0)

# Num 7
# a = '01234567'
# for x in a:
#     for y in a:
#         b = int(x + '01' + y + '4', 9) + int(x + y + '544', 8)
#         if b % 89 == 0:
#             print(int(b//89))

# Num 8
# a = '0123456789abc'
# for x in a:
#     for y in a:
#         b = int(x + 'A04', 13) + int('1D' + x + '3', 18)
#         if b % 184 == 0:
#             print(int(b//184))

# Num 9

# a = 5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 -98
# s=''
# g=[]
# while a != 0:
#     s = str(a%7) + s
#     a = a//7
#     g.append(s)
# print(s.count('0'), s.count('6'), s.count('5'))

# Num 10
# a = '0123456789ab'
# for x in a:
#     for y in a:
#         b = int(x + '231' + y, 12) + int('78' + x + '98' + y, 14)
#         if b % 99 == 0:
#             print(int(b//99))

# Num 11
# a = '0123456789abcdefghijklmnopqrstu'
# for x in a:
#     for y in a:
#         b = int('123' + x + 'AB3', 31) + int('3CE' + x + '321', 31)
#         if b % 17 == 0:
#             print(int(b//17))

# Num 12
# for x in '0123456789':
#     t = int('4C' + x + '4', 15) + int('' + x + '62A', 13)
#     if t % 121 == 0:
#         print(t // 121)

# Num 13

# for x in '0123456789ABCDEF':
#     t = int('8' + x + '84' + x, 16) + int('78' + x + '34', 16)
#     if t % 23 == 0:
#         print(t // 23)

# Num 14
# a = 8 ** 2020 + 4 ** 2017 + 26 - 1
# s = bin(a)[2:]
# print(s.count('1'))

# Num 15
# a = '0123456789abcde'   
# for x in a:
#     for y in a:
#         b = int('90' + x + '4' + y, 15) + int('91' + x + y + '2', 16)
#         if b % 56 == 0:
#             print(int(b//56))

# Num 16

# a = '0123456789ab'
# for x in a:
#     b = int('28' + x + '2', 18) + int('93' + x + '5', 12)
#     if b % 133 == 0:
#         print(b//133)

# Num 17
# a = 49 ** 7 + 7 ** 21 - 7
# s = ''
# while a != 0:
#     s += str(a % 7)
#     a //= 7
# s = s[::-1]
# print(s.count("6"))

# Num 18

# a = '0123456789ab'
# for x in a:
#     b = int('2AB' + x, 12) + int(x + '8E', 17)
#     if b % 27 == 0:
#         print(b//27)

# Num 19
# g=[]
# for p in range (16, 150):
#     a = 10 * p ** 6 + 11 * p ** 5 + 2 * p ** 4 + 6 * p ** 3 + 7 * p ** 2 + 13 * p ** 1 + 1
#     b = 15 * p ** 6 + 0 * p ** 5 + 2 * p ** 4 + 4 * p ** 3 + 10 * p ** 2 + 8 * p ** 1 + 9
#     if (a + b) % (p - 1) == 0:
#         g.append(p)
# print(min(g))

# Num 20
# g = []
# for x in range (40):
#     for y in range (40):
#         a = 5 * 40 ** 8 + 7 * 40 ** 7 + x * 40 ** 6 + 6 * 40 ** 5 + 9 * 40 ** 4 + 2 * 40 ** 3 + y * 40 ** 2 + 1 * 40 ** 1 + 9
#         if a % 39 == 0 and (y * 40 ** 1 + x) ** 0.5 == round((y * 40 ** 1 + x) ** 0.5):
#             g.append((y * 40 ** 1 + x))
# print(max(g))