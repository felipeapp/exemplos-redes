"""
LISTA 2 | Estudo dirigido: Relacionamentos entre objetos.

Nome: __________________________________________________________

Este e o arquivo onde voce trabalha. Siga o roteiro do documento da
Lista 4, etapa por etapa. Ao terminar cada etapa:

    1. abra o arquivo conferir.py e mude a linha ETAPA;
    2. rode conferir.py
    3. so siga em frente quando todos os testes derem OK.

CENARIO
    Uma companhia aerea. Passageiros fazem reservas; cada reserva pode
    ter um assento; cada voo nasce com os seus assentos e recebe uma
    tripulacao que tambem trabalha em outros voos.
"""


# ======================================================================
# Passageiro
# ======================================================================
class Passageiro:
    def __init__(self, nome: str, documento: str) -> None:
        # ETAPA 1: guarde nome (sem espacos sobrando) e documento
        # ETAPA 2: comece com uma lista vazia de reservas
        ...

    def identificacao(self) -> str:
        # ETAPA 1: devolva algo como "Ana Souza (111)"
        ...

    # ETAPA 5: escreva __eq__ (passageiros iguais = mesmo documento)


# ======================================================================
# Assento
# ======================================================================
class Assento:
    def __init__(self, codigo: str) -> None:
        # ETAPA 2: guarde o codigo; o assento comeca sem passageiro
        ...

    def esta_livre(self) -> bool:
        # ETAPA 2
        ...

    def ocupar(self, passageiro: Passageiro) -> bool:
        # ETAPA 2: recuse (avise e devolva False) se ja estiver ocupado;
        #          caso contrario, guarde o passageiro e devolva True
        ...

    def liberar(self) -> None:
        # ETAPA 2
        ...


# ======================================================================
# Reserva
# ======================================================================
class Reserva:
    def __init__(self, codigo: str, passageiro: Passageiro) -> None:
        # ETAPA 1: guarde o codigo e o OBJETO passageiro
        # ETAPA 2: comece sem assento, e avise o passageiro desta reserva
        ...

    def cartao(self) -> str:
        # ETAPA 1: devolva "R1 | Ana Souza (111)"
        # ETAPA 2: acrescente o assento: "R1 | Ana Souza (111) | 1A"
        #          ou "R1 | Ana Souza (111) | sem assento"
        ...

    # ETAPA 2: escreva marcar_assento(assento)


# ======================================================================
# Tripulante
# ======================================================================
class Tripulante:
    def __init__(self, nome: str, funcao: str) -> None:
        # ETAPA 3
        ...


# ======================================================================
# Voo
# ======================================================================
class Voo:
    def __init__(self, numero: str, origem: str, destino: str) -> None:
        # ETAPA 3: guarde os dados e comece com a tripulacao vazia
        # ETAPA 4: acrescente os parametros fileiras=5 e letras="ABCD"
        #          e crie aqui dentro todos os assentos do voo
        # ETAPA 5: comece tambem com uma lista vazia de reservas
        ...

    def escalar(self, tripulante: Tripulante) -> None:
        # ETAPA 3: inclua o tripulante, sem repetir
        # ETAPA 5: troque para escalar(self, *tripulantes)
        ...

    def dispensar(self, tripulante: Tripulante) -> None:
        # ETAPA 3
        ...

    # ETAPA 4: escreva buscar_assento(codigo) e assentos_livres()
    # ETAPA 5: escreva primeiro_livre(), reservar(...) e __len__
    # ETAPA 6: escreva mapa() e resumo()


# ======================================================================
# ETAPA 6: o programa final
# ======================================================================
if __name__ == "__main__":
    pass  # monte aqui o voo descrito na etapa 6
