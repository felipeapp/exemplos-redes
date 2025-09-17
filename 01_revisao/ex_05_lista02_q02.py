nota1 = float(input("Digite a primeira nota: "))

if 0 <= nota1 <= 10:
    nota2 = float(input("Digite a segunda nota: "))

    if 0 <= nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f"A média é {media:.2f}")

        if media >= 7:
            print("Aprovado")
        elif media >= 4:
            print("Prova final")
        else:
            print("Reprovado")
    else:
        print("Nota 2 inválida, as notas devem estar entre 0 e 10.")
else:
    print("Nota 1 inválida, as notas devem estar entre 0 e 10.")
