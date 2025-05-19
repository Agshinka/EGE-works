with open('files/27423.txt', 'r') as file:
    a = file.readlines()
    disk, users = a[0].split()
    disk = int(disk)
    users = int(users)
    del a[0]
    a = sorted([int(i) for i in a])
    total = 0
    b = []
    for n in range (len(a)):
        if total + a[n] < disk:
            total += a[n]
            b.append(a[n])
    print(disk - total + b[-1])
    print(len(b), a)
