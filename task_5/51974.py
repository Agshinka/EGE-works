for n in range (1, 100):
    s = bin(n)[2:]
    k = 0
    for g in n:
        k += g
    if k % 2 == 0:
        s += '0'
    else:
        s += '1'
    if k % 2 == 0:
        s += '0'
    else:
        s += '1'
    if k % 2 == 0:
        s += '0'
    else:
        s += '1'
    r = int(s,2)
    if r > 1028:
        print(r)
        break