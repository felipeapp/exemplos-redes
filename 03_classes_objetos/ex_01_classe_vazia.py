class Servidor:
    pass


srv = Servidor()
print("tipo do objeto:", type(srv))
print("sao objetos diferentes:", Servidor() is not Servidor())
