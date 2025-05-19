with open('task_17/files/73843.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    b = []
    k = 0
    g=[]
    for j in range (len(a)):
        g.append(a[j])
    for n in range (len(a)-2):
        elem = [a[n], a[n+1], a[n+2]]
        kr3 = [i for i in elem if i % 3 == (min(g) % 3)]
        kr7 = [i for i in elem if i % 7 == (max(g) % 7)]
        if len(kr3) == 1 and len(kr7) >= 2:
            k+=1
            b.append(a[n] + a[n+1] + a[n+2])
print(k, max(b))