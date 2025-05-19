for n in range (1,1000):
    s = bin(n)[2:]
    s = s + bin(s.count('1') % 2)[2:]
    s = s + bin(s.count('1') % 2)[2:]
    r = int(s,2)
    if r >= 77:
        print(n)