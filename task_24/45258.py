with open('files/45258.txt', 'r') as file:
    a = file.readline()
    k=0
    a = a.replace('CB', '+')
    a = a.replace('AB', '+')
    a = a.replace('A', '-')
    a = a.replace('B', '-')
    a = a.replace('C', '-')
    a = a.split('-')
    for n in range (len(a)):
        k = max(len(a[n]), k)
print(k)