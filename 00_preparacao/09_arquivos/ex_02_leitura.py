arquivo = open("contatos.txt", "r", encoding="utf-8")  # noqa: SIM115, UP015

# Leitura de todo o arquivo para uma string
texto = arquivo.read()
print(texto)

arquivo.close()

print(30 * "-")

arquivo = open("contatos.txt", "r", encoding="utf-8")  # noqa: SIM115, UP015

# Leitura de todo o arquivo para uma lista de strings, cada linhe se torna um elemento
linhas = arquivo.readlines()
print("Número de linhas:", len(linhas))
print(linhas)

arquivo.close()

print(30 * "-")

arquivo = open("contatos.txt", "r", encoding="utf-8")  # noqa: SIM115, UP015

# Leitura linha a linha manualmente
linha = arquivo.readline()
print("Linha 1:", linha)

linha = arquivo.readline()
print("Linha 2:", linha)

linha = arquivo.readline()
print("Linha 3:", linha)

arquivo.close()

print(30 * "-")

arquivo = open("contatos.txt", "r", encoding="utf-8")  # noqa: SIM115, UP015

# Leitura linha a linha até o final do arquivo
for linha in arquivo:
    linha_limpa = linha.strip()  # o strip remove a quebra de linha adicional
    print(linha_limpa)

arquivo.close()
