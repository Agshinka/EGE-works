with open('files/64947.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b=[]
    t=0
    k=0
    p=0
    j=[]
    for g in range (len(a)):
        if a[g] % 1000 == 832:
            j.append(a[g])
    for n in range (len(a)-2):
        elem = [a[n], a[n+1], a[n+2]]
        qlen = [len(str(i)) for i in elem]
        if f'{qlen[0]}{qlen[1]}{qlen[2]}'.count('4') >= 1:
            if ((a[n] % 5 == 0) + (a[n+1] % 5 == 0) + (a[n+2] % 5 == 0)) > ((a[n] % 3 == 0) + (a[n+1] % 3 == 0) + (a[n+2] % 3 == 0)):
                if (a[n] + a[n+1] + a[n+2]) > max(j):
                    b.append(a[n] + a[n+1] + a[n+2])
                    k+=1
print(k, max(b))
