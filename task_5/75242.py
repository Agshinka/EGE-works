def fun(a):
    s = ''
    while a!=0:
        s = str(a % 3) + s
        a = a//3
    return s
for n in range (1,10000000):
    s = fun(n)
    s = s.replace('0', '+')
    s = s.replace('2', '0')
    s = s.replace('+', '2')
    g = int(str(int(s)),3)
    r = abs(n - g)
    if r == 1_864_246:
        print(n)
        break