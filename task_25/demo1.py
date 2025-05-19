# from fnmatch import *
# for n in range (0, 10 ** 10, 1917):
#     if fnmatch(str(n), '3?12?14*5'):
#         print(n, n // 1917)

def fun(n):
    b = []
    for x in range (2, n):
        if n % x == 0:
            b.append(n // x)
    return sorted(b)

for n in range (800_000, 850_000):
    num = fun(n)
    if len(num) != 0:
        if (min(num) + max(num)) % 10 == 4:
            print(n, min(num) + max(num))