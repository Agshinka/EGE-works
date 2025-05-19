from math import dist

with open('files/7581a.txt', 'r') as file:
    a = file.readlines()
    a = [[float(i.split()[0].replace(',', '.')), float(i.split()[1].replace(',', '.'))] for i in a]
    d = 1
    p = [1, 2]
    q = [5, 2]
    print(dist(p, q))
    # for n in range (len(a)):
    #     for p in a[n]:
    #         point = [j for j in a if dist([p], j) < d]
    #         print(point)