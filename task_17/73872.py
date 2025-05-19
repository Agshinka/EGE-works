with open('task_17/files/73872.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    j=[]
    for g in range (len(a)):
        j.append(a[g])
    for n in range (len(a)-2):
        elem = [a[n], a[n+1], a[n+2]]
        kr3 = [i for i in elem if i % 3 == (max(j) % 3)]
        kr7 = [i for i in elem if i % 7 == (min(j) % 7)]
        if len(kr3) == 1 and len(kr7) >= 2:
            k+=1
            b.append(sum(elem))
print(k, max(b))