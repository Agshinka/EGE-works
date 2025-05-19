def fun(n):
    b = set()
    j=[]
    l=0
    for x in range(2, int(n ** 0.5)+1):
        if n % x == 0:
            b.add(x)
            b.add(n//x)
            b.add(n)
    b = sorted(list(b))
    for g in range (len(b)):
        k = b[g]
        l+=1
        if l >= 5:
            return k[0] * k[1] * k[2] * k[3] * k[4]
        else:
            return 0

print(fun(24))

