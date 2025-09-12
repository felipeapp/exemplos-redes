# Criação de algumas variáveis
nome = "João Ninguém"
curso = "Redes de Computadores"
media = 8.5
faltas = 15

# Usando a função de saída de dados para mostrar as variáveis
print(nome)
print(curso)
print(media)
print(faltas)

print("--------------")

# Mostrando variáveis junto com texto
print("O nome do aluno é", nome)
print("O nome do curso é", curso)
print("A média é", media)
print("O número de faltas é", faltas)

print("--------------")

# Exemplo de print com várias variáveis
print(nome, "cursa", curso, "e tem média", media, "com", faltas, "faltas!")

print("--------------")

# Exemplos mudando o caractere de terminção da função print
print(nome, end="")
print(curso, end="\n")
print(media, end="-")
print(faltas)

# Equivalente a linha 16
print("O nome do aluno é ", end="")
print(nome)

print("--------------")

# Exemplo usando quebras de linha
print("Este é um exemplo\nsobre saída de dados\nusando a função print!")
