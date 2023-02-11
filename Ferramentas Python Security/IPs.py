import ipaddress #importando a bibilioteca IP Address

ip = "192.168.0.1"
ip_rede = "192.168.0.1/24"

endereco = ipaddress.ip_address(ip) #retornando uma string em forma de IP
rede = ipaddress.ip_network(ip, strict=False) #retornando uma string em forma de rede

for ip in rede: #criando um loop para verificar os ips na rede
    print(ip)

print(endereco)
print(rede)
