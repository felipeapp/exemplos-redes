nomes = ["Felipe", "Jefferson", "Gustavo", "Jéssica", "Mary"]

# É possível manipular listas com while, mas há formas melhores
i = 0
while i < len(nomes):
    print(f"O elemento da posição {i} é {nomes[i]}.")
    i += 1

print(30 * "-")

# Use esta forma quando precisar do índice e do elemento
for i, e in enumerate(nomes):
    print(f"O elemento da posição {i} é {e}.")

print(30 * "-")

# Use esta forma quando precisar apenas dos elementos
for e in nomes:
    print(e)
