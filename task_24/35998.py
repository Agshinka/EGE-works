with open('task_24/files/35998.txt', 'r') as file:
    a = file.readlines()
    b=[]
    for l in range (len(a)):
        if a[l].count('A') < 25:
            for i in range (len(a[l])):
                if a[l].count(a[l][i]) > 1:
                    d = a[l].rfind(a[l][i]) - a[l].find(a[l][i])
                    b.append(d)
print(max(b))