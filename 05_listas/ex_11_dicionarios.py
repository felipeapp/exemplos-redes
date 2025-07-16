# Podemos criar um dicionário informando chaves e valores
notas = {"Gustavo": 3, "Mary": 2, "Felipe": 10}

print(notas)

# Acessando elementos (primeira forma)
# print(notas["Ana"])
print(notas["Gustavo"])
print(notas["Mary"])
print(notas["Felipe"])

# Adicionando/atualizando elementos no dicionário
notas["Matheus"] = 9  # Chave não existe, adiciona a chave e o valor
notas["Mary"] = 9  # Chave existe, atualiza o valor
print(notas)

# Obter o tamanho do dicionário (quantidade de elementos)
print(len(notas))

# Teste se a chave existe ou não no dicionário
print("Mary" in notas)
print("Mary" not in notas)

# Remover um elemento
del notas["Felipe"]
print(notas)

# Acessar um elemento usando valor padrão (segunda forma)
print(notas.get("Mary"))
print(notas.get("Matheus"))
print(notas.get("Gustavo", 0))
print(notas.get("Felipe", 0))

# Retornar um conjunto a partir das chaves
print("Keys:", notas.keys())

# Retornar uma lista a partir dos valores
print("Values:", notas.values())

# Retornar uma lista de itens chave/valor
print("Itens:", notas.items())

# Usando for nas chaves do dicionário
for chave in notas:
    print(chave)

# Usando for nos valores do dicionário
for valor in notas.values():
    print(valor)

# Usando for nos itens do dicionário
for chave, valor in notas.items():
    print(f"A chave {chave} tem valor {valor}!")
