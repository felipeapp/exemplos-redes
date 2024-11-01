# gethostname: retorna o nome de host
# gethostbyname: retorna o IP a partir do nome de host
# gethostbyname_ex: retorna o (nome de host, os alias, os IPs) a partir do nome de host
# gethostbyaddr: retorna o (nome de host, os alias, os IPs) a partir do IP

import socket

host = socket.gethostname()
print(f"Meu hostname é {host}.")
print(30 * "-")

ip = socket.gethostbyname(host)
print(f"Meu endereço IP é {ip}.")
print(30 * "-")

name, alias, ips = socket.gethostbyname_ex(host)
print(f"Hostname: {name}")
print(f"Alias: {alias}")
print(f"Endereços IP: {ips}")
print(30 * "-")

name, alias, ips = socket.gethostbyaddr(ip)
print(f"Hostname: {name}")
print(f"Alias: {alias}")
print(f"Endereços IP: {ips}")
