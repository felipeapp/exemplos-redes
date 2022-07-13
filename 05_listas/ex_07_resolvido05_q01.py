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
inversa = numeros[:]
inversa.reverse()
print(f"Lista invertida: {inversa}")
print(f"Lista original: {numeros}")

# Mostra todos os números pares e a quantidade deles
pares = 0
print("Números pares:", end=" ")
for elem in numeros:
    if elem % 2 == 0:
        pares += 1
        print(elem, end=" ")
print(f"\nQuantidade de números pares: {pares}")

# Mostra todos os números ímpares e a quantidade deles
impares = 0
print("Números impares:", end=" ")
for elem in numeros:
    if elem % 2 == 1:
        impares += 1
        print(elem, end=" ")
print(f"\nQuantidade de números ímpares: {impares}")

# Pegar o menor e o maior elemento da lista
menor = maior = numeros[0]

for elem in numeros:
    if elem < menor:
        menor = elem

    if elem > maior:
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
