nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A média das notas é: {media:.2f}")

if 7 <= media <= 10:
    print("Aprovado")
elif 4 <= media < 7:
    print("Recuperação")
elif 0 <= media < 4:
    print("Reprovado")
else:
    print("Média inválida")
