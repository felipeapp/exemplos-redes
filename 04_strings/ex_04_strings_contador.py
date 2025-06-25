texto = input("Digite um texto qualquer: ")
minusculos = maiusculos = outros = 0

for c in texto:
    if c.islower():
        minusculos += 1
    elif c.isupper():
        maiusculos += 1
    else:
        outros += 1

print(f"Quantidade de Minúsculos: {minusculos}")
print(f"Quantidade de Maiúsculos: {maiusculos}")
print(f"Quantidade de Outros: {outros}")
