import sys
sys.setrecursionlimit(1000000)

def fun(n):
    if n == 1:
        return n
    elif n > 1:
        return n - 1 + fun(n-1)
print(fun(2024) - fun(2022))