for a in range (250):
    flag = True
    for x in range (1, 250):
        if ((a % 40 == 0) and ((780 % x == 0) <= ((a % x != 0) <= (180 % x != 0)))) == 0:
            flag = False
    if flag == True:
        print(a)