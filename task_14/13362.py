a = 125 + 25 ** 3 + 5 ** 9
s = ''
while a != 0:
    s = str(a % 5) + s
    a = a//5
print(s)
print(s.count('0'))