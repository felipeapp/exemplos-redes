n1 = float(input("Digite a primeira nota: "))

if 0 <= n1 <= 10:
    n2 = float(input("Digite a segunda nota: "))

    if 0 <= n2 <= 10:
        n3 = float(input("Digite a terceira nota: "))

        if 0 <= n3 <= 10:
            n4 = float(input("Digite a quarta nota: "))

            if 0 <= n4 <= 10:
                faltas = int(input("Digite o número de faltas: "))

                if 0 <= faltas <= 60:
                    media = (2 * n1 + 2 * n2 + 3 * n3 + 3 * n4) / 10
                    print(f"A média foi {media:.2f}!")

                    if faltas > 20:
                        print("Reprovado por faltas!")
                    elif media >= 9:
                        print("Aprovado com louvor!")
                    elif media >= 7:
                        print("Aprovado!")
                    elif media >= 3:
                        print("Recuperação!")
                    else:
                        print("Reprovado por média!")
                else:
                    print("Número de faltas inválido!")
            else:
                print("Nota 4 inválida!")
        else:
            print("Nota 3 inválida!")
    else:
        print("Nota 2 inválida!")
else:
    print("Nota 1 inválida!")
