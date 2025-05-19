for a in range (1, 250):
    flag = True
    for x in range (1, 250):
        if ((x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))) == 0:
            flag = False
    if flag == True:
        print(a)