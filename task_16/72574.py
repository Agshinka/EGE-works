import sys
sys.setrecursionlimit(5000)

def fun(n):
    if n < 3:
        return n
    if n >= 3:
        return fun(n-1) * fun(n-2)
print((fun(2025) - fun(2023)) // fun(2021))