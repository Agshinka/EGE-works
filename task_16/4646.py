def fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return fun(n-1) * fun(n-2) + (n-2)
print(fun(5))