casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = int(input("Digite a quantidade de anos: "))

meses = anos * 12
prestacao = casa / meses
limite = 0.3 * salario

print(f"O limite de 30% do salário é R$ {limite:.2f}!")

if prestacao <= limite:
    print(f"Empréstimo aprovado para R$ {prestacao:.2f} em {meses} meses!")
else:
    print(f"Empréstimo negado para R$ {prestacao:.2f} em {meses} meses!")
