def fun(n):
    if n > 1000000:
        return n
    elif n <= 1000000:
        return n + fun(2*n)
def fug(n):
    return fun(n) / n

k=0
for g in range (1, 10001):
    if fug(g) == fug(2000):
        k+=1
print(k)