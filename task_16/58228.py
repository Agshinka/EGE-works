def fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return (4 * n - fun(n-3)) // 8
    elif n > 2 and n % 2 != 0:
        return (4 * n - fun(n-1) + fun(n-2)) // 8
print(fun(52) - fun(38))