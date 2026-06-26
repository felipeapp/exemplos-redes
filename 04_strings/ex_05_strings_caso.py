texto = input("Digite um texto qualquer: ")
resultado = ""

for i, c in enumerate(texto):
    resultado += c.upper() if i % 2 == 0 else c.lower()
    # if i % 2 == 0:
    #     resultado += c.upper()
    # else:
    #     resultado += c.lower()

print(f"Texto divertido: {resultado}")
