contador = 0
maior = 0
somatorio = 0

while True:
    numero = int(input("Digite um número inteiro positivo: "))

    if numero > 0:
        print("Valor válido!")

        # if numero > maior:
        #     maior = numero
        maior = max(numero, maior)

        somatorio += numero
        contador += 1
    elif numero == 0:
        print("Leitura finalizada!")
        break
    else:
        print("Valor inválido, será desconsiderado!")

print(30 * "-")
print(f"Quantidade de números digitados foi {contador}.")
print(f"O maior número digitado foi {maior}.")
print(f"A média aritmética dos números foi {somatorio / contador:.2f}.")
