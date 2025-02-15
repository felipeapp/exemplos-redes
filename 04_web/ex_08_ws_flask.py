from flask import Flask

app = Flask("Primeiro Serviço Web")


@app.route("/", methods=["GET"])
def ola():
    return "Olá, sou um serviço web!"


@app.route("/disciplina", methods=["GET"])
def disciplina_get():
    return "Usando GET, estamos na disciplina de programação!"


@app.route("/disciplina", methods=["POST"])
def disciplina_post():
    return "Usando POST, estamos na disciplina de programação!"


app.run("0.0.0.0", port=8080, debug=True)
