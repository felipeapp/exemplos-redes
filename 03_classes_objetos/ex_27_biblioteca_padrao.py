import ipaddress


def ip_valido_caseiro(texto: str) -> bool:
    partes = str(texto).split(".")
    return len(partes) == 4 and all(p.isdigit() for p in partes)


def ip_valido(texto: str) -> bool:
    try:
        ipaddress.ip_address(str(texto))
        valido = True
    except ValueError:
        valido = False
    return valido


testes = ["10.0.0.1", "10.0.0.999", "10.0.0", "192.168.000.1", "::1"]

print(f"{'ENTRADA':<16} {'CASEIRO':<10} {'BIBLIOTECA'}")
for t in testes:
    print(f"{t:<16} {ip_valido_caseiro(t):<10} {ip_valido(t)}")

rede = ipaddress.ip_network("10.0.0.0/24")
print(f"\nrede: {rede}")
print(f"mascara: {rede.netmask}")
print(f"10.0.0.5 pertence a rede? {ipaddress.ip_address('10.0.0.5') in rede}")

print("hosts:")
for ip in rede.hosts():
    print(ip, end=" ")
print()
