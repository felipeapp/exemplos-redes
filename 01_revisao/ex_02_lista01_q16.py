import math

a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

h = math.sqrt(a**2 + b**2)
# h = math.hypot(a, b)
print(f"O valor da hipotenusa é: {h:.2f}")
