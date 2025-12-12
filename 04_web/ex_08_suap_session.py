from getpass import getpass
from http import HTTPStatus

import requests


def criar_sessao_suap(matricula: str, senha: str) -> requests.Session | None:
    s = requests.Session()

    with s.post(
        "https://suap.ifrn.edu.br/api/token/pair",
        json={"username": matricula, "password": senha},
    ) as response:
        if response.status_code == HTTPStatus.OK:
            s.headers["Authorization"] = f"Bearer {response.json()['access']}"
        else:
            return None

    return s


def main() -> None:
    print(50 * "-")
    matricula = input("Digite sua matrícula: ")
    senha = getpass("Digite sua senha: ", echo_char="*")

    # A sessão é um elemento já configurado com a autenticação.
    # Podemos usar ela para fazer múltiplas requisições,
    # sem precisar repetir o processo de autenticação
    sessao = criar_sessao_suap(matricula, senha)

    if sessao is None:
        print("Erro de autenticação!")
    else:
        print("Autenticado com sucesso!")
        print(50 * "-")

        # Consulta de dados do usuário
        with sessao.get("https://suap.ifrn.edu.br/api/rh/eu") as resposta:
            if resposta.status_code == HTTPStatus.OK:
                json_data = resposta.json()

                print("Matrícula:", json_data["identificacao"])
                print("Nome:", json_data["nome"])
                print("E-Mail:", json_data["email"])
                print("Campus:", json_data["campus"])
                print("Categoria:", json_data["tipo_usuario"])
            else:
                print("Erro ao consultar dados do usuário:", resposta.status_code)

        print(50 * "-")

        # Consulta de estatísticas institucionais
        with sessao.get("https://suap.ifrn.edu.br/api/institucional/estatisticas") as resposta:
            if resposta.status_code == HTTPStatus.OK:
                json_data = resposta.json()

                print("Número de alunos ativos:", json_data["results"]["alunos_ativos"])
                print("Número de servidores ativos:", json_data["results"]["servidores_ativos"])
            else:
                print("Erro ao consultar estatísticas institucionais:", resposta.status_code)

    print(50 * "-")


if __name__ == "__main__":
    main()
