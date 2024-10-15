while True:
    quantidade = int(input("Quantos alunos existem na turma: "))
    if quantidade > 0:
        break
    print("Quantidade inválida, tente novamente!")

contador = 1

while contador <= quantidade:
    print(30 * "-")

    while True:
        nota1 = float(input(f"Digite a primeira nota do aluno {contador}: "))
        if 0 <= nota1 <= 10:
            break
        print("Primeira nota inválida, tente novamente!")

    while True:
        nota2 = float(input(f"Digite a segunda nota do aluno {contador}: "))
        if 0 <= nota2 <= 10:
            break
        print("Segunda nota inválida, tente novamente!")

    media = (nota1 + nota2) / 2
    print(f"A média do aluno {contador} é {media:.2f}")

    if media >= 6:
        print(f"O aluno {contador} está aprovado!")
    elif media < 2:
        print(f"O aluno {contador} está reprovado!")
    else:
        print(f"O aluno {contador} está em recuperação!")

    contador += 1
