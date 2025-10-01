# gethostname: retorna o nome de host
# gethostbyname: retorna o IP a partir do nome de host
# gethostbyname_ex: retorna o (nome de host, os alias, os IPs) a partir do nome de host
# gethostbyaddr: retorna o (nome de host, os alias, os IPs) a partir do IP

import socket

hostname = socket.gethostname()
print(hostname)

ip = socket.gethostbyname(hostname)
extras_por_nome = socket.gethostbyname_ex(hostname)
extras_por_ip = socket.gethostbyaddr(ip)

print(f"O IP de {hostname} é {ip}")
print(f"Extras sobre {hostname}: {extras_por_nome}")
print(f"Extras sobre {ip}: {extras_por_ip}")
print(10 * "-")

print(socket.gethostbyname_ex("suap.ifrn.edu.br"))
print(10 * "-")

print(socket.gethostbyname_ex("facebook.com"))
print(socket.gethostbyaddr(socket.gethostbyname("facebook.com")))
print(10 * "-")

print(socket.gethostbyname_ex("portal.ifrn.edu.br"))
print(10 * "-")

print(socket.gethostbyname_ex("tribunadonorte.com.br"))
print(10 * "-")
