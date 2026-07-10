def imprimir(valor: int) -> None:
    if valor < 10:
        print(valor)
        imprimir(valor + 1)


imprimir(0)

# Equivalente a recursão acima
for i in range(10):
    print(i)
