with open('files/55604.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k=0
    j=[]
    for g in range (len(a)-1):
        x = a[g]
        y = a[g+1]
        if str(x)[-1] == str(y)[-1]:
            j.append(a[g])
    for n in range (len(a)-1):
        x = a[n]
        y = a[n+1]
        if (str(x)[-1] == str(y)[-2]):
            if ((a[n] % 7 == 0) + (a[n+1] % 7 == 0)) == 1:
                if (a[n] ** 2 + a[n + 1] ** 2) <= min(j) ** 2:
                    b.append(a[n] ** 2 + a[n+1] ** 2)
                    k+=1
print(k, max(b))