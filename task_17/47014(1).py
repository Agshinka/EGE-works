with open('files/47014.txt' ,'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b=[]
    k=0
    j=[]
    for g in range (len(a)):
        if a[g] % 2 != 0:
            j.append(a[g])
    for n in range (len(a)-1):
        sr = sum(j) / len(j)
        if (a[n] % 5 == 0 and (a[n+1] < sr)) or ((a[n] < sr) and (a[n+1] % 5 == 0)):
            k+=1
            b.append(a[n] + a[n+1])
print(k, max(b))