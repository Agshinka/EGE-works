for n in range (1, 200):
    s = '0' + '1' * n + '2' * n + '0'
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    summ = [int(i) for i in s]
    k=0
    for x in range (2, summ):
        if summ % x == 0:
            k += 1
    if k == 0:
        print(s.count('1'))