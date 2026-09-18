class Dispositivo:
    def __init__(self, nome: str) -> None:
        self.nome = nome


rt = Dispositivo("rt-core")
copia = rt

copia.nome = "novo-nome"

print(f"rt.nome   : {rt.nome}")
print(f"copia.nome: {copia.nome}")
print(f"e o mesmo objeto? {rt is copia}")

outro = Dispositivo("rt-core")
print(f"outro is rt: {outro is rt}")
