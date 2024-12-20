def fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return 2 * fun(n-1) + (n-2) * fun(n-2)
print(fun(6))