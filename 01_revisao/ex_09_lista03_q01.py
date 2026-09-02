quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um valor inteiro: "))

    if numero == 0:
        break

    quantidade += 1
    soma += numero

print(f"Quantidade de números: {quantidade}")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {soma / quantidade:.2f}")
