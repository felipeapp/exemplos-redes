"""
Entrada e saída de dados.

Este é um exemplo de script python mostrando
o uso da função input e print com variáveis
de diferentes tipos.
"""

# Este trecho do código fará a leitura dos dados
nome = input("Digite o nome do aluno: ")
curso = input("Digite o nome do curso do aluno: ")
media = float(input("Digite o valor da média do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

print("-----------------")

# Imprimindo várias variáveis no mesmo print
print(nome, "cursa", curso, "e tem média", media, "com", faltas, "faltas!")
