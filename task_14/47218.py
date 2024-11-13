a = '0123456789abcde'
for x in a:
    b = int('123' + x + '5', 15) + int('1' + x + '233', 15)
    if b % 14 == 0:
        print(int(b//14))