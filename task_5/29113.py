for n in range (128, 256):
    s = bin(n)[2:]
    s = s.replace('0', '+')
    s = s.replace('1', '-')
    s = s.replace('+', '1')
    s = s.replace('-', '0')
    r = int(s, 2)
    g = n - r
    if g == 185:
        print(n)
        