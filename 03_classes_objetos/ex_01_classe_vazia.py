class Servidor:
    pass


srv = Servidor()
print(f"tipo do objeto: {type(srv)}")
print(f"sao objetos diferentes: {Servidor() is not Servidor()}")
