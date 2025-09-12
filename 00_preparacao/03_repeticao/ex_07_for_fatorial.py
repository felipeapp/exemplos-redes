while True:
    n = int(input("Digite um valor maior ou igual a zero: "))

    if n >= 0:
        break

    print("Valor inválido, tente novamente!")

fatorial = 1

for i in range(n, 1, -1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}.")
