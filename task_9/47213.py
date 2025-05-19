k=0
for n in open('files/47213.txt', 'r'):
    a = [int(i) for i in n.split()]
    pov = [i for i in a if a.count(i) == 2]
    nepov = [i for i in a if a.count(i) == 1]
    if len(pov) == 2 and len(nepov) == 4 and (sum(nepov) / len(nepov)) <= (sum(pov)):
        k+=1
print(k)