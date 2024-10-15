# joao = 0
# severina = 0
# nulos = 0
# brancos = 0
joao = severina = nulos = brancos = 0

while True:
    print(30 * "-")
    print("As opções são:")
    print("0. Finalizar votação")
    print("1. Votar em João Rodrigues")
    print("2. Votar em Severina da Luz")
    print("3. Nulo")
    print("4. Branco")
    opcao = int(input("Entre com o seu voto: "))

    if opcao == 0:
        print("Finalizando votação...")
        break
    elif opcao == 1:
        joao += 1
    elif opcao == 2:
        severina += 1
    elif opcao == 3:
        nulos += 1
    elif opcao == 4:
        brancos += 1
    else:
        print("Opção inválida, tente novamente!")

print(30 * "#")
quantidade = joao + severina + nulos + brancos

if quantidade > 0:
    porcentagem_nulos = 100 * nulos / quantidade
    porcentagem_brancos = 100 * brancos / quantidade

    print(f"Votos para João Rodrigues: {joao}.")
    print(f"Votos para Severina da Luz: {severina}.")
    print(f"Votos Nulos: {nulos}.")
    print(f"Votos Brancos: {brancos}.")
    print(f"Porcentagem de votos nulos: {porcentagem_nulos:.2f}%.")
    print(f"Porcentagem de votos brancos: {porcentagem_brancos:.2f}%.")

    if joao > severina:
        print("O vencedor foi João Rodrigues!")
    elif severina > joao:
        print("A vencedora foi Severina!")
    else:
        print("Empate entre João Rodrigues e Severina da Luz!")
else:
    print("Sem votos nesta eleição!")
