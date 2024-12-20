def fun(n):
    if n < 3:
        return 1
    elif n > 2:
        return sum([fun(i) for i in range (1, n)])
    
print(fun(18))