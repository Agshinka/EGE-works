a = '4230567458976345'
b = sum([int(i) for i in a])
k=0
for n in a:
    k += int(n)

print(b, k)