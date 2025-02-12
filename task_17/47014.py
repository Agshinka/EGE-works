with open('files/47014.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    j=[]
    for g in range (len(a)):
        if a[g] % 2 != 0:
            j.append(a[g])
    for n in range (len(a)-1):
        if ((a[n] % 5 == 0) and a[n+1] < sum(j) // len(j)) or ((a[n+1] % 5 == 0) and a[n] < sum(j) // len(j)):
            b.append(a[n] + a[n+1])
            k+=1
print(k, max(b))