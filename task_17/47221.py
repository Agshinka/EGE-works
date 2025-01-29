with open('files/47221.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    g=[]
    for j in range (len(a)):
        if abs(a[j]) % 10 == 3:
            g.append(a[j])
    for n in range (len(a)-1):
        l = (abs(a[n]) % 10 == 3 and abs(a[n+1])% 10 != 3) or (abs(a[n]) % 10 != 3 and abs(a[n+1])% 10 == 3)
        if l:
            if (abs(a[n]) ** 2 + abs(a[n+1]) ** 2) >= (max(g) ** 2):
                k+=1
                b.append(abs(a[n]) ** 2 + abs(a[n+1]) ** 2)
print(k, max(b))