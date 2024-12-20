def fun(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return fun(n-1) + 1
    elif n % 2 == 0 and n > 0:
        return fun(n//2)
print(fun(2))