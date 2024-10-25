minimo = int(input("Digite o limite inferior: "))
maximo = int(input("Digite o limite superior: "))

for tab in range(1, 10):
    print(25 * "-")
    for i in range(minimo, maximo + 1):
        print(f"{tab} + {i} = {tab + i} | {tab} x {i} = {tab * i}")
