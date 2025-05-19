with open('task_26/files/36881.txt', 'r') as file:
    a = file.readlines()
    j=[]
    del a[0]
    a = [int(i) for i in a]
    # print(a)
    k=0
    for n in range (len(a)-1):
        for g in range (n + 1, len(a)):
            # print('p: ', a[n], a[g])
            if (a[n] % 2 == 0 and a[g] % 2 == 0) or (a[n] % 2 != 0 and a[g] % 2 != 0):
                # print('p2: ', a[n], a[g])
                if (a[n] + a[g]) in a:
                    # print('p3: ', a[n], a[g])
                    k+=1
                    j.append(a[n] + a[g])
print(k, max(j))