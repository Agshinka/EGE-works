for a in range (1, 1000):
    flag = True
    for x in range (1000):
        for y in range (1000):
            if ((x + 3 * y > a) or (y < 30) or (x < 30)) == 0:
                flag = False
    if flag == True:
        print(a)