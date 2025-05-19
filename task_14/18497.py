a = 6 * 343 ** 5 + 5 * 49 ** 7 - 50
s = ''
while a!=0:
    s = str(a % 7) + s
    a = a//7
print(s.count('6'))