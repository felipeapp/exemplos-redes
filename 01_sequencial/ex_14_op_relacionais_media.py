nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (2 * nota1 + 3 * nota2) / 5
aprovado = media >= 6

print("A média foi", media)
print("O aluno foi aprovado?", aprovado)
