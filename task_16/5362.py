def fun(n):
    if n + 1 and n <= 2:
        return n + 1
    elif n > 2:
        return 2 * fun(n-1) + fun(n-2)
print(fun(4))