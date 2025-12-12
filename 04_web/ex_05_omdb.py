from http import HTTPStatus

import requests

titulo = input("Digite parte do título do filme: ")

parametros = {"apikey": "", "s": titulo}

with requests.get("http://www.omdbapi.com", params=parametros, timeout=10) as resposta:
    if resposta.status_code == HTTPStatus.OK:
        dados = resposta.json()

        if dados["Response"] == "True":
            print(f"{dados['totalResults']} resultados encontrados, os 10 primeiros são:")

            for filme in dados["Search"]:
                print(f"- {filme['Title']} ({filme['Year']})")
        else:
            print("A busca não encontrou resultados!")
    else:
        print(f"Erro ao realizar requisição: {resposta.status_code}!")
