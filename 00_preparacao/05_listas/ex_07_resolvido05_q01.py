while True:
    n = int(input("Digite a quantidade de elementos: "))
    if n > 0:
        break
    print("A quantidade deve ser maior que zero!")

numeros = []

for i in range(n):
    elem = int(input(f"Digite o elemento {i + 1}: "))
    numeros.append(elem)

# Invertendo a lista original
inversa = numeros.copy()
inversa.reverse()
print(f"Lista invertida: {inversa}")
print(f"Lista original: {numeros}")

# Mostra todos os números pares/ímpares e a quantidade deles
pares = []
impares = []

for n in numeros:
    pares.append(n) if n % 2 == 0 else impares.append(n)

print(f"Números pares: {pares}")
print(f"Total de pares: {len(pares)}")
print(f"Números ímpares: {impares}")
print(f"Total de ímpares: {len(impares)}")

# Pegar o menor e o maior elemento da lista
menor = maior = numeros[0]

for elem in numeros:
    if elem < menor:  # noqa: PLR1730
        menor = elem

    if elem > maior:  # noqa: PLR1730
        maior = elem

print(f"Menor elemento (manual): {menor}")
print(f"Maior elemento (manual): {maior}")
print(f"Menor elemento (função): {min(numeros)}")
print(f"Maior elemento (função): {max(numeros)}")

# Conta quantas vezes cada elemento aparece na lista
contados = []

for elem in numeros:
    if elem not in contados:
        print(f"O número {elem} aparece {numeros.count(elem)} vez(es)!")
        contados.append(elem)
