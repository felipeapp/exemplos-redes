codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    procedencia = "Sul"
elif codigo == 2:
    procedencia = "Norte"
elif codigo == 3:
    procedencia = "Leste"
elif codigo == 4:
    procedencia = "Oeste"
elif codigo in (5, 6) or 21 <= codigo <= 30:
    procedencia = "Nordeste"
elif 7 <= codigo <= 9:
    procedencia = "Sudeste"
elif 10 <= codigo <= 20:
    procedencia = "Centro-Oeste"
else:
    procedencia = "Desconhecida"

print(f"A procedência do produto de código {codigo} é {procedencia}")
