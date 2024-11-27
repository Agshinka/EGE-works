with open('files/45228.txt', 'r') as file:
    a = file.readline()
    cout = 0
    k = 0
    for n in range (len(a)-2):
        s = a.replace('A', '+')
        s = a.replace('C', '-')
        s = a.replace('D', '-')
        s = a.replace('F', '-')
        s = a.replace('O', '+')
        if a[n] == '-' and a[n+1] == '+' and a[n+2] == '-':
            k = max(len(a[n], k))
print(k)