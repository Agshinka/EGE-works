def fun(n):
    if n >= 2025:
        return n
    elif n < 2025:
        return n + 3 + fun(n + 3)
print(fun(23) - fun(21))