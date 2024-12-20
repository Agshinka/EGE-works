for n in range (1, 1000):
    s = bin(n)[2:]
    k1 = 0
    k2 = 0
    for g in range (len(s)):
        if g % 2 != 0 and s[g] == '1':
            k1 += 1
        elif g % 2 == 0 and s[g] == '0':
            k2 += 1
    if abs(k1 - k2) == 4:
        print(n)