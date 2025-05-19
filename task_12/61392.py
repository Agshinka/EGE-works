for a in range (45, 500):
    s = '0' + a * '1' + a * '2'
    while '01' in s or '02' in s:
        s = s.replace('02', '1110', 1)
        s = s.replace('01', '220', 1)
    summ = sum([int(i) for i in s])
    if summ % 2 == 0:
        print(a)
        break