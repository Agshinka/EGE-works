with open('files/39762.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    for n in range (len(a)-1):
        if (a[n] * a[n+1]) % 15 == 0 and (a[n] + a[n+1]) % 7 == 0:
            b.append(a[n] + a[n+1])
            k +=1
print(k, max(b))