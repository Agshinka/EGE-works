
for n in range (0, 256):
    s = bin(n)[2:]
    if len(s) < 8:
        s = '0' * (8 - len(s)) + s
    s = s.replace('0', '+')
    s = s.replace('1', '0')
    s = s.replace('+', '1')
    r = int(s,2)
    d = r - n
    if d == 111:
        print(n)