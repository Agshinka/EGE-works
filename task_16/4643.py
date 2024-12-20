def fun(n):
    if n == 1:
        return 1
    else:
        return 5 * fun(n-1) + 3 * n
print(fun(4))