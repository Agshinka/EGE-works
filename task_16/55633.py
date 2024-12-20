# def fun (a, b):
#     if a == 0:
#         return a
#     elif b > 0 and a >= b:
#         return fun(a-b, b)
#     elif a < b:
#         return fun(b, a)

# k=0
# for n in range (123456798, 1234567886):
#     if (fun(n,15) == 1):
#         k+=1
# print(k)

del_3 = len(range (123456798, 1234567885, 3))
del_5 = len(range (123456798, 1234567885, 5))
del_15 = len(range (123456798, 1234567885, 15))
print(len(range(123456798, 1234567885))- del_3 - del_5 + del_15)