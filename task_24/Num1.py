# Num 1
# with open('files/52195.txt', 'r') as file:
#     a = file.readline().split('D')[1:-1]
#     k = 1
#     b = 0
#     for n in range (len(a)):
#         if a[n].count('O') <= 2:
#             k += len(a[n]) + 1
#             b = max(b, k)
#         else:
#             k = 1 
# print(b)
    

# Num 2   ???
# with open('files/59702.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):
#         if a[n].count('Y') <= 150:
#             g = max(k, g)
#             k += 1
#         else:
#             k = 0
# print(g)

# s = open('files/59702.txt').readline()[:-1]
# a = [i for i in range(len(s)) if s[i]=='Y']
# maxl = 0
# for i in range(150,len(a)):
#     maxl = max(a[i]-a[i-150],maxl)
#     print(maxl)

# Num 3 !!
# with open('files/37159.txt', 'r') as file:
#     a = file.readline()
#     k = 1
#     g = 1
#     for n in range (len(a)):
#         if (a[n] == 'd' and a[n+1] == 'a') or (a[n] == 'a' and a[n+1] == 'd'):
#             g = max(k, g)
#             k = 1
#         else:
#             k+=1
# print(g)

# Num 4 
with open('files/56552.txt', 'r') as file:
    a = file.readlines()
    k = 1
    g = 0
    for n in range (len(a)-1):
        if (a[n] == a[n+1]):
            k += 1
            g = max(k, g)
        else:
            k = 1
        cout = [[i, a[n].count(i)] for i in set(a[n])]
        print(n, g)

# Num 5 ??
# with open('files/56524.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a))


# Num 6
# with open('files/58326.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):
#         if a[n-1] > a[n]:
#             g += 1
#         else:
#             k = max(g, k)
#             g = 1
# print(k)

# Num 7 ??
# with open('files/56524.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):

# Num 8 ???
# with open('files/61404.txt', 'r') as file:
#     a = file.readline()
#     for n in range (len(a)):
#         if n.count('X') == 1 and n.count('Y'):
#             k = max(len(a[n]), k)
# print(k)

# Num 9
# with open('files/38602.txt', 'r') as file:
#     a = file.readline().split('PP')
#     k = 0
#     for n in range (len(a)):
#         k = max(len(a[n]), k)
# print(k+2)

# Num 10
# with open('files/59790.txt', 'r'):
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):


# Num 11
# with open('files/36879.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):

# Num 12
# print(len('DDDDDDDDDDD'))

# Num 13
# with open('files/51993.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):


# Num 14
# print(len('C'))

# Num 15
# with open('files/45258.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):

# Num 16
# with open('files/59793.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):

# Num 17
# with open('files/29672.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):
#         if n.count('E') > n.count('A'):
#             k+=1
#             g = max(k, g)
#         else:
#             k = 0
# print(g)

# Num 18
# with open('files/47021.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     g = 0
#     for n in range (len(a)):

# Num 19
# with open('files/27695.txt', 'r') as file:
#     a = file.readline()
#     k = 1
#     g = 0
#     for n in range (len(a)-1):
#         if a[n] != a[n+1]:
#             k+=1
#             g = max(k, g)
#         else:
#             k = 1
# print(g)

# Num 20
# with open('files/59849.txt', 'r') as file:
#     a = file.readline()
#     b = '0123456789ABCDEFGHIJKLMNOP'
#     k = ''
#     g = 0
#     for n in range (len(a)):
#         if a[n] in b:
#             k += a[n]
#             g = max(len(k), g)
#         else:
#             k = ''
# print(max(len(k), g))

# Способ:
# try:
#     print(int('10ghp', 26))
# except ValueError:
#     print('Плохой ввод')