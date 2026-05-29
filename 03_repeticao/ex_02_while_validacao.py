while True:
    media = float(input("Digite a sua média: "))

    if 0 <= media <= 10:
        break

    print("Média inválida!")

if media >= 6:
    print("Aprovado!")
elif media < 2:
    print("Reprovado!")
else:
    print("Recuperação")
