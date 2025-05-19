for a in range (100):
    flag = True
    for x in range (1, 100):
        if (x & 51 == 0 or (not(x & 41 == 0) or (x & a == 0))) == 0:
            flag = False
    if flag == True:
        print(a)