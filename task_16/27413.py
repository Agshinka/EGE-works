def fun(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + fun(n-1)
    elif n > 1 and n % 2 != 0:
        return 2 * fun(n-2)
print(fun(26))