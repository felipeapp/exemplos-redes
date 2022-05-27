distancia = float(input("Digite a distância da viagem: "))

# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45

# if-else de uma linha equivalente ao código acima
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f"O preço da viagem será R$ {preco:.2f}!")
