with open('files/38602.txt', 'r') as file:
    a = file.readline()
    b=[]
    k=0
    for n in range (len(a)-1):
        if a[n] == 'P' and a[n+1] == 'P':
            k = 1
        else:
            k+=1
            b.append(k)
print(max(b))