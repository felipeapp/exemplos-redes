from dataclasses import asdict
from datetime import date, datetime
from secrets import compare_digest
from typing import Any

import alunodao
from comum import API_KEY, Aluno
from flask import Flask, Response, abort, make_response, request
from flask.json.provider import DefaultJSONProvider


class UpdatedJSONProvider(DefaultJSONProvider):
    def default(self, o: Any, *args: Any, **kwargs: Any) -> Any:
        if isinstance(o, (date, datetime)):
            return o.isoformat()
        return super().default(o, *args, **kwargs)


app = Flask("Diário de Alunos na Nuvem")
app.json = UpdatedJSONProvider(app)
alunodao.criar_tabela()


def criar_resposta(dados: Any, codigo: int) -> Response:
    return make_response(dados, codigo)


def criar_erro(mensagem: str, codigo: int) -> Response:
    return make_response({"erro": mensagem}, codigo)


@app.before_request
def autenticacao() -> None:
    chave = request.headers.get("API-KEY", "")

    if not compare_digest(chave, API_KEY):
        abort(criar_erro("Chave de API inválida!", 401))


@app.route("/alunos", methods=["POST"])
def adicionar() -> Response:
    if request.is_json and request.json:
        try:
            aluno = alunodao.adicionar(Aluno(**request.json))
            resposta = (
                criar_resposta(asdict(aluno), 201)
                if aluno
                else criar_erro("Conflito de dados ao adicionar aluno!", 409)
            )
        except TypeError:
            resposta = criar_erro("O formato dos dados é inválido!", 400)
    else:
        resposta = criar_erro("O tipo da mensagem é inválido!", 415)

    return resposta


@app.route("/alunos", methods=["GET"])
def listar() -> Response:
    alunos = alunodao.listar()
    return criar_resposta(alunos, 200) if alunos else criar_erro("Não há alunos cadastrados!", 404)


@app.route("/alunos/<int:matricula>", methods=["GET"])
def buscar_por_matricula(matricula: int) -> Response:
    aluno = alunodao.buscar_por_matricula(matricula)
    return criar_resposta(asdict(aluno), 200) if aluno else criar_erro("A mátricula não foi encontrada!", 404)


@app.route("/alunos/<int:matricula>", methods=["DELETE"])
def remover_por_matricula(matricula: int) -> Response:
    sucesso = alunodao.remover_por_matricula(matricula)
    return criar_resposta("", 204) if sucesso else criar_erro("A mátricula não foi encontrada!", 404)


@app.route("/alunos", methods=["PUT"])
def atualizar() -> Response:
    if request.is_json and request.json:
        try:
            aluno = Aluno(**request.json)

            if alunodao.buscar_por_id(aluno.id):
                resposta = (
                    criar_resposta("", 204)
                    if alunodao.atualizar(aluno)
                    else criar_erro("Conflito de dados ao atualizar aluno!", 409)
                )
            else:
                resposta = criar_erro("O ID não foi encontrado!", 404)
        except TypeError:
            resposta = criar_erro("O formato dos dados é inválido!", 400)
    else:
        resposta = criar_erro("O tipo da mensagem é inválido!", 415)

    return resposta


# Para executar com gunicorn e https use:
# gunicorn -b 127.0.0.1:4443 servidor:app --certfile certs/flask.crt --keyfile certs/flask.key --access-logfile -
if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True, ssl_context=("certs/flask.crt", "certs/flask.key"))
