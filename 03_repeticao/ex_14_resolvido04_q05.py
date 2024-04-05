n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# if n1 < n2:
#     menor = n1
# else:
#     menor = n2
menor = n1 if n1 < n2 else n2
mdc = 1

for i in range(menor, 1, -1):
    if n1 % i == 0 and n2 % i == 0:
        mdc = i
        break

print(f"O MDC entre {n1} e {n2} é {mdc}!")
