for n in range (1,10000):
    s = bin(n)[2:]
    s = s.replace('0', '+')
    s = s.replace('1', '0')
    s = s.replace('+', '1')
    s.strip('0')
    r = int(s,2)
    if n - r == 999:
        print(n)
        break