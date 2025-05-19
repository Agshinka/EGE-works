a = 9 ** 12 + 3 ** 8 - 3
s = ''
while a!= 0:
    s = str(a% 3) + s
    a = a//3
print(s.count('2'))