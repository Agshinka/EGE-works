for n in range (100):
    for g in range (100):
        for h in range (100):
            s = '0' + '1' * n + '2' * g + '3' * h + '0'
            s1 = s
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(len(s1))