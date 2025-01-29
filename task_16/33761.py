def fun(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return fun(n // 2)
    if n % 2 != 0:
        return 1 + fun(n-1)

k = 0
while fun(k) != 11:
    k+=1
print(k)