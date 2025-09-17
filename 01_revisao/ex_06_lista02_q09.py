preco = float(input("Digite o preço do produto: "))

if preco <= 50:
    novo_preco = preco * 1.05
elif preco <= 100:
    novo_preco = preco * 1.10
else:
    novo_preco = preco * 1.15

print(f"O novo preço do produto é: R$ {novo_preco:.2f}")

if novo_preco <= 80:
    print("Barato")
elif novo_preco <= 120:
    print("Normal")
elif novo_preco <= 200:
    print("Caro")
else:
    print("Muito caro")
