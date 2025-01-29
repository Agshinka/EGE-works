with open('task_17/files/38951.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    for n in range (len(a)-1):
        if (a[n] % 3 == 0 or a[n+1] % 3 == 0):
            if (a[n] + a[n+1]) % 5 == 0:
                k+=1
                b.append(a[n] + a[n+1])
print(k, max(b))