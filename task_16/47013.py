k=0
for n in range (2, 100):
    for g in range (0, n):
        for j in range (0, g):
            if (2 ** n + 2 ** g + 2 ** j) < 1000000000:
                k+=1
print(k)