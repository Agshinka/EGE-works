with open('files/69932.txt', 'r') as file:
    a = file.read()
    k=0
    maxx = 0
    for n in range (len(a)-1):
        if (a[n] in '6780') or (a[n-1] in '678' and a[n+1] in '678' and k!=0):
            k+=1
        else:
            maxx = max(maxx, k)
            k=0
print(maxx)