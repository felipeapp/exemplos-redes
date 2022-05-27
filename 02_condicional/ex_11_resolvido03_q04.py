valor_casa = float(input("Digite o valor da casa: "))
valor_salario = float(input("Digite o valor do salário: "))
quantidade_anos = int(input("Digite a quantidade de anos para pagar: "))

quantidade_meses = quantidade_anos * 12
valor_parcela = valor_casa / quantidade_meses

print(f"A parcela para {quantidade_meses} meses será R$ {valor_parcela:.2f}!")

if valor_parcela <= valor_salario * 0.3:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
