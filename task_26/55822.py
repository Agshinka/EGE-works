with open('files/55822.txt', 'r') as file:
    a = file.readlines()
    k = int(a[0])
    n = int(a[1])
    del a[0]
    del a[0]
    bags = 0
    last = 0
    a = [i.split() for i in a]
    a = [[int(line[0]), int(line[1])] for line in a]
    a = sorted(a, key=lambda i: (i[0]))
    cells = []
    for cell in range (k):
        cells.append(a[cell])
    print(cells)
    for p in range (k, len(a)):
        for c in range (len(cells)):
            if cells[c][1] <= a[p][0] - 1:
                bags += 1
                cells[c] = a[p]
                last = cells.index(cells[c])
                break
    print(cells)
    print(a)
    print(bags + k)
    print(last + 1)