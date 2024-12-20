k=0
for n in range (1, 1048577):
    if 1048576 % n == 0:
        k+=1
print(k)