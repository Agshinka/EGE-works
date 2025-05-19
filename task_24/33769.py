with open('task_24/files/33769.txt', 'r') as file:
    a = file.readline()
    b=[]
    for n in range (len(a)-2):
        if (a[n] == a[n+1]):
            b.append(a[n+2])
print(sorted([[b.count(i), i] for i in set(b)]))