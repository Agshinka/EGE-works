with open('files/demo.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b=[]
    k=0
    for n in range (len(a)-1):
        if (a[n] % 16 == min(a) and a[n+1] % 16 != min(a)) or (a[n+1] % 16 == min(a) and a[n] % 16 != min(a)) or (a[n] % 16 == min(a) and (a[n+1] % 16 == min(a))):
            k+=1
            b.append(a[n] + a[n+1])
print(k, max(b))