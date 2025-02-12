k=0
for n in range (1100000000, 1987653211):
    if n % 16 in [10, 15] or n % 8 in [0, 3]:
        k+=1
print(k)