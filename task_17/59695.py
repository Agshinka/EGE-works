with open('task_17/files/59695.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    g = []
    k = 0
    for j in range (len(a)):
        if a[j] % 100 == 15:
            g.append(a[j])
    for n in range (len(a)-2):
        elem = [a[n], a[n+1], a[n+2]]
        qlen = [len(str(i)) for i in elem]
        if f'{qlen[0]}{qlen[1]}{qlen[2]}'.count('4') == 1:
            if (a[n] + a[n+1] + a[n+2]) >= max(g):
                k+=1
                b.append(a[n] + a[n+1] + a[n+2])
print(k, max(b))