k=0
for a in range (1000):
    flag = True
    for x in range (1, 1000):
        for y in range (1,1000):
            if ((x < 6) <= (x ** 2 < a) and ((y ** 2 <= a) <= (y <= 6))) == 0:
                flag = False
    if flag == True:
        k+=1
        print(k)