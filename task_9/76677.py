k=0
for n in open('files/76677.txt'):
    a = [int(i) for i in n.split()]
    sr = (sum(a) / len(a))
    zamch = [i for i in a if i > sr and (i % 2 == 0)]
    zamnech = [i for i in a if i > sr and (i % 2 != 0)]
    chet = [i for i in a if (i % 2 == 0)]
    nechet = [i for i in a if (i % 2 != 0)]
    if len(zamch) > len(zamnech) and sum(chet) < sum(nechet):
        k+=1
print(k)