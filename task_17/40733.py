with open ('files/40733.txt', 'r') as file:
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
        sr = sum(j) // t
        if (a[n] % 3 == 0 or a[n+1] % 3 == 0) and ((a[n] < sr) or (a[n+1] < sr)):
            k+=1
            b.append(a[n] + a[n+1])
print(k, max(b))