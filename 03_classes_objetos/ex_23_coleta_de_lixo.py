class Dispositivo:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __del__(self) -> None:
        print(f"   [o objeto {self.nome} foi liberado]")


print("criando...")
rt = Dispositivo("rt-core")
copia = rt

print("apagando a primeira referencia:")
del rt
print(f"   copia ainda funciona: {copia.nome}")

print("apagando a ultima referencia:")
del copia

print("fim do programa")
