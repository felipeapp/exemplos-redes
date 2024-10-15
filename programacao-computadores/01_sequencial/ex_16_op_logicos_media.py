nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite o número de faltas: "))

media = (2 * nota1 + 3 * nota2) / 5
aprovado = media >= 6 and faltas < 15

print("A média foi", media)
print("O aluno foi aprovado?", aprovado)
