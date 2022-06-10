consumo = float(input("Digite a quantidade de kWh consumidos: "))

if consumo > 0:
    tipo = input("Digite o tipo da instalação (R, I ou C): ").upper()

    if tipo in ("R", "C", "I"):
        if tipo == "R":
            preco = 0.40 if consumo <= 500 else 0.65
        elif tipo == "C":
            preco = 0.55 if consumo <= 1000 else 0.60
        else:
            preco = 0.55 if consumo <= 5000 else 0.60

        print(f"O valor a ser pago é R$ {preco * consumo:.2f}!")
    else:
        print("O tipo digitado é inválido!")
else:
    print("O consumo digitado é inválido!")
