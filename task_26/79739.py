with open('files/79739.txt' ,'r') as file:
    a = file.readlines()
    a = sorted([int(i) for i in a])[::-1]
    k=0
    box = a[0]
    for n in range (1, len(a)):
        if box - a[n] >= 9:
            k+=1
            box = a[n]
print(k, box)
