def fun(n):
    if n > 2024:
        return n
    elif n <= 2024:
        return n * fun(n+1)
print(fun(2022) / fun(2024))