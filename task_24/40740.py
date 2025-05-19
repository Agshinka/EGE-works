with open('files/40740.txt', 'r') as file:
    a = file.readline()
    a = a.split('A')
    b=[]
    maxx=0
    for n in a:
        if n.count('E') >= 3:
            b.append(len(n))
print(max(b))
