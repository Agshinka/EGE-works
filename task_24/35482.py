with open('files/35482.txt', 'r') as file:
    a = file.readlines()
    maxx = 0
    minn = 1_000_000
    for n in range (len(a)):
        g = a[n].count('G')
        if g < minn:
            minn = g
            line = n
print(a[line])
print(max(set(a[line]), key = a[line].count))