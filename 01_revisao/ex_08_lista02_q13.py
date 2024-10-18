preco = float(input("Digite o preço do produto (Maior que zero): "))
categoria = input("Digite a categoria do produto (Limpeza, Alimentação ou Vestuário): ").lower()
situcao = input("Digite a situação do produto (R ou S): ").lower()

if preco <= 25:
    if categoria == "limpeza":
        aumento = 0.05
    elif categoria == "alimentação":
        aumento = 0.08
    elif categoria == "vestuário":
        aumento = 0.1
    else:
        aumento = 0
else:
    if categoria == "limpeza":
        aumento = 0.12
    elif categoria == "alimentação":
        aumento = 0.15
    elif categoria == "vestuário":
        aumento = 0.18
    else:
        aumento = 0

print(f"O valor do aumento será de {aumento * 100}%")

imposta_extra = 0.05 if categoria == "alimentação" or situcao == "r" else 0.08
print(f"O valor da imposta extra será de {imposta_extra * 100}%")

# novo = preco + (preco * aumento) + (preco * imposta_extra)
novo = preco * (1 + aumento + imposta_extra)
print(f"O valor do novo preço será de R$ {novo:.2f}")

if novo <= 50:
    print("Barato")
elif novo >= 120:
    print("Caro")
else:
    print("Normal")
