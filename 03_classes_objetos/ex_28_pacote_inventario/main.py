from inventario import Dispositivo, Rack

if __name__ == "__main__":
    dispositivos = [
        Dispositivo("rt-core", "10.0.0.1"),
        Dispositivo.de_texto("sw-01 ; 10.0.0.2 ; inativo ; 10"),
        Dispositivo("srv-web", "10.0.0.10", "ativo", 20),
    ]

    print("--- inventario ---")
    for d in dispositivos:
        print(d)

    rack = Rack("A1")
    for d in dispositivos:
        rack.adicionar(d)

    print("\n--- rack ---")
    print(rack)
    print(f"dispositivos criados no programa: {Dispositivo.quantos()}")

    print("\n--- tentando estragar ---")
    dispositivos[0].ip = "10.0.0.999"
    dispositivos[0].vlan = 9999
    print(f"continua valido: {dispositivos[0]}")
