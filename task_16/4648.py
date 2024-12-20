def fun(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fun(n-2) + fun(n-1)
print(fun(8))