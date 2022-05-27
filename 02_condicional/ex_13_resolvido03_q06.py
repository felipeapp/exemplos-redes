kwh = float(input("Digite a quantidade de kWh consumidos: "))
tipo = input("Digite o tipo da instalação (R, C ou I): ").upper()

# if tipo == "R" or tipo == "C" or tipo == "I":
if tipo in ("R", "C", "I"):
    if tipo == "R":
        preco = kwh * 0.40 if kwh <= 500 else kwh * 0.65
    elif tipo == "C":
        preco = kwh * 0.55 if kwh <= 1000 else kwh * 0.60
    else:
        preco = kwh * 0.55 if kwh <= 5000 else kwh * 0.60

    print(f"O preço a pagar é R$ {preco:.2f}!")
else:
    print("O tipo digitado é inválido!")
