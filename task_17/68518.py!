with open('files/68518.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    h = []
    k = 0
    for g in range (len(a)):
        if a[g] % 19 == 0:
            h.append(a[g])
    for n in range (len(a)-1):
        if (a[n] % min(h) == 0) or a[n+1] % min(h) == 0:
            b.append(a[n] + a[n+1])
            k+=1
print(k, max(b))