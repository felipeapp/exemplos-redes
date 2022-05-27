velocidade = int(input("Digite a velocidade do veículo: "))

if velocidade > 80:
    multa = 150 + (velocidade - 80) * 5
    print(f"O valor da multa é R$ {multa}!")
else:
    print(f"{velocidade} km/h está dentro do limite de velocidade!")
