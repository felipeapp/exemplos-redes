import threading
from random import randint
from time import sleep

lista = list(range(10))
lock = threading.Lock()


def imprimir1() -> None:
    sleep(randint(0, 1))
    with lock:
        for elem in lista:
            print("Imprimir 1.1:", elem)

    sleep(randint(0, 1))
    with lock:
        for elem in lista:
            print("Imprimir 1.2:", elem)


def imprimir2() -> None:
    sleep(randint(0, 1))
    with lock:
        for elem in lista:
            print("Imprimir 2.1:", elem)

    sleep(randint(0, 1))
    with lock:
        for elem in lista:
            print("Imprimir 2.2:", elem)


t1 = threading.Thread(target=imprimir1)
t2 = threading.Thread(target=imprimir2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final do script!")
