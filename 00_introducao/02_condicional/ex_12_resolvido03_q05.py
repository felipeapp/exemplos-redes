mes = input("Digite o nome de um mês do ano: ").lower()

if mes == "fevereiro":
    print(f"O mês de {mes} tem 28 ou 29 dias!")
elif mes in ("abril", "junho", "setembro", "novembro"):
    print(f"O mês de {mes} tem 30 dias!")
elif mes in ("janeiro", "março", "maio", "julho", "agosto", "outubro", "dezembro"):
    print(f"O mês de {mes} tem 31 dias!")
else:
    print(f"O valor {mes} é inválido!")
