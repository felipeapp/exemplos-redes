import sqlite3

BANCO_ARQUIVO = "exemplo.db"


def criar_tabela() -> None:
    conexao = sqlite3.connect(BANCO_ARQUIVO)
    cur = conexao.cursor()

    cur.execute("""
        create table if not exists aluno (
            id integer primary key not null,
            nome text not null,
            matricula integer unique not null,
            ira real not null
        )
    """)

    cur.close()
    conexao.close()


def adicionar(nome: str, matricula: int, ira: float) -> bool:
    conexao = sqlite3.connect(BANCO_ARQUIVO)
    cur = conexao.cursor()

    try:
        cur.execute("insert into aluno (nome, matricula, ira) values (?, ?, ?)", (nome, matricula, ira))
        conexao.commit()
        sucesso = cur.rowcount == 1
    except sqlite3.Error:
        sucesso = False
        conexao.rollback()

    cur.close()
    conexao.close()

    return sucesso


def main() -> None:
    criar_tabela()
    print("Tabela criada!")

    if adicionar("Felipe", 123456, 9.5):
        print("Inserção 1 com sucesso!")
    else:
        print("Inserção 1 falhou!")

    if adicionar("Alcivan", 80801, 7.5):
        print("Inserção 2 com sucesso!")
    else:
        print("Inserção 2 falhou!")


if __name__ == "__main__":
    main()
