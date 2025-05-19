a = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255
s = ''
while a!=0:
    s = str(a % 8) + s
    a = a // 8
print(s.count('0'))