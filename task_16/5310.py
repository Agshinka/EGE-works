def fun(n):
    if n == 1:
        return 1
    elif n > 1:
        return 2 * fun(n-1)+1
print(fun(6))