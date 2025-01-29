with open('files/37358.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    g = []
    b = []
    k = 0
    for n in range (len(a)-1):
        for j in range(n + 1, len(a)):
            if (a[n] + a[j]) % 10 == 0:
                b.append(a[n] + a[j])
                k+=1
print(k, max(b))