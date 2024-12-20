def fun(n):
    if n == 1:
        return 0
    else:
        return fun(n-1)+n

def fun1(g):
    if g == 1:
        return 1
    else:
        return fun1(g-1) * g
print(fun(5) + fun1(5))