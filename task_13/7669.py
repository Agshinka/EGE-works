# print(bin(224)[2:], bin(128)[2:], '0' + bin(112)[2:], '0' * 8)

# print(bin(224)[2:], bin(128)[2:], '0' + bin(64)[2:], '0' * 8)


# print('119', '167', int('10000000', 2), '0')


mask = [int('1' * i + '0' * (8 - i), 2) for i in range (9)]
print(*[m for m in mask if 112 & m == 64])