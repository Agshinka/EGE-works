import sys
sys.setrecursionlimit(1000000)

def fun(n):
    if n < 11:
        return n
    elif n >= 11:
        return n + fun(n-1)
print(fun(2024)-fun(2021))