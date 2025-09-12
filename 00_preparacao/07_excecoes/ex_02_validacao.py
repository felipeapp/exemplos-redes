try:
    while True:
        try:
            nota = int(input("Digite a nota (0 - 100): "))
            if 0 <= nota <= 100:
                break
            print("A nota deve estar entre 0 e 100, tente novamente!")
        except ValueError:
            print("O valor deve ser um inteiro, tente novamente!")
except KeyboardInterrupt:
    print("\nExecução cancelada pelo usuário!")

print("Fim do programa...")
