def fun(n):
    if n <= 2:
        return 2
    elif n > 2:
        return fun(n-1) + 2 * fun(n-2)
print(fun(5))