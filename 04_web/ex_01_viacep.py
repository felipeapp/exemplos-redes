from http import HTTPStatus

import requests

cep = input("Digite o CEP a ser consultado: ")

with requests.get(f"https://viacep.com.br/ws/{cep}/json", timeout=10) as resposta:
    if resposta.status_code == HTTPStatus.OK:
        dados = resposta.json()

        if "erro" in dados:
            print("O CEP informado não foi encontrado!")
        else:
            print("Rua:", dados["logradouro"])
            print("Bairro:", dados["bairro"])
            print("Cidade:", dados["localidade"])
            print("Estado:", dados["uf"])
            print("DDD:", dados["ddd"])
    elif resposta.status_code == HTTPStatus.NOT_FOUND:
        print("O CEP informado é inválido!")
    else:
        print(f"Erro ao realizar a requisição: {resposta.status_code}!")
