with open('files/33198.txt', 'r') as file:
    a = file.readlines()
    numofitems, limit = a[0].split()
    numofitems = int(numofitems)
    limit = int(limit)
    b = []
    del a[0]
    items = [int(i) for i in a]

    for n in range (len(items)):
        if (items[n] >= 200) and (items[n] <= 210):
            b.append(items[n])
    for i in items:
        if i in b:
            items.remove(i)

    freespace = limit - sum(b)
    items = sorted(items)
    k = []
    for g in range(len(items)):
        if sum(k) <= freespace:
            k.append(items[g])
    print(len(b) + len(k) - 1)
    print(items[110])
    print(items)
    print(len(k))