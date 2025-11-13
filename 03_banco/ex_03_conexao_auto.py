import sqlite3

BANCO_ARQUIVO = "exemplo.db"


def criar_tabela() -> None:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        conexao.execute("""
            create table if not exists aluno (
                id integer primary key not null,
                nome text not null,
                matricula integer unique not null,
                ira real not null
            )
        """)


def adicionar(nome: str, matricula: int, ira: float) -> bool:
    try:
        with sqlite3.connect(BANCO_ARQUIVO) as conexao:
            cur = conexao.execute(
                "insert into aluno (nome, matricula, ira) values (?, ?, ?)",
                (nome, matricula, ira),
            )
            sucesso = cur.rowcount == 1
    except sqlite3.Error:
        sucesso = False

    return sucesso


def buscar_por_matricula(matricula: int) -> tuple:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("select * from aluno where matricula = ?", (matricula,))
        return cur.fetchone()


def listar() -> list[tuple]:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("select * from aluno")
        return cur.fetchall()


def main() -> None:
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
