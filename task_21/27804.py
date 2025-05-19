def fun(n, m):
    if n >= 68:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [fun(n + 1, m - 1), fun(n + 4, m - 1), fun(n * 5, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
print(min([s for s in range (1, 68) if not fun(s, 2) and fun(s, 4)]))