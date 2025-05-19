with open('files/33528.txt', 'r') as file:
    a = file.readlines()
    n, m = a[0].split()
    n = int(n)
    m = int(m)
    k=0
    del a[0]
    a = [i.split() for i in a]
    for n in range (len(a)):
        if a[n][2] == 'A':
            m = m - (int(a[n][0]))
    print(m)
    a = [[int(line[0]), int (line[1]), line[2]] for line in a]
    a = sorted(a, key = lambda i:(i[0], i[1]))
    print(a)
    for g in range (len(a)):
        if a[g][2] == 'B':
            if (m - (a[g][0])) > 0:
                m = m - (a[g][0])
                k+=1
print(k, m)