k=0
for n in open('files/38943.txt'):
    a = sorted([int(i) for i in n.split()])
    if (a[0] ** 2 + a[1] ** 2) > a[2] ** 2:
        k+=1
print(k)
