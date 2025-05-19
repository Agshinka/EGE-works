k=0
for n in open('files/48430.txt'):
    a = [int(i) for i in n.split()]
    pov = [i for i in a if a.count(i) == 2]
    nepov = [i for i in a if a.count(i) == 1]
    if len(pov) == 4 and len(nepov) == 2:
        if (sum(pov) // 2) < (sum(nepov)):
            k+=1
print(k)