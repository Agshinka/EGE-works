# a = '0123456789abc'
# b = '0123456789abcdefgh'
# b = []
# for x in a:
#     for y in a:
#         t = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
#         if t % 9 == 0:
#             t = int(t//9)
#             b.append(t)
#             print(min(b))