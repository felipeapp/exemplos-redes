from threading import Thread


def imprimir1() -> None:
    for i in range(5):
        print(f"Execução {i} da função imprimir 1.")


def imprimir2() -> None:
    for i in range(5):
        print(f"Execução {i} da função imprimir 2.")


Thread(target=imprimir1).start()
Thread(target=imprimir2).start()

print("Final do script!")
