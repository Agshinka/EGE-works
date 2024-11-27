with open('files/37345.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k=0
    for n in range (len(a)-1):
        for g in range (n+1, len(a)):
            if (a[n] * a[g]) % 62 == 0:
                k+=1
                b.append(a[n] + a[g])
print(k, max(b))
