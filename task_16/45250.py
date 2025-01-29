def fun(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return fun(n-2) + fun(n-1) - n
    if n > 2 and n % 2 != 0:
        return fun(n-1) - fun(n-2) + 2 * n
print(fun(32))