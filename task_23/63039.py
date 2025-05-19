def fun(n, m, k):
    if n > m + 1:
        return 0
    if n == m:
        return 1
    else:
        if k == 1:
            return fun(n * 2, m, k-1) + fun(n * 3, m, k-1)
        else:
            return fun(n-1, m, k+1) + fun(n * 2, m, k) + fun(n * 3, m, k)
print(fun(3, 20, 0))