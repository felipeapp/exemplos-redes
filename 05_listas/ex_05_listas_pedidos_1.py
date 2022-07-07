# [nome_produto, preco_unitario, quantidade_comprada]
compras = [["coxinha", 3.0, 10], ["pizza", 50.0, 2], ["coca-cola", 10, 3]]

# Quanto vai pagar em coxinhas
print(compras[0][1] * compras[0][2])

# Quanto vai pagar no total
total = 0

for item in compras:
    valor = item[1] * item[2]
    total += valor
    print(f"{item[0]} = {valor}")

print(f"Total: {total}")
