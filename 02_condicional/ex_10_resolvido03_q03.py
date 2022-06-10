distancia = float(input("Digite a distância da viagem (km): "))

# if distancia <= 200:
#     valor = 0.50 * distancia
# else:
#     valor = 0.45 * distancia

valor = 0.50 * distancia if distancia <= 200 else 0.45 * distancia

print(f"O valor da viagem será R$ {valor:.2f}!")
