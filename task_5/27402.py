for n in range (1,100):
    s = bin(n)[2:]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s,2)
    if r > 77:
        print(n)
        break