# Solução modelada para lista de listas
# [
#      codigo,     nome, valor, dia, mes,  ano
#     [   100, "Felipe", 99.99,  12,  12, 2022],
#     [   101,  "Maria", 50.99,   1,  10, 2022],
#     [   102,   "João",  9.99,   12, 10, 2022]
# ]
vendas = []

while True:
    print(30 * "-")
    print("0 - Sair do programa")
    print("1 - Cadastrar uma venda")
    print("2 - Listar todas as vendas cadastradas")
    print("3 - Mostrar uma venda a partir de seu código")
    print("4 - Calcular o valor total das vendas em um mês do ano")
    opcao = int(input("Escolha sua opção: "))

    if opcao == 0:
        print("Finalizando programa...")
        break
    elif opcao == 1:
        codigo = int(input("Digite o código: "))

        repetido = False
        for v in vendas:
            if v[0] == codigo:
                repetido = True
                break

        if repetido:
            print("O código já está cadastrado!")
        else:
            nome = input("Nome do cliente: ")
            valor = float(input("Valor da venda: "))
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano: "))

            vendas.append([codigo, nome, valor, dia, mes, ano])
            print("Cadastro da venda realizado!")
    elif opcao == 2:
        if vendas:
            for v in vendas:
                print(f"\nCódigo: {v[0]}")
                print(f"Cliente: {v[1]}")
                print(f"Valor: R${v[2]:.2f}")
                print(f"Data: {v[3]}/{v[4]}/{v[5]}")
        else:
            print("Não há vendas cadastradas!")
    elif opcao == 3:
        codigo = int(input("Digite o código da busca: "))
        indice = -1

        for i, v in enumerate(vendas):
            if v[0] == codigo:
                indice = i
                break

        if indice == -1:
            print("O código informado não foi encontrado!")
        else:
            print(f"\nCódigo: {vendas[indice][0]}")
            print(f"Cliente: {vendas[indice][1]}")
            print(f"Valor: R${vendas[indice][2]:.2f}")
            print(f"Data: {vendas[indice][3]}/{vendas[indice][4]}/{vendas[indice][5]}")
    elif opcao == 4:
        mes = int(input("Digite o mês da busca: "))
        ano = int(input("Digite o ano da busca: "))
        total = 0

        for v in vendas:
            if v[4] == mes and v[5] == ano:
                total += v[2]

        if total == 0:
            print("Não houve vendas no período!")
        else:
            print(f"O total de vendas para o período foi R${total:.2f}")
    else:
        print("Opção inválida, tente novamente!")
