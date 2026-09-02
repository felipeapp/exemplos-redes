while True:
    nome_completo = input("Digite seu nome completo: ").strip()

    if " " in nome_completo:
        break

    print("Nome inválido, tente novamente!")

primeiro_espaco = nome_completo.index(" ")
ultimo_espaco = nome_completo.rindex(" ")

primeiro_nome = nome_completo[:primeiro_espaco].capitalize()
ultimo_nome = nome_completo[ultimo_espaco + 1 :].capitalize()

print(f"Olá {primeiro_nome} {ultimo_nome}, bem vindo a aula de programação!")
