def fun(n):
    if n <= 2:
        return 2
    if n > 2:
        return fun(n-1) + 3 * fun(n-2)
print(fun(5))