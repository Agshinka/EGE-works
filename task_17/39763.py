with open('files/39763.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    for n in range (len(a)-2):
        s = sorted([a[n], a[n+1], a[n+2]])
        if s[2] ** 2 < (s[1] ** 2 + s[0] ** 2):
            b.append(a[n] + a[n+1] + a[n+2])
            k+=1
print(k, max(b))