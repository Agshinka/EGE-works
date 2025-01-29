from ipaddress import *
k = 0
net = ip_network('112.160.0.0/255.240.0.0', 0)
for ip in net:
    a = bin(int(ip))[2:].zfill(32)
    if a.count('1') % 5 != 0:
        k+=1
print(k)