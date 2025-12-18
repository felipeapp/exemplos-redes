from flask import Flask

app = Flask("Primeiro Serviço Web")


@app.route("/", methods=["GET"])
def ola() -> str:
    return "Olá, sou um serviço web!"


@app.route("/disciplina", methods=["GET"])
def disciplina_get() -> str:
    return "Usando GET, estamos na disciplina de programação!"


@app.route("/disciplina", methods=["POST"])
def disciplina_post() -> str:
    return "Usando POST, estamos na disciplina de programação!"


if __name__ == "__main__":
    app.run("127.0.0.1", port=8080)
