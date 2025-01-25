import sqlite3

BANCO_ARQUIVO = "exemplo.db"


def criar_tabela():
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        conexao.execute(
            """
            create table if not exists aluno (
                id integer primary key not null,
                nome text not null,
                matricula integer unique not null,
                ira real not null
            )
            """
        )


def adicionar(nome, matricula, ira):
    try:
        with sqlite3.connect(BANCO_ARQUIVO) as conexao:
            cur = conexao.execute(
                "insert into aluno (nome, matricula, ira) values (?, ?, ?)", (nome, matricula, ira)
            )
            sucesso = cur.rowcount == 1
    except sqlite3.Error:
        sucesso = False

    return sucesso


def buscar_por_matricula(matricula):
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("select * from aluno where matricula = ?", (matricula,))
        aluno = cur.fetchone()

    return aluno


def listar():
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("select * from aluno")
        alunos = cur.fetchall()

    return alunos


def main():
    criar_tabela()
    print("Tabela criada!")

    if adicionar("Felipe", 1234, 9.5):
        print("Inserção 1 com sucesso!")
    else:
        print("Inserção 1 falhou!")

    if adicionar("Alcivan", 8080, 7.5):
        print("Inserção 2 com sucesso!")
    else:
        print("Inserção 2 falhou!")

    print(buscar_por_matricula(1234))
    print(buscar_por_matricula(78677))

    print(listar())


if __name__ == "__main__":
    main()
