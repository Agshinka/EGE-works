for n in open('files/55596.txt'):
    a = [int(i) for i in n.split()]
    lines = [list(map(int, i.split())) for i in open('files/55596.txt')]
    numlist = [num for line in lines for num in line]
    good = [line for line in lines if any([line.count(g) == 1 and numlist.count(g) == 46 for g in line])]
    print(len(good))
