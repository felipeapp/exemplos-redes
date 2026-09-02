cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0

for i in range(15):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    if idade <= 15:
        cont_1 += 1
    elif idade <= 30:
        cont_2 += 1
    elif idade <= 45:
        cont_3 += 1
    elif idade <= 60:
        cont_4 += 1
    else:
        cont_5 += 1

print(f"Quantidade de pessoas com até 15 anos: {cont_1}")
print(f"Quantidade de pessoas com 16 a 30 anos: {cont_2}")
print(f"Quantidade de pessoas com 31 a 45 anos: {cont_3}")
print(f"Quantidade de pessoas com 46 a 60 anos: {cont_4}")
print(f"Quantidade de pessoas com mais de 60 anos: {cont_5}")
