# a = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2025
# s = ''
# while a!=0:
#     s = str(a % 25) + s
#     a = a//25
# print(s.count('0'))

# a = '0123456789abcdefghi'
# for x in a:
#     d = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
#     if d % 18 == 0:
#         print(int(d // 18))

# for x in range (1, 2031):
#     a = 7 ** 170 + 7 ** 100 - x
#     s = ''
#     while a!=0:
#         s = str(a % 7) + s
#         a = a//7
#     if s.count('0') == 71:
#         print(x)