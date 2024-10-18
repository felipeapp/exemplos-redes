import math

raio = float(input("Digite o valor do raio: "))

# O comprimento da circunferência
comprimento = 2 * math.pi * raio
print("O comprimento da circunferência é", comprimento)

# A área da circunferência
area = math.pi * raio**2
# area = math.pi * raio * raio
print("A área da circunferência é", area)

# O volume de uma esfera com mesmo raio
volume = (4 * math.pi * raio**3) / 3
print("O volume de uma esfera com mesmo raio é", volume)
