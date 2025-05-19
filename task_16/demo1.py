import sys
sys.setrecursionlimit(10000)
def fun(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * fun(n-1)
print((fun(2024) + 2 * fun(2023)) // fun(2022))