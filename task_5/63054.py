k=0
for n in range (0,100):
    s = bin(n)[2:]
    s = s + bin(n % 4)[2:]
    r = int(s,2)
    if r >= 0 and r <= 65:
        k+=1
print(k)