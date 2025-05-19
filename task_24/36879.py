with open ('files/36879.txt', 'r') as file:
    a = file.readlines()
    b = []
    maxx = 0
    for n in range (len(a)):
        if a[n].count('G') <= 25:
            for g in a[n]:
                if a[n].rfind(g) - a[n].find(g):
                    maxx = max(maxx, a[n].rfind(g) - a[n].find(g))
print(maxx)