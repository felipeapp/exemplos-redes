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

print(f"Converter a lista para tupla: {tuple(lista)}")
print(f"Converter a tupla para lista: {list(tupla)}")
