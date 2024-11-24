import threading


def imprimir1():
    for i in range(5):
        print(f"Execução {i} da função imprimir 1.")


def imprimir2():
    for i in range(5):
        print(f"Execução {i} da função imprimir 2.")


threading.Thread(target=imprimir1).start()
threading.Thread(target=imprimir2).start()

print("Final do script!")
