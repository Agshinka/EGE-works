b=[]
for n in range (1, 100):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s,2)
    if r > 52:
        b.append(r)
print(min(b))