def fun(n):
    if n <= 1:
        return 0
    if n % 2 != 0 and n > 1:
        return fun(n-1) + 3 * n * n
    if n > 1 and n % 2 == 0:
        return n // 2 + fun(n-1) + 2
print(fun(49))