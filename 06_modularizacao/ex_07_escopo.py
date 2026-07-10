a = 10


def funcao1() -> None:
    a = 20
    print("Função 1:", a)


def funcao2() -> None:
    print("Função 2:", a)


def funcao3() -> None:
    global a  # noqa: PLW0603
    print("Função 3.1:", a)
    a = 20
    print("Função 3.2:", a)


funcao1()
print("Depois da função 1:", a)

funcao2()
print("Depois da função 2:", a)

funcao3()
print("Depois da função 3:", a)
