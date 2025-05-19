with open('files/37359.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    for n in range (len(a)-1):
        for g in range (n + 1, len(a)):
            if (a[n] + a[g]) % 117 == 0:
                b.append(a[n] + a[g])
                k+=1
print(k, max(b))