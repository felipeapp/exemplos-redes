mes = input("Digite o nome do mês: ").lower()

if mes == "abril" or mes == "junho" or mes == "setembro" or mes == "novembro":
    print(f"O mês {mes} tem 30 dias!")
elif mes == "fevereiro":
    print("O mês fevereito tem 28 ou 29 dias!")
elif (
    mes == "janeiro"
    or mes == "março"
    or mes == "maio"
    or mes == "julho"
    or mes == "agosto"
    or mes == "outubro"
    or mes == "dezembro"
):
    print(f"O mês {mes} tem 31 dias")
else:
    print(f"O valor {mes} não é um mês válido!")
