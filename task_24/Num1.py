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
    

# Num 2
# with open('files/59702.txt', 'r') as file:
#     a = file.readline().split(a)[1:-1]
#     k = 0
#     for n in range (len(a)):
#         if n.count('Y') == 150:
#             k+=1
# print(k)

# Num 12
# print(len('DDDDDDDDDDD'))

# Num 13
# print(len('C'))

# Num 17
# with open('files/29672.txt', 'r') as file:
#     a = file.readline()
#     k = 0
#     for n in range (len(a)):
#         if n.count('E') > n.count('A'):
#             k+=1
# print(k)

# Num 9
# with open('files/38602.txt', 'r') as file:
#     a = file.readline().split('PP')
#     k = 0
#     for n in range (len(a)):
#         k = max(len(a[n]), k)
# print(k+2)

# Num 20

# def fun(n):
#     s = ''
#     while n != 0:
#         s = str(n%26) + s
#         n = n//26

with open('files/59849.txt', 'r') as file:
    a = file.readline()
    b = '0123456789ABCDEFGHIJKLMNOP'
    k = ''
    g = 0
    for n in range (len(a)):
        if a[n] in b:
            k += a[n]
            g = max(len(k), g)
        else:
            k = ''
print(max(len(k), g))

# Способ:
# try:
#     print(int('10ghp', 26))
# except ValueError:
#     print('Плохой ввод')