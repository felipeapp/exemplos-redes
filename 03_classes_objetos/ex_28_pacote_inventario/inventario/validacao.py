STATUS_VALIDOS = ("ativo", "inativo", "manutencao")
VLAN_MINIMA = 1
VLAN_MAXIMA = 4094


def ip_valido(texto: str) -> bool:
    partes = str(texto).split(".")
    if len(partes) != 4:
        return False
    return all(p.isdigit() and 0 <= int(p) <= 255 for p in partes)


def vlan_valida(numero: int) -> bool:
    return isinstance(numero, int) and VLAN_MINIMA <= numero <= VLAN_MAXIMA


def status_valido(texto: str) -> bool:
    return str(texto).strip().lower() in STATUS_VALIDOS


if __name__ == "__main__":
    print(f"ip_valido('10.0.0.1')   : {ip_valido('10.0.0.1')}")
    print(f"ip_valido('10.0.0.999') : {ip_valido('10.0.0.999')}")
    print(f"vlan_valida(4095)       : {vlan_valida(4095)}")
    print(f"status_valido(' ATIVO '): {status_valido(' ATIVO ')}")
