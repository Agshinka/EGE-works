with open('task_17/files/56545.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    j=[]
    for g in range (len(a)):
        if abs(a[g]) % 10 == 7:
            j.append(a[g])
    for n in range (len(a)-1):
        if (abs(a[n]) % 7 == 0 and abs(a[n+1]) % 7 != 0) or (abs(a[n]) % 7 != 0 and abs(a[n+1]) % 7 == 0):
            if (abs(a[n]) ** 2 + abs(a[n+1]) ** 2) <= min(j) ** 2:
                if abs(a[n]) % 10 == abs(a[n+1]) % 10:
                    k+=1
                    b.append(abs(a[n]) ** 2 + abs(a[n+1]) ** 2)
print(k, max(b))