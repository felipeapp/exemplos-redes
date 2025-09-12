while True:
    linhas = int(input("Digite a quantidade de linhas do padrão: "))

    if linhas <= 0:
        print("O número de linhas deve ser positivo!")
    elif linhas % 2 == 0:
        print("O número de linhas deve ser ímpar!")
    else:
        break

for i in range(linhas // 2 + 1):
    for _ in range(i + 1):
        print(" * ", end="")
    print()

for i in range(linhas // 2, 0, -1):
    for _ in range(i):
        print(" * ", end="")
    print()
