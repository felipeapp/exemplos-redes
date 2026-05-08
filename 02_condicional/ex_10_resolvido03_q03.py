distancia = float(input("Digite a distância da viagem (km): "))

# if distancia <= 200:
#     preco_km = 0.50
# else:
#     preco_km = 0.45

preco_km = 0.50 if distancia <= 200 else 0.45

preco_viagem = distancia * preco_km
print(f"O preço da viagem será: R$ {preco_viagem:.2f}")
