from flask import Flask, Response, make_response, request

app = Flask("Calculadora Web")


def calcular(operacao: str, numero1: int, numero2: int) -> int | None:
    if operacao == "soma":
        resultado = numero1 + numero2
    elif operacao == "subtracao":
        resultado = numero1 - numero2
    elif operacao == "multiplicacao":
        resultado = numero1 * numero2
    elif operacao == "divisao":
        resultado = numero1 // numero2
    else:
        resultado = None

    print(f"{operacao} entre {numero1} e {numero2} = {resultado}")
    return resultado


@app.route("/", methods=["GET"])
def raiz():
    return "Exemplo: Recuperando Valores da Requisição"


@app.route("/calc/path/<string:operacao>/<int:numero1>/<int:numero2>", methods=["GET"])
def calc_path(operacao: str, numero1: int, numero2: int) -> str | Response:
    resultado = calcular(operacao, numero1, numero2)
    return str(resultado) if resultado is not None else make_response("Operação inválida!", 400)


@app.route("/calc/query")
def calc_query() -> str | Response:
    operacao = request.args.get("operacao", "soma")
    numero1 = int(request.args.get("numero1", "0"))
    numero2 = int(request.args.get("numero2", "0"))

    resultado = calcular(operacao, numero1, numero2)

    return str(resultado) if resultado is not None else make_response("Operação inválida!", 400)


@app.route("/calc/json", methods=["GET"])
def calc_json() -> str | Response:
    if request.is_json and request.json:
        # Exemplo de validação com exceções
        # Também podemos validar com if-else usando o método get -> request.json.get("...")
        # Ver a outra forma no exemplo 10
        try:
            operacao = request.json["operacao"]
            numero1 = request.json["numero1"]
            numero2 = request.json["numero2"]

            resultado = calcular(operacao, numero1, numero2)
            resposta = str(resultado) if resultado is not None else make_response("Operação inválida!", 400)
        except KeyError:
            resposta = make_response("JSON está incompleto!", 400)
    else:
        resposta = make_response("A requisição não possui um JSON!", 415)

    return resposta


app.run("localhost", 8080, debug=True)
