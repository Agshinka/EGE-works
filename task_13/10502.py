print('0' + bin(119)[2:], bin(167)[2:], '00' + bin(58)[2:], '0' + bin(77)[2:])

print('0' + bin(119)[2:], bin(167)[2:], '00' + bin(32)[2:], '0' * 8)


print('119', '167', int('11100000', 2), '0')

# mask = [int('1' * i + '0' * (8 - i), 2) for i in range (9)]
# print(*[m for m in mask if 58 & m == 32])