try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    print(f"A divisão é {numero1 / numero2}")
except ZeroDivisionError:
    print("Divisão por zero não é possível!")
except KeyboardInterrupt:
    print("\nA execução foi cancelada pelo usuário!")
except ValueError:
    print("O valor deve ser um inteiro!")
