import sqlite3
from dataclasses import asdict

from comum import Aluno

BANCO_ARQUIVO = "diario.db"


def criar_tabela() -> None:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        conexao.execute(
            """create table if not exists aluno (
                id integer primary key not null,
                nome text not null,
                matricula integer unique not null,
                ira real not null,
                cadastro timestamp not null default (datetime('now', 'localtime'))
            )"""
        )


def adicionar(aluno: Aluno) -> Aluno | None:
    try:
        with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
            conexao.row_factory = sqlite3.Row

            cur = conexao.execute(
                "insert into aluno (nome, matricula, ira) values (:nome, :matricula, :ira) returning *",
                asdict(aluno),
            )

            linha = cur.fetchone()
            resposta = Aluno(**linha) if linha else None
    except sqlite3.Error:
        resposta = None

    return resposta


def atualizar(aluno: Aluno) -> bool:
    try:
        with sqlite3.connect(BANCO_ARQUIVO) as conexao:
            cur = conexao.execute(
                "update aluno set nome = :nome, matricula = :matricula, ira = :ira where id = :id",
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
        aluno = Aluno(**linha) if linha else None

    return aluno


def buscar_por_id(id_aluno: int) -> Aluno | None:
    with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("select * from aluno where id = ?", (id_aluno,))

        linha = cur.fetchone()
        aluno = Aluno(**linha) if linha else None

    return aluno


def remover_por_matricula(matricula: int) -> bool:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("delete from aluno where matricula = ?", (matricula,))
        sucesso = cur.rowcount == 1

    return sucesso


def listar() -> list[Aluno]:
    alunos = []

    with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("select * from aluno order by nome")

        for linha in cur:
            alunos.append(Aluno(**linha))

    return alunos
