nomes = ["Jefferson", "Gustavo", "Jéssica", "Mary"]
print(nomes)

# Adiciona um elemento ao final da lista
nomes.append("Felipe")
nomes.append("Jamesson")
nomes += ["Carlos"]
print(nomes)

# Adiciona um elemento em uma posição específica, deslocando para a direita
nomes.insert(0, "João")
print(nomes)
nomes.insert(4, "Maria")
print(nomes)

# Remove a primeira ocorrência do elemento
nomes.remove("João")
nomes.remove("Maria")
print(nomes)

# Remove o elemento de um índice específico
elem = nomes.pop(1)
print(f"Elemento removido: {elem}")
elem = nomes.pop()  # Remove o último elemento
print(f"Elemento removido: {elem}")
print(nomes)

# Retorno o índice de um elemento
print(nomes.index("Mary"))

# Conta quantas vezes um elemento existe
print(nomes.count("Mary"))
print(nomes.count("Jamesson"))

# Verificar se um elemento pertence ou não a lista
print("Jamesson" in nomes)
print("Jamesson" not in nomes)

# Inverte a ordem dos elementos da lista
nomes.reverse()
print(nomes)

# Ordena os elementos da lista de forma crescente
nomes.sort()
print(nomes)

# Ordena os elementos da lista de forma decrescente
nomes.sort(reverse=True)
print(nomes)

# Realiza uma cópia da lista
copia1 = nomes.copy()
copia2 = nomes[:]
print(copia1)
print(copia2)

# Remove todos os elementos da lista
nomes.clear()
print(nomes)
