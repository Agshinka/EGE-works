with open('files/27887.txt', 'r') as file:
    a = file.readlines()
    del a[0]
    b = []
    k = 0
    a = sorted([int(i) for i in a])
    for n in range (len(a)):
        k+=1

