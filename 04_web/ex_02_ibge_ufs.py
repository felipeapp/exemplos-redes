from http import HTTPStatus

import requests

with requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados", timeout=10) as resposta:
    if resposta.status_code == HTTPStatus.OK:
        for estado in resposta.json():
            print(30 * "-")
            print("ID:", estado["id"])
            print("Sigla:", estado["sigla"])
            print("Nome:", estado["nome"])
            print("Região:", estado["regiao"]["nome"])
    else:
        print(f"A requisição retornou um erro: {resposta.status_code}!")
