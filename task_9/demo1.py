k=0
for n in open('files/demo.txt'):
    a = [int(i) for i in n.split()]
    pov = [i for i in a if a.count(i) == 3]
    nepov = [i for i in a if a.count(i) == 1]
    summ = sum(pov)
    summ1 = sum(nepov)
    if (len(pov) == 3 and len(nepov) == 3) and (summ ** 2 > summ1 ** 2):
        k+=1
print(k)
