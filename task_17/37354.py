with open('files/37354.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k=0
    for n in range (len(a)-1):
        for g in range (n+1, len(a)):
            if (a[n] + a[g])%2 !=0 and (a[n] * a[g]) % 5 == 0:
                k+=1
                b.append(a[n] + a[g])
print(k, max(b))