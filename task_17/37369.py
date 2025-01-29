with open('task_17/files/37369.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    k = 0
    b = []
    j = []
    for n in range (len(a)-1):
        for g in range (n + 1, len(a)):
            if (a[n] - a[g]) % 80 == 0:
                b.append(a[n] - a[g])
                k+=1
print(k, max(b))