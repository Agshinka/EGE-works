k=0
for n in range (1_222_222_222, 1_555_555_667):
    s = bin(n)[2:]
    s = s + bin(n%3)[2:]
    s = s + bin(n % 3)[2:]
    r = int(s,2)
    k+=1
print(k)