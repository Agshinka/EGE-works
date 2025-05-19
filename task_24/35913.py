with open('files/35913.txt' ,'r') as file:
    a = file.readlines()
    minn = 1_000_000
    for n in range (len(a)):
        g = a[n].count('N')
        if g < minn:
            minn = g
            line = n
print(sorted([[i, a[line].count(i)] for i in set(a[line])]))