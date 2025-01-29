for a in range (1000):
    flag = True
    for x in range (1, 1000):
        if (((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0)) == 0:
            flag = False
    if flag == True:
        print(a)