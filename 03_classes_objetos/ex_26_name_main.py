class Dispositivo:
    def __init__(self, nome: str) -> None:
        self.nome = nome


print("esta linha roda SEMPRE -- ate quando o arquivo e importado")

if __name__ == "__main__":
    print(f"__name__ vale: {__name__}")
    rt = Dispositivo("rt-core")
    print(f"teste rapido: {rt.nome}")
