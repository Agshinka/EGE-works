def fun(a):
    s = ''
    while a != 0:
        s = str(a % 3) + s
        a = a//3
    return s

b=[]
for n in range (1, 10000):
    s = fun(n) 
    s = s + fun(n % 3)
    r = int(s,3)
    if r >= 1000 and r < 10000:
        b.append(r)
        print(min(b))