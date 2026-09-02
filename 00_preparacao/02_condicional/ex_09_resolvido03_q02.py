velocidade = float(input("Digite a velocidade do veículo: "))

if velocidade > 80:
    # multa = 5 * velocidade - 250
    multa = 150 + 5 * (velocidade - 80)
    print(f"Você foi multado, valor da multa: R$ {multa:.2f}")
else:
    print("Não há multa para esta velocidade!")
