horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

# A
horas_em_minutos = horas * 60
print(f"A quantidade de horas em minutos é {horas_em_minutos}")

# B
total_minutos = horas_em_minutos + minutos
print(f"O total de minutos é {total_minutos}")

# C
total_segundos = total_minutos * 60
print(f"O total de segundos é {total_segundos}")
