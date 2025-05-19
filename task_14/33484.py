a = 343 ** 6 - 7 ** 10 + 47
s =''
while a != 0:
    s = str(a % 7) + s
    a = a//7
print(s.count('6'))