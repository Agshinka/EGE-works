def fun(n, m):
    if n >= 41:
        return m % 2 == 0
    if m == 0:
        return 0
    if n % m == 0:
        h = [fun(n + (n // m),m -1)]
        return any(h) if m % 2 != 0 else all(h)
print(max([s for s in range (1, 41) if not fun(s, 2) and fun(s, 4)]))