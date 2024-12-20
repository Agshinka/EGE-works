def fun(n):
    if n <= 2:
        return 1
    elif n > 2:
        return 2 * fun(n-1) + fun(n-2)
print(fun(6))