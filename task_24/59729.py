with open('files/59729.txt', 'r') as file:
    a = file.readline()
    k=0
    b=[]
    for n in range (len(a)-1):
        if a[n] + a[n+1] == 'TT':
            b.append(n)
    for g in range (0, len(b)-149):
        k = b[g + 149] - b[g] + 2
print(k)