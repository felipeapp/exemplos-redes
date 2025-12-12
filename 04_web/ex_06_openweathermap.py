from http import HTTPStatus

import requests

latitude = input("Digite a latitude da localização: ")
longitude = input("Digite a longitude da localização: ")

parametros = {
    "lat": latitude,
    "lon": longitude,
    "units": "metric",
    "lang": "pt_br",
    "appid": "",
}

with requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params=parametros,
    timeout=10,
) as resposta:
    if resposta.status_code == HTTPStatus.OK:
        dados = resposta.json()

        print(40 * "-")

        print(f"ID da Localidade: {dados['id']}")
        print(f"Nome da Localidade: {dados['name']}")
        print(f"Temperatura Atual: {dados['main']['temp']}ºC")
        print(f"Pressão Atmosférica: {dados['main']['pressure']}hPa")
        print(f"Umidade do Ar: {dados['main']['humidity']}%")
        print(f"Velocidade do Vento: {dados['wind']['speed']}m/s")

        if dados["weather"]:
            print(f"Nuvens: {dados['weather'][0]['description']}")

        print(40 * "-")
    else:
        print(f"Erro ao realizar requisição: {resposta.status_code}!")
