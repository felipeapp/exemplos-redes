from dataclasses import asdict

import requests
from comum import API_KEY, URL_ALUNOS, Aluno, imprimir
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


def criar_sessao() -> requests.Session:
    sessao = requests.Session()
    sessao.headers["API-KEY"] = API_KEY

    # Estas duas linhas são necessárias apenas se usando certificados auto-assinados
    sessao.verify = False
    disable_warnings(InsecureRequestWarning)

    return sessao


def main() -> None:
    sessao = criar_sessao()

    while True:
        print(50 * "-")
        print("0. Sair do programa")
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Buscar aluno por matrícula")
        print("4. Atualizar aluno")
        print("5. Remover aluno por matrícula")
        opcao = int(input("Digite sua opção: "))

        if opcao == 0:
            print("Finalizando o programa...")
            break
        elif opcao == 1:
            nome = input("Digite o nome do aluno: ")
            matricula = int(input("Digite a matrícula do aluno: "))
            ira = float(input("Digite o IRA do aluno: "))

            with sessao.post(URL_ALUNOS, json=asdict(Aluno(nome, matricula, ira))) as resposta:
                if resposta.status_code == 201:
                    print("Aluno adicionado com sucesso!")
                    imprimir(Aluno(**resposta.json()))
                elif resposta.status_code in (400, 409, 415):
                    print(resposta.json()["erro"], resposta.status_code)
                else:
                    print("Erro desconhecido ao adicionar o aluno", resposta.status_code)
        elif opcao == 2:
            with sessao.get(URL_ALUNOS) as resposta:
                if resposta.status_code == 200:
                    for aluno in resposta.json():
                        print("-")
                        imprimir(Aluno(**aluno))
                elif resposta.status_code == 404:
                    print(resposta.json()["erro"])
                else:
                    print("Erro desconhecido ao listar alunos", resposta.status_code)
        elif opcao == 3:
            matricula = int(input("Digite a matrícula do aluno: "))

            with sessao.get(f"{URL_ALUNOS}/{matricula}") as resposta:
                if resposta.status_code == 200:
                    imprimir(Aluno(**resposta.json()))
                elif resposta.status_code == 404:
                    print(resposta.json()["erro"])
                else:
                    print("Erro desconhecido ao buscar aluno pela matrícula", resposta.status_code)
        elif opcao == 4:
            nome = input("Digite o novo nome do aluno: ")
            matricula = int(input("Digite a nova matrícula do aluno: "))
            ira = float(input("Digite o novo IRA do aluno: "))
            id_aluno = int(input("Digite o ID do aluno a ser atualizado: "))

            with sessao.put(URL_ALUNOS, json=asdict(Aluno(nome, matricula, ira, id_aluno))) as resposta:
                if resposta.status_code == 204:
                    print("Aluno atualizado com sucesso!")
                elif resposta.status_code in (400, 404, 409, 415):
                    print(resposta.json()["erro"])
                else:
                    print("Erro desconhecido ao atualizar o aluno", resposta.status_code)
        elif opcao == 5:
            matricula = int(input("Digite a matrícula do aluno: "))

            with sessao.delete(f"{URL_ALUNOS}/{matricula}") as resposta:
                if resposta.status_code == 204:
                    print("Aluno removido com sucesso!")
                elif resposta.status_code == 404:
                    print(resposta.json()["erro"])
                else:
                    print("Erro desconhecido ao remover aluno", resposta.status_code)
        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    main()
