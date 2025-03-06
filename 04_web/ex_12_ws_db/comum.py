from dataclasses import dataclass
from datetime import date, datetime

API_KEY = "M83rZ7XX9GRm81pfTQuBpUbMXDIYO_ls7Ims2acJdLE"

# Use este se rodar nativamente com Flask e http
# URL_ALUNOS = "http://127.0.0.1:8080/alunos"

# Use este se rodar o servidor com gunicorn e https
URL_ALUNOS = "https://127.0.0.1:4443/alunos"


@dataclass
class Aluno:
    nome: str
    matricula: int
    ira: float
    id: int = 0
    cadastro: datetime | None = None


def imprimir(aluno: Aluno) -> None:
    print("ID:", aluno.id)
    print("Nome:", aluno.nome)
    print("Matrícula:", aluno.matricula)
    print("IRA:", aluno.ira)

    if aluno.cadastro:
        if isinstance(aluno.cadastro, str):
            print("Data de Cadastro:", datetime.fromisoformat(aluno.cadastro).strftime("%d/%m/%Y, %H:%M:%S"))
        elif isinstance(aluno.cadastro, (date, datetime)):
            print("Data de Cadastro:", aluno.cadastro.strftime("%d/%m/%Y, %H:%M:%S"))
