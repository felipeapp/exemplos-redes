from threading import Thread


def imprimir1() -> None:
    for i in range(5):
        print(f"Execução {i} da função imprimir 1.")


def imprimir2(nome: str, repeticoes: int) -> None:
    for i in range(repeticoes):
        print(f"Execução {i} da função {nome}.")


t1 = Thread(target=imprimir1)
t2 = Thread(target=imprimir2, args=("com parâmetros", 10))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final do script!")
