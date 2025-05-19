with open('files/58484.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    j=[]
    for g in range (len(a)):
        if (len(str(a[g])) == 3) and a[g] % 10 == 5:
            j.append(a[g])
    for n in range (len(a)-2):
        elem = [a[n], a[n+1]]
        qlen = [len(str(i)) for i in elem]
        if f'{qlen[0]}{qlen[1]}'.count('4') == 1:
            if ((a[n] ** 2) + (a[n + 1] ** 2)) % min(j) == 0:
                b.append((a[n] ** 2) + (a[n + 1] ** 2))
                k+=1
print(k, max(b))