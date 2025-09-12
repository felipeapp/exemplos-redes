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

# Declarar uma lista de apenas um elemento
lista_1_valor = [10]
print(lista_1_valor)

# Declarar uma tupla de apenas um elemento
tupla_1_valor = (10,)
print(tupla_1_valor)
