# print(73 | 54) #побитывая дизъюнкция
# print(39 & 325) #побитывая конъюкция

from ipaddress import *
# ind=1
# adress=IPv4Address('212.165.94.118')
# network=ip_network('212.165.94.118/255.255.255.0',0) #ip узла/маска -> ip в сети
# for host in network.hosts():
#     if host!=adress:
#         ind+=1
#     else:
#         print(ind)
#         break

# adress=IPv4Address('234.156.48.153')
# raw_network=IPv4Address('234.156.32.0')
# for mask in range(33):
#     network=ip_network(f'{raw_network}/{mask}',0)
#     if network.network_address==raw_network and adress in network:
#         print(network.netmask)

counter=0
adress=IPv4Address('115.212.110.50')
raw_network=IPv4Address('231.192.30.160')
mask=IPv4Address('255.255.255.240')
network=ip_network(f'{raw_network}/{mask}',0)
print(network)
for host in network.hosts():
    if sum([bin(int(el))[2::].count("1") for el in str(host).split('.')])%2==0:
        counter+=1
print(counter)
