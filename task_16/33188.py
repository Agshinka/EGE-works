def fun(n):
    if n == 0:
        return 0
    elif n % 3 == 0 and n > 0:
        return n + (fun(n-3))
    elif n % 3 > 0:
        return n + fun(n-(n % 3))
print(fun(22))