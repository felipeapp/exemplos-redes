nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
faltas = int(input("Digite o número de faltas: "))

media = (2 * nota1 + 2 * nota2 + 3 * nota3 + 3 * nota4) / 10
reprovado_por_faltas = faltas > 20

print("A média do aluno é", media)

print("A primeira nota digitada é válida?", 0 <= nota1 <= 10)
print("A segunda nota digitada é válida?", 0 <= nota2 <= 10)
print("A terceira nota digitada é válida?", 0 <= nota3 <= 10)
print("A quarta nota digitada é válida?", 0 <= nota4 <= 10)
print("O número de faltas digitado é válido?", 0 <= faltas <= 60)
print("O aluno está reprovado por faltas?", reprovado_por_faltas)
print("O aluno está reprovado por média?", media < 3)
print("O aluno está em recuperação?", 3 <= media < 7 and not reprovado_por_faltas)
print("O aluno está aprovado?", 7 <= media <= 10 and not reprovado_por_faltas)
