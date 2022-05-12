diurno = int(input("Quantas horas de trabalho diurno: "))
noturno = int(input("Quantas horas de trabalho noturno: "))
fim = int(input("Quantas horas de trabalho no fim de semana: "))

salario = diurno * 50 + noturno * 75 + fim * 100

print(f"O salário da semana será de R$ {salario:.2f}")
