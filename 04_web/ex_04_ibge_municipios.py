from http import HTTPStatus

import requests

codigo = int(input("Digite o código do estado: "))
nome = input("Digite o nome do município: ").casefold()

with requests.get(
    f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{codigo}/municipios", timeout=None
) as resposta:
    if resposta.status_code == HTTPStatus.OK:
        municipios = resposta.json()

        if municipios:
            for m in municipios:
                if m["nome"].casefold() == nome:
                    print(30 * "-")
                    print("Nome:", m["nome"])
                    print("Microrregião:", m["microrregiao"]["nome"])
                    print("Mesorregião:", m["microrregiao"]["mesorregiao"]["nome"])
                    break
        else:
            print("Código do estado não encontrado!")
    else:
        print(f"Erro ao enviar a requisição: {resposta.status_code}!")
