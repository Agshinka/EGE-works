with open('task_17/files/63033.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    j = []
    for g in range (len(a)):
        if a[g] % 1000 == 123:
            j.append(a[g])
    for n in range (len(a)-2):
        summ = [a[n], a[n+1], a[n+2]]
        qlen = [len(str(i)) for i in summ]
        if ((a[n] % 3 == 0) + (a[n+1] % 3 == 0) + (a[n+2] % 3 == 0)) == 1:
            if f'{qlen[0]}{qlen[1]}{qlen[2]}'.count('5') >= 2:
                if (a[n] + a[n+1] + a[n+2]) > max(j):
                    k+=1
                    b.append(a[n] + a[n+1] + a[n+2])
print(k, max(b))
