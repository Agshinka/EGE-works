def fun(n):
    if n < 10:
        return n
    elif n >= 10:
        return fun(n % 10) + fun(n // 10)
print(fun(159))