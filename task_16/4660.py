def fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return (fun(n-1) - fun(n-2)) * n
print(fun(8))