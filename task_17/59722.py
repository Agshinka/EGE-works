with open('task_17/files/59722.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    h=[]
    k=0
    j=0
    for g in range (len(a)):
        if a[g] % 100 == 17:
            h.append(a[g])
    for n in range (len(a)-2):
        elem = [a[n], a[n+1], a[n+2]]
        qlen = [len(str(i)) for i in elem]
        if (a[n] + a[n+1] + a[n+2]) < max(h):
                if f'{qlen[0]}{qlen[1]}{qlen[2]}'.count('3') == 1:
                    j+=1
print(j)
