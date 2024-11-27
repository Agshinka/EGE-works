# with open('files/59722.txt', 'r') as file:
#     a = file.readlines()
#     a = [int(i) for i in a]
#     b = []
#     h=[]
#     k=0
#     j=0
#     for g in range (len(a)):
#         if a[g] % 100 == 17:
#             h.append(a[g])
#     for n in range (len(a)-2):
#         if (a[n] > 99 and a[n] < 1000) or (a[n+1] > 99 and a[n+1] < 1000) or (a[n+2] > 99 and a[n+2] < 1000):
#             k+=1
#             if k == 1 and (a[n] + a[n+1] + a[n+2] < max(h)):
#                 j+=1
# print(j)
