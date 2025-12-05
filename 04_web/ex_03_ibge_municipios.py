from http import HTTPStatus

import requests

codigo = int(input("Digite o código do estado: "))

with requests.get(
    f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{codigo}/municipios",
    timeout=10,
) as resposta:
    if resposta.status_code == HTTPStatus.OK:
        municipios = resposta.json()

        if municipios:
            for m in municipios:
                print(30 * "-")
                print("Nome:", m["nome"])
                print("Microrregião:", m["microrregiao"]["nome"])
                print("Mesorregião:", m["microrregiao"]["mesorregiao"]["nome"])
        else:
            print("Código do estado não encontrado!")
    else:
        print(f"Erro ao enviar a requisição: {resposta.status_code}!")
