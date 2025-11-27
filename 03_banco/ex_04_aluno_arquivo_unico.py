import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime

BANCO_ARQUIVO = "exemplo.db"


@dataclass
class Aluno:
    nome: str
    matricula: int
    ira: float
    id: int = 0
    cadastro: datetime | None = None


def criar_tabela() -> None:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        conexao.execute(
            """
            create table if not exists aluno (
                id integer primary key not null,
                nome text not null,
                matricula integer unique not null,
                ira real not null,
                cadastro timestamp not null default (datetime('now', 'localtime'))
            )
            """,
        )


def adicionar(aluno: Aluno) -> bool:
    try:
        with sqlite3.connect(BANCO_ARQUIVO) as conexao:
            cur = conexao.execute(
                "insert into aluno (nome, matricula, ira) values (:nome, :matricula, :ira)",
                asdict(aluno),
            )
            sucesso = cur.rowcount == 1
    except sqlite3.Error:
        sucesso = False

    return sucesso


def buscar_por_matricula(matricula: int) -> Aluno | None:
    with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("select * from aluno where matricula = ?", (matricula,))

        linha = cur.fetchone()
        return Aluno(**linha) if linha else None


def remover(matricula: int) -> bool:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("delete from aluno where matricula = ?", (matricula,))
        return cur.rowcount == 1


def listar() -> list[Aluno]:
    with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("select * from aluno")
        return [Aluno(**linha) for linha in cur]


def imprimir(aluno: Aluno) -> None:
    print("ID:", aluno.id)
    print("Nome:", aluno.nome)
    print("Matrícula:", aluno.matricula)
    print("IRA:", aluno.ira)

    if aluno.cadastro:
        print("Data de Cadastro:", aluno.cadastro.strftime("%d/%m/%Y %H:%M:%S"))


def main() -> None:  # noqa: C901, PLR0912
    criar_tabela()

    while True:
        print(30 * "-")
        print("0 - Sair do programa")
        print("1 - Adicionar aluno")
        print("2 - Buscar por matrícula")
        print("3 - Listar")
        print("4 - Remover")
        opcao = int(input("Escolha sua opção: "))

        if opcao == 0:
            print("Saindo do programa...")
            break

        if opcao == 1:
            nome = input("Digite o nome do aluno: ")
            matricula = int(input("Digite a matrícula do aluno: "))
            ira = float(input("Digite o IRA do aluno: "))

            aluno = Aluno(nome, matricula, ira)

            if adicionar(aluno):
                print("Aluno cadastrado com sucesso!")
            else:
                print("Algum dado do aluno já cadastrado!")
        elif opcao == 2:
            matricula = int(input("Digite a matrícula do aluno: "))
            aluno = buscar_por_matricula(matricula)

            if aluno:
                imprimir(aluno)
            else:
                print("Matrícula não encontrada!")
        elif opcao == 3:
            alunos = listar()

            if alunos:
                for a in alunos:
                    print(5 * "-")
                    imprimir(a)
            else:
                print("Não há alunos cadastrados!")
        elif opcao == 4:
            matricula = int(input("Digite a matrícula do aluno: "))

            if remover(matricula):
                print("Aluno removido com sucesso!")
            else:
                print("Matrícula não encontrada!")
        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    main()
