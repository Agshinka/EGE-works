with open('files/37131.txt', 'r') as file:
    a = file.readline()
    k = 0
    for n in range (1, len(a)):
        if (a[n] == 'K' and a[n-1] == 'L') or (a[n-1] == 'K' and a[n] == 'L'):
            k += 1
print(k)