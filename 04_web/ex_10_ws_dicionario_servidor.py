from flask import Flask, Response, make_response, request

app = Flask("Serviço de Dicionário Web")
dicionario = {}


def criar_resposta(mensagem: str | dict[str, str], codigo: int) -> Response:
    return make_response({"resposta": mensagem}, codigo)


@app.route("/palavras", methods=["GET"])
def buscar_todos() -> dict[str, str]:
    return dicionario


@app.route("/palavras/<string:palavra>", methods=["GET", "DELETE"])
def buscar_ou_remover(palavra: str) -> Response:
    if palavra in dicionario:
        resposta = criar_resposta({palavra: dicionario[palavra]}, 200)

        if request.method == "DELETE":
            del dicionario[palavra]
    else:
        resposta = criar_resposta("Palavra não encontrada!", 404)

    return resposta


@app.route("/palavras", methods=["POST", "PUT"])
def adicionar_ou_atualizar() -> Response:
    if request.is_json and request.json:
        # Neste exemplo usamos o método get de request.json.get("...")
        # Assim, fazemos a validação do retorno com estruturas if-else
        # Outra forma seria usar request.json["..."] e validar com exceções, ver o exemplo 9
        palavra = request.json.get("palavra")
        significado = request.json.get("significado")

        if palavra is None or significado is None:
            resposta = criar_resposta("O formato do JSON é inválido!", 400)
        else:
            resposta = criar_resposta({palavra: significado}, 200 if palavra in dicionario else 201)
            dicionario[palavra] = significado
    else:
        resposta = criar_resposta("A requisição não possui um JSON!", 415)

    return resposta


app.run("localhost", 8080, debug=True)
