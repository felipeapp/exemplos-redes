# Criação de variáveis com tipos diferentes
x = 10
y = 3.14
curso = "Redes de Computadores"
facil_e_divertido = True
alguem_vai_reprovar = False

print(x)
print(y)
print(curso)
print("curso")  # Aqui será interpretado como texto
print(facil_e_divertido)
print(alguem_vai_reprovar)

print(type(x))
print(type(y))
print(type(curso))
print(type(facil_e_divertido))
print(type(alguem_vai_reprovar))

"""
A seguir mostramos como podemos usar a mesma variável
com valores de diferentes tipos, no caso inteiro,
real e texto. Por isso, Python é considerada uma
linguagem dinamicamente tipada.
"""
nota = 10
print(nota)
print(type(nota))

nota = 10.0
print(nota)
print(type(nota))

nota = "10"
print(nota)
print(type(nota))
