p = list(range(10, 35))
q = list(range(17, 48))
for a in range (1000):
    flag = True
    for x in range (1000):
        if (((x in a) <= (not x in p)) <= ((x in a) <= (x in q))) == 0:
            flag = False
    if flag == True:
        print(a)


# [10 11 12 13 14 15 16 (17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35) 36 37 38 39 40 41 42 43 44 45 46 47 48]