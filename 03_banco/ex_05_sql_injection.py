import sqlite3

BANCO_ARQUIVO = "injection.db"


def criar_tabela() -> None:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        conexao.execute(
            """
            create table if not exists aluno (
                id integer primary key not null,
                nome text not null,
                matricula text unique not null
            )
            """,
        )


def adicionar(nome: str, matricula: str) -> bool:
    try:
        with sqlite3.connect(BANCO_ARQUIVO) as conexao:
            cur = conexao.execute("insert into aluno (nome, matricula) values (?, ?)", (nome, matricula))
            sucesso = cur.rowcount == 1
    except sqlite3.Error:
        sucesso = False

    return sucesso


def remover(matricula: str) -> bool:
    # Vulnerabilidade de SQL Injection, NÃO FAZER ASSIM
    sql = f"delete from aluno where matricula = '{matricula}'"  # noqa: S608
    print("SQL:", sql)

    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute(sql)
        return cur.rowcount == 1


def listar() -> list:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("select * from aluno")
        return cur.fetchall()


def listar_por_nome(nome: str) -> list:
    # Vulnerabilidade de SQL Injection, NÃO FAZER ASSIM
    sql = f"select * from aluno where nome = '{nome}'"  # noqa: S608
    print("SQL:", sql)

    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute(sql)
        return cur.fetchall()


def main() -> None:  # noqa: C901, PLR0912
    criar_tabela()

    while True:
        print(40 * "-")
        print("0. Sair")
        print("1. Adicionar")
        print("2. Listar todos")
        print("3. Listar por nome")
        print("4. Remover")
        opcao = int(input(">> "))

        if opcao == 0:
            print("Saindo...")
            break

        if opcao == 1:
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula do aluno: ")

            if adicionar(nome, matricula):
                print("Aluno adicionado!")
            else:
                print("Erro ao adicionar aluno!")
        elif opcao == 2:
            alunos = listar()

            if alunos:
                for a in alunos:
                    print(a)
            else:
                print("Não há alunos cadastrados!")
        elif opcao == 3:
            nome = input("Digite o nome do aluno: ")
            alunos = listar_por_nome(nome)

            if alunos:
                for a in alunos:
                    print(a)
            else:
                print("Nome não encontrado!")
        elif opcao == 4:
            matricula = input("Digite a matrícula do aluno: ")

            if remover(matricula):
                print("Aluno removido com sucesso!")
            else:
                print("Erro ao remover aluno!")
        else:
            print("Inválido, tente novamente!")


if __name__ == "__main__":
    main()
