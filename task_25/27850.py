def fun(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

k=0
for n in range (245_690, 245_756 + 1):
    k+=1
    if fun(n):
        print(k, n)
