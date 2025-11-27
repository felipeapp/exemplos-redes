import sqlite3
from dataclasses import asdict

from modelo.entidade.produto import Produto

BANCO_ARQUIVO = "estoque.db"


def criar_tabela_produto() -> None:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        conexao.execute(
            """
            create table if not exists produto (
                id integer primary key not null,
                nome text check(length(nome) between 2 and 50) unique not null,
                preco real check(preco > 0) not null,
                quantidade integer check(quantidade >= 0) not null,
                medida text check(medida in ('ML', 'L', 'KG', 'G', 'UNIDADE')) not null,
                cadastro timestamp not null default (datetime('now', 'localtime'))
            )
            """,
        )


def adicionar_produto(produto: Produto) -> bool:
    try:
        with sqlite3.connect(BANCO_ARQUIVO) as conexao:
            cur = conexao.execute(
                "insert into produto (nome, preco, quantidade, medida) values"
                "(:nome, :preco, :quantidade, :medida)",
                asdict(produto),
            )
            sucesso = cur.rowcount == 1
    except sqlite3.Error as erro:
        print(erro)
        sucesso = False

    return sucesso


def atualizar_produto(nome: str, novo_preco: float, nova_quantidade: int) -> bool:
    try:
        with sqlite3.connect(BANCO_ARQUIVO) as conexao:
            cur = conexao.execute(
                "update produto set preco = ?, quantidade = ? where nome = ?",
                (novo_preco, nova_quantidade, nome),
            )
            sucesso = cur.rowcount == 1
    except sqlite3.Error as erro:
        print(erro)
        sucesso = False

    return sucesso


def remover_produto(nome: str) -> bool:
    with sqlite3.connect(BANCO_ARQUIVO) as conexao:
        cur = conexao.execute("delete from produto where nome = ?", (nome,))
        return cur.rowcount == 1


def listar_produtos() -> list[Produto]:
    with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("select * from produto")

        # produtos = []
        # for linha in cur:
        #     produtos.append(Produto(**linha))
        # return produtos
        return [Produto(**linha) for linha in cur]


def buscar_por_nome_exato(nome: str) -> Produto | None:
    with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("select * from produto where nome = ?", (nome,))
        linha = cur.fetchone()

    return Produto(**linha) if linha else None


def buscar_por_nome_similar(nome: str) -> list[Produto]:
    with sqlite3.connect(BANCO_ARQUIVO, detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("select * from produto where nome like ?", (f"%{nome}%",))

        # produtos = []
        # for linha in cur:
        #     produtos.append(Produto(**linha))
        # return produtos
        return [Produto(**linha) for linha in cur]
