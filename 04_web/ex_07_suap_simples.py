from getpass import getpass
from http import HTTPStatus

import requests

username = input("Digite seu nome de usuário: ")
password = getpass("Digite sua senha: ", echo_char="*")

with requests.post(
    "https://suap.ifrn.edu.br/api/token/pair",
    json={"username": username, "password": password},
    timeout=10,
) as resposta:
    if resposta.status_code == HTTPStatus.OK:
        dados = resposta.json()
        token_acesso = dados["access"]

        with requests.get(
            "https://suap.ifrn.edu.br/api/rh/eu",
            timeout=10,
            headers={"Authorization": f"Bearer {token_acesso}"},
        ) as resposta_rh:
            if resposta_rh.status_code == HTTPStatus.OK:
                dados_rh = resposta_rh.json()
                print("Nome:", dados_rh["nome"])
                print("E-mail:", dados_rh["email"])
                print("Campus:", dados_rh["campus"])
                print("Tipo de Usuário:", dados_rh["tipo_usuario"])
            else:
                print(f"Erro ao consultar dados do usuário: {resposta_rh.status_code}!")
    else:
        print(f"Erro ao realizar autenticação: {resposta.status_code}!")
