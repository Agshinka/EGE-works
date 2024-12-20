def fun(n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return (n%10) * fun(n//100)
    elif n > 0 and n % 2 == 0:
        return fun(n//100)

k = 0
for n in range (10 ** 7, 9 * 10 ** 7 + 1):
    if fun(n) == 25:
        k+=1
print(k)