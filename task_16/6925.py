def fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n > 3:
        return fun(n-3) * n
print(fun(11))