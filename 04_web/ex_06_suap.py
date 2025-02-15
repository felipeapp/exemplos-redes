from getpass import getpass
from http import HTTPStatus

import requests


def criar_sessao_suap(matricula: str, senha: str) -> requests.Session | None:
    s = requests.Session()

    with s.post(
        "https://suap.ifrn.edu.br/api/v2/autenticacao/token/", json={"username": matricula, "password": senha}
    ) as response:
        if response.status_code == HTTPStatus.OK:
            s.headers["Authorization"] = f"Bearer {response.json()['access']}"
        else:
            return None

    return s


def main():
    print(50 * "-")
    matricula = input("Digite sua matrícula: ")
    senha = getpass("Digite sua senha: ")

    sessao = criar_sessao_suap(matricula, senha)

    if sessao is None:
        print("Erro de autenticação!")
    else:
        print("Autenticado com sucesso!")
        print(50 * "-")

        with sessao.get("https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/") as resposta:
            if resposta.status_code == 200:
                json_data = resposta.json()

                print("Matrícula:", json_data["matricula"])
                print("Nome:", json_data["nome_usual"])
                print("E-Mail:", json_data["email"])
                print("Campus:", json_data["vinculo"]["campus"])
                print("Categoria:", json_data["vinculo"]["categoria"])
            else:
                print("Erro ao realizar requisição:", resposta.status_code)

    print(50 * "-")


if __name__ == "__main__":
    main()
