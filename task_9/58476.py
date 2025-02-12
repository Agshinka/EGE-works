k = 0
for n in open('files/58476.txt'):
    a = sorted([int(i) for i in n.split()])
    pov = [i for i in a if a.count(i) > 1]
    nepov = [i for i in a if a.count(i) == 1]
    if len(pov) > 1:
        if a[-1] != a[-2]:
            if max(a) > ((3 * (sum(a) - max(a))) // 5):
                k+=1
print(k)