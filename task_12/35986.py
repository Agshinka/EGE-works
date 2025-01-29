for g in range (1, 50):
    for n in range (1, 50):
        for j in range (1, 50):
            s = '0' + '1' * g + '2' * n + '3' * j + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '320', 1)
                s = s.replace('03', '3012', 1)
            if s.count('1') == 23 and s.count('2') == 48 and s.count('3') == 41:
                print(g + n + j + 2)