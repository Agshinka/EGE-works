def fun(n, m):
    if n >= 39:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [fun(n + 1, m -1), fun(n * 3, m -1)]
    return any(h) if m % 2 != 0 else all(h)
print(min([s for s in range (1, 39) if not fun(s ,2) and fun(s, 4)]))