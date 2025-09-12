horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

# Somente a variável da hora convertida em minutos
horas_em_minutos = horas * 60
print(f"A quantidade de horas em minutos é {horas_em_minutos}")

# O total dos minutos
total_minutos = horas_em_minutos + minutos
print(f"O total de minutos é {total_minutos}")

# O total dos minutos convertidos em segundos
total_segundos = total_minutos * 60
print(f"O total de segundos é {total_segundos}")
