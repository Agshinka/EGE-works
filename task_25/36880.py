b=[]
for m in range (0, 50, 2):
    for n in range (1, 50, 2):
        N = 2 ** m * 3 ** n
        if N >= 400_000_000 and N <= 600_000_000:
            b.append(N)
print(sorted(b))