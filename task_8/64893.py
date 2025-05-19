def fun(n):
    s = str(n)
    if len(s) == 12:
        return 1
    b=[]
    for g in range (9):
        summ = int(s[-1]) + g
        if (summ % 2 == 0) and (g < int(s[-1])):
            b.append(int(s + str(g)))
        if (summ % 2 != 0) and (g > int(s[-1])):
            b.append(int(s + str(g)))
    return sum(fun(n) for n in b)
print(sum(fun(g) for g in range (1, 9)))


# def f(n):
#     s = str(n)
#     if len(s) == 12:
#         return 1
#     podr = []
#     for i in range(9):
#         if (int(s[-1]) + i) % 2 == 0 and i > int(s[-1]):
#             podr.append(int(s + str(i)))
#         if (int(s[-1]) + i) % 2 != 0 and i < int(s[-1]):
#             podr.append(int(s + str(i)))
#     return sum(f(i) for i in podr)
# print(sum(f(i) for i in range(1, 9)))