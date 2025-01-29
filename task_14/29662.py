a = 81 ** 17 + 3 ** 24 - 45
s = ''
while a != 0:
    s = str(a % 9) + s
    a = a//9
print(s.count('8'))