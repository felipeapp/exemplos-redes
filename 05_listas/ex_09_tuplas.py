# Podemos usar colcheter para criar uma lista
lista = ["Pablo", "Maria", "João"]

# Podemos usar parênteses para criar uma tupla
tupla = ("Pablo", "Maria", "João")

# Operações de leitura são permitidas
print(lista[1])
print(tupla[1])

# Operações de atualização não são permitidas
lista[2] = "Guilherme"
# tupla[2] = "Guilherme"

print(lista)
print(tupla)

print(f"Gerar uma tupla: {tuple(lista)}")
print(f"Gerar uma lista: {list(tupla)}")
