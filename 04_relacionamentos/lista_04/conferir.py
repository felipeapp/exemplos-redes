"""
LISTA 4 | Estudo dirigido: Relacionamentos entre objetos.

Conferencia automatica

Como usar:
    1. Termine uma etapa no arquivo lista_04.py.
    2. Mude a linha ETAPA abaixo para o numero da etapa que voce terminou.
    3. Rode conferir.py

O programa testa todas as etapas ate a escolhida. Mensagens de aviso
no meio da saida (como "assento 2C ja esta ocupado") sao esperadas:
alguns testes provocam situacoes erradas de proposito.
"""

import lista_04 as l4

ETAPA = 1  # <-- mude aqui: 1, 2, 3, 4, 5 ou 6

placar = [0, 0]  # [certos, errados]


def confere(descricao: str, obtido: object, esperado: object) -> None:
    if obtido == esperado:
        placar[0] += 1
        print(f"   OK      {descricao}")
    else:
        placar[1] += 1
        print(f"   FALHOU  {descricao}")
        print(f"           esperado: {esperado!r}")
        print(f"           obtido  : {obtido!r}")


def titulo(texto: str) -> None:
    print()
    print("=" * 66)
    print(texto)
    print("=" * 66)


# ------------------------------------------------------------------ 1 ---
def etapa_1() -> None:
    titulo("ETAPA 1 - Associacao: a reserva conhece o passageiro")
    ana = l4.Passageiro("  Ana Souza ", "111")
    confere("nome do passageiro sem espacos sobrando", ana.nome, "Ana Souza")
    confere("identificacao()", ana.identificacao(), "Ana Souza (111)")

    r1 = l4.Reserva("R1", ana)
    confere("a reserva guarda o OBJETO passageiro", r1.passageiro is ana, True)
    confere(
        "cartao() comeca com codigo e identificacao",
        r1.cartao().startswith("R1 | Ana Souza (111)"),
        True,
    )

    r2 = l4.Reserva("R2", ana)
    confere("duas reservas apontam para o mesmo passageiro", r1.passageiro is r2.passageiro, True)

    ana.nome = "Ana Souza Lima"
    confere(
        "mudou o nome: a reserva ja enxerga a mudanca",
        r2.cartao().startswith("R2 | Ana Souza Lima (111)"),
        True,
    )


# ------------------------------------------------------------------ 2 ---
def etapa_2() -> None:
    titulo("ETAPA 2 - Associacao opcional e bidirecional")
    ana = l4.Passageiro("Ana Souza", "111")
    bia = l4.Passageiro("Bia Lima", "222")

    a1 = l4.Assento("1A")
    confere("assento novo comeca sem passageiro", a1.passageiro is None, True)
    confere("assento novo esta livre", a1.esta_livre(), True)

    r = l4.Reserva("R1", ana)
    confere("reserva nova comeca sem assento", r.assento is None, True)
    confere("cartao() de reserva sem assento", r.cartao(), "R1 | Ana Souza (111) | sem assento")

    confere("marcar_assento em assento livre devolve True", r.marcar_assento(a1), True)
    confere("o assento agora conhece a passageira", a1.passageiro is ana, True)
    confere("o assento deixou de estar livre", a1.esta_livre(), False)
    confere("cartao() mostra o assento", r.cartao(), "R1 | Ana Souza (111) | 1A")

    rb = l4.Reserva("R2", bia)
    confere("marcar assento ocupado devolve False", rb.marcar_assento(a1), False)
    confere("o assento continua com a primeira passageira", a1.passageiro is ana, True)
    confere("a segunda reserva continua sem assento", rb.assento is None, True)

    a1.liberar()
    confere("liberar() deixa o assento livre de novo", a1.esta_livre(), True)

    davi = l4.Passageiro("Davi Rocha", "333")
    x1 = l4.Reserva("X1", davi)
    x2 = l4.Reserva("X2", davi)
    confere("o passageiro conhece as proprias reservas", len(davi.reservas), 2)
    confere(
        "as reservas ficam na ordem em que foram criadas",
        davi.reservas[0] is x1 and davi.reservas[1] is x2,
        True,
    )


# ------------------------------------------------------------------ 3 ---
def etapa_3() -> None:
    titulo("ETAPA 3 - Agregacao: o voo reune tripulantes")
    marta = l4.Tripulante("Marta", "piloto")
    caio = l4.Tripulante("Caio", "comissario")
    confere("tripulante guarda a funcao", marta.funcao, "piloto")

    v1 = l4.Voo("AZ101", "NAT", "REC")
    v2 = l4.Voo("AZ202", "REC", "NAT")
    confere("voo novo comeca sem tripulacao", len(v1.tripulacao), 0)

    v1.escalar(marta)
    v1.escalar(caio)
    v2.escalar(marta)
    confere("o voo 1 tem dois tripulantes", len(v1.tripulacao), 2)
    confere("a mesma piloto esta nos dois voos", marta in v1.tripulacao and marta in v2.tripulacao, True)

    v1.escalar(marta)
    confere("escalar de novo nao duplica", len(v1.tripulacao), 2)

    v1.dispensar(marta)
    confere("dispensada do voo 1", marta in v1.tripulacao, False)
    confere("continua no voo 2", marta in v2.tripulacao, True)
    confere("e continua existindo", marta.nome, "Marta")


# ------------------------------------------------------------------ 4 ---
def etapa_4() -> None:
    titulo("ETAPA 4 - Composicao: o voo cria os proprios assentos")
    v = l4.Voo("AZ303", "NAT", "GRU", fileiras=3)
    confere("3 fileiras de 4 letras: 12 assentos", len(v.assentos), 12)
    confere("primeiro assento", v.assentos[0].codigo, "1A")
    confere("ultimo assento", v.assentos[-1].codigo, "3D")

    padrao = l4.Voo("AZ000", "NAT", "REC")
    confere("sem informar nada: 5 fileiras, 20 assentos", len(padrao.assentos), 20)

    pequeno = l4.Voo("AZ001", "NAT", "MOS", fileiras=2, letras="AB")
    confere("letras escolhidas pelo voo", [a.codigo for a in pequeno.assentos], ["1A", "1B", "2A", "2B"])

    confere("buscar_assento encontra pelo codigo", v.buscar_assento("2B").codigo, "2B")
    confere("buscar_assento devolve None se nao existir", v.buscar_assento("9Z") is None, True)

    confere("todos livres no inicio", v.assentos_livres(), 12)
    v.buscar_assento("1C").ocupar(l4.Passageiro("Ana", "111"))
    confere("um ocupado: 11 livres", v.assentos_livres(), 11)

    outro = l4.Voo("AZ304", "NAT", "GRU", fileiras=3)
    confere("cada voo tem os SEUS assentos", v.buscar_assento("1A") is outro.buscar_assento("1A"), False)
    confere("ocupar no voo 1 nao afeta o voo 2", outro.buscar_assento("1C").esta_livre(), True)


# ------------------------------------------------------------------ 5 ---
def etapa_5() -> None:
    titulo("ETAPA 5 - Sobrecarga: um reservar(), varios jeitos de chamar")
    confere(
        "passageiros com o mesmo documento sao iguais",
        l4.Passageiro("Ana", "111") == l4.Passageiro("Ana S.", "111"),
        True,
    )
    confere(
        "documentos diferentes nao sao iguais",
        l4.Passageiro("Ana", "111") == l4.Passageiro("Ana", "999"),
        False,
    )

    v = l4.Voo("AZ404", "NAT", "REC", fileiras=2)
    ana = l4.Passageiro("Ana Souza", "111")
    bia = l4.Passageiro("Bia Lima", "222")
    davi = l4.Passageiro("Davi Rocha", "333")

    r1 = v.reservar(ana)
    confere("sem assento informado: pega o primeiro livre", r1.assento.codigo, "1A")
    confere("codigo da reserva gerado pelo voo", r1.codigo, "AZ404-1")

    r2 = v.reservar(bia, "2C")
    confere("com assento informado: pega aquele", r2.assento.codigo, "2C")
    confere("segunda reserva, segundo codigo", r2.codigo, "AZ404-2")

    confere("assento ocupado: devolve None", v.reservar(davi, "2C") is None, True)
    confere("assento inexistente: devolve None", v.reservar(davi, "9Z") is None, True)
    confere("mesmo documento de novo: devolve None", v.reservar(l4.Passageiro("Ana S.", "111")) is None, True)

    confere("len(voo) conta os assentos ocupados", len(v), 2)
    confere("a reserva aparece na lista da passageira", ana.reservas[-1] is r1, True)

    v.escalar(
        l4.Tripulante("Marta", "piloto"),
        l4.Tripulante("Caio", "comissario"),
        l4.Tripulante("Rita", "comissaria"),
    )
    confere("escalar varios tripulantes de uma vez", len(v.tripulacao), 3)
    v.escalar()
    confere("escalar sem ninguem nao muda nada", len(v.tripulacao), 3)

    lotado = l4.Voo("AZ999", "NAT", "FEN", fileiras=1, letras="AB")
    lotado.reservar(ana)
    lotado.reservar(bia)
    confere("voo lotado: devolve None", lotado.reservar(davi) is None, True)


# ------------------------------------------------------------------ 6 ---
def etapa_6() -> None:
    titulo("ETAPA 6 - Juntando tudo")
    v = l4.Voo("AZ505", "NAT", "REC", fileiras=2)
    ana = l4.Passageiro("Ana Souza", "111")
    bia = l4.Passageiro("Bia Lima", "222")
    v.reservar(ana, "1B")
    v.reservar(bia, "2D")

    confere("mapa() do voo", v.mapa(), " 1A .   1B X   1C .   1D .\n 2A .   2B .   2C .   2D X")
    confere("resumo() sem tripulacao", v.resumo(), "Voo AZ505 NAT->REC: 2 ocupados, 6 livres, 0 tripulantes")

    v.escalar(l4.Tripulante("Marta", "piloto"))
    confere("resumo() com tripulacao", v.resumo(), "Voo AZ505 NAT->REC: 2 ocupados, 6 livres, 1 tripulantes")

    volta = l4.Voo("AZ506", "REC", "NAT", fileiras=2)
    volta.reservar(ana)
    confere("a passageira tem reservas em dois voos", len(ana.reservas), 2)
    confere("cartao da reserva de volta", ana.reservas[1].cartao(), "AZ506-1 | Ana Souza (111) | 1A")


# --------------------------------------------------------------- roda ---
ETAPAS = [etapa_1, etapa_2, etapa_3, etapa_4, etapa_5, etapa_6]

if __name__ == "__main__":
    print(f"Conferindo ate a etapa {ETAPA}...")
    for numero in range(1, ETAPA + 1):
        ETAPAS[numero - 1]()

    print()
    print("-" * 66)
    total = placar[0] + placar[1]
    print(f"Resultado: {placar[0]} de {total} testes certos.")
    if placar[1] == 0 and ETAPA < 6:
        print(f"Etapa {ETAPA} concluida! Mude ETAPA para {ETAPA + 1} e siga em frente.")
    elif placar[1] == 0:
        print("Estudo dirigido concluido! Rode tambem o seu lista_04.py.")
    else:
        print("Corrija os testes que FALHARAM antes de seguir.")
        print("Leia o 'esperado' e o 'obtido': a diferenca diz o que falta.")
