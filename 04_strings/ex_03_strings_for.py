curso = "Redes de Computadores"

# Neste formato de for, usamos os indices os elementos
# Evitar esta forma e dar preferência às indicadas em seguida
# for i in range(len(curso)):
#     print(curso[i])

# Neste formato de FOR, o c assume cada caractere
for c in curso:
    print(c)

# Imprime o texto: posições pares em maiúsculo e ímpares em minúsculo
# Neste formato de FOR, o i assume os índices e c os caracteres
for i, c in enumerate(curso):
    if c == " ":
        print("_", end="")
    elif i % 2 == 0:
        print(c.upper(), end="")
    else:
        print(c.lower(), end="")

print()
