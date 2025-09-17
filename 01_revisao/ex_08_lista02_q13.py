preco = float(input("Digite o preço: "))
categoria = input("Digite a categoria (Limpeza, Alimentação ou Vestuário): ").lower()
situacao = input("Digite a situação (R ou S): ").lower()

# A
if preco <= 25:
    if categoria == "limpeza":
        valor_aumento = preco * 0.05
    elif categoria == "alimentação":
        valor_aumento = preco * 0.08
    elif categoria == "vestuário":
        valor_aumento = preco * 0.10
    else:
        valor_aumento = 0
else:  # noqa: PLR5501
    if categoria == "limpeza":
        valor_aumento = preco * 0.12
    elif categoria == "alimentação":
        valor_aumento = preco * 0.15
    elif categoria == "vestuário":
        valor_aumento = preco * 0.18
    else:
        valor_aumento = 0

print(f"Valor do aumento: R$ {valor_aumento:.2f}")

# B
valor_imposto = preco * 0.05 if categoria == "alimentação" or situacao == "r" else preco * 0.08
print(f"Valor do imposto: R$ {valor_imposto:.2f}")

# C
novo_preco = preco + valor_aumento + valor_imposto
print(f"Novo preço: R$ {novo_preco:.2f}")

if novo_preco <= 50:
    print("Barato")
elif novo_preco >= 120:
    print("Caro")
else:
    print("Normal")
