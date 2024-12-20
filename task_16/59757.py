import sys
sys.setrecursionlimit(10000000)

def fun(n):
    if n < 9:
        return n
    elif n >= 9:
        return fun(n % 9) + fun(n // 9)

k=0
for n in range (4 * 6 ** 20, 5 * 6 ** 20 + 1):
    if fun(n) == 121:
        k+=1
print(k)
