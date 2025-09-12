valor = int(input("Digite o valor do saque: "))

notas_100 = valor // 100
# valor = valor % 100
valor %= 100

notas_50 = valor // 50
valor %= 50

notas_20 = valor // 20
valor %= 20

notas_10 = valor // 10
valor %= 10

notas_5 = valor // 5
valor %= 5

print("Notas de 100:", notas_100)
print("Notas de 50:", notas_50)
print("Notas de 20:", notas_20)
print("Notas de 10:", notas_10)
print("Notas de 5:", notas_5)
print("Valor restante:", valor)
