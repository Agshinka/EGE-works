def fun(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * fun(n-1)
print(fun(2023))
print(fun(2020))