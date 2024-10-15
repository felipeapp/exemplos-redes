curso = "Redes de Computadores"

# Coloca a primeira letra em maiúsculo e o resto em minúsculo
print(curso.capitalize())

# Permite alinhar a string dentro de um conjunto de caracteres
print(curso.center(30, "*"))
print(curso.ljust(30, "*"))
print(curso.rjust(30, "*"))

# Retorna o número de ocorrências da string
print(curso.count("e"))
print(curso.count("R"))
print(curso.count("r"))
print(curso.count("de"))
print(curso.count("x"))

# Verifica se a string contem ou não o elemento
print("de" in curso)
print("x" not in curso)

# Verifica se a string começa ou termina com algum valor
print(curso.startswith("redes"))
print(curso.startswith("Redes"))
print(curso.endswith("s"))
print(curso.endswith("dores"))

# Retorna o índice do elemento ou -1 caso não exista
print(curso.find("o"))
print(curso.rfind("o"))
print(curso.find("de"))
print(curso.rfind("de"))
print(curso.find("x"))
print(curso.find("e", 5, 8))

# Retorna o índice do elemento ou erro caso não exista
print(curso.index("o"))
print(curso.rindex("o"))
# print(curso.index("x"))

# Verifica se é maiúsculo
print("A".islower())
print("a".islower())

# Verifica se é minúsculo
print("A".isupper())
print("a".isupper())

# Retorna uma cópia da string com todos os caracteres minúsculos
print(curso.lower())

# Retorna uma cópia da string com todos os caracteres maiúsculo
print(curso.upper())

# Inverte o caso da string
print(curso.swapcase())

# Retorna uma cópia da string com caracteres iniciais e finais removidos
print("   Redes   ".strip())
print("***Redes***".strip("*"))
print("***Redes***".strip("s"))
print("***Redes***".lstrip("*"))
print("***Redes***".rstrip("*"))
print("Nome: Felipe".lstrip("Nome: "))

# Substitui uma substring por outra
print(curso.replace("e", "3"))
print(curso.replace("e", "3", 2))
print(curso.replace(" ", ""))
print(curso.replace("de", "*"))
print(curso.replace("de Computadores", "é muito legal!"))

# Divide a string em partes usando um separador
print(curso.split(" "))

# Retorno o tamanho (quantidade de elementos)
print(len(curso))

# É possível concaternar strings usando o operador +
print("O curso " + curso + " é muito legal!")

# É possível gerar uma string usando o operador *
print(30 * "-")
print(10 * "Redes")
print(10 * "*-*")
