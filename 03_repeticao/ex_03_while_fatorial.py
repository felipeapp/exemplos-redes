while True:
    n = int(input("Digite um valor maior ou igual a zero: "))

    if n >= 0:
        break

    print("Valor inválido, tente novamente!")

cont = n
fatorial = 1

while cont > 1:
    fatorial *= cont
    cont -= 1

print(f"O fatorial de {n} é {fatorial}.")
