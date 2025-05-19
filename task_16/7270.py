import sys
sys.setrecursionlimit(1000)

def fun(n):
    if n == 1:
        return 1
    if n > 1:
        return fun(n-1) * (n + 2)
print(fun(5))