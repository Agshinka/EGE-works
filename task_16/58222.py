def fun(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 != 0:
        return fun(n-1) + 3 * fun(n-2)
    elif n > 2 and n % 2 == 0:
        return sum([fun(i) for i in range (1, n)])
print(fun(28))