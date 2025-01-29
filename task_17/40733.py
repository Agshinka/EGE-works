with open ('task_17/files/40733.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    j=[]
    t = 0
    for g in range (len(a)):
        if a[g] % 2 == 0:
            j.append(a[g])
            t += 1
    for n in range (len(a)-1):
        if ((a[n] % 3 == 0) + (a[n+1] % 3 == 0)) >= 1:
            if ((a[n] < (sum(j) // t)) + (a[n+1] < (sum(j) // t))) >= 1:
                k+=1
                b.append(a[n] + a[n+1])
print(k, max(b))