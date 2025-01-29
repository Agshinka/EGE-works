# print(bin(143)[2:], bin(131)[2:], bin(211)[2:], '00' + bin(37)[2:])

# print(bin(231)[2:], '00' + bin(32)[2:], bin(240)[2:], '0' * 8)

from ipaddress import *
k = 0
net = ip_network('143.131.211.37/255.255.240.0', 0)
for ip in net:
    a = bin(int(ip))[2:].zfill(32)
    if a.count('1') == 10:
        print(a.count('1'))