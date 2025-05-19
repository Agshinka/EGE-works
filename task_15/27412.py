for a in range (1,1000):
    flag = True
    for x in range (1,1000):
        if ((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0))) == 0:
            flag = False
    if flag == True:
        print(a)