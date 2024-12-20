with open('files/51986.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    h=[]
    k=0
    for g in range (len(a)):
        if abs(a[g]) % 10 == 5:
            h.append(a[g])
    for n in range (len(a)-1):
        if (abs(a[n]) ** 2 + abs(a[n+1]) ** 2) < min(h) ** 2:
                k+=1
                b.append(abs(a[n]) ** 2 + abs(a[n+1]) ** 2)
print(k, max(b))