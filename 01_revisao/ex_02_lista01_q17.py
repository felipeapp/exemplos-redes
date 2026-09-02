import math

raio = float(input("Digite o raio da circunferência: "))

# O comprimento da circunferência
comprimento = 2 * math.pi * raio
print(f"Comprimento da circunferência: {comprimento:.2f}")

# A área da circunferência
area = math.pi * raio**2
# area = math.pi * raio * raio
print(f"Área da circunferência: {area:.2f}")

# O volume de uma esfera com mesmo raio
volume = (4 * math.pi * raio**3) / 3
print(f"Volume da esfera: {volume:.2f}")
