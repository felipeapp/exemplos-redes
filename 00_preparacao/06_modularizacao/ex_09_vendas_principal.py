from ex_09_vendas_funcoes import buscar_por_codigo, calcular_rendimento, imprimir_venda


# Solução modelada para lista de listas
# [
#      codigo,     nome, valor, dia, mes,  ano
#     [   100, "Felipe", 99.99,  12,  12, 2022],
#     [   101,  "Maria", 50.99,   1,  10, 2022],
#     [   102,   "João",  9.99,   12, 10, 2022]
# ]
def main() -> None:  # noqa: C901, PLR0912
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
        elif opcao == 1:  # noqa: RET508
            codigo = int(input("Digite o código: "))

            if buscar_por_codigo(vendas, codigo) is None:
                nome = input("Nome do cliente: ")
                valor = float(input("Valor da venda: "))
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))

                vendas.append([codigo, nome, valor, dia, mes, ano])
                print("Cadastro da venda realizado!")
            else:
                print("O código já está cadastrado!")
        elif opcao == 2:
            if vendas:
                for v in vendas:
                    imprimir_venda(v)
            else:
                print("Não há vendas cadastradas!")
        elif opcao == 3:
            codigo = int(input("Digite o código da busca: "))
            v = buscar_por_codigo(vendas, codigo)

            if v is None:
                print("O código informado não foi encontrado!")
            else:
                imprimir_venda(v)
        elif opcao == 4:
            mes = int(input("Digite o mês da busca: "))
            ano = int(input("Digite o ano da busca: "))

            total = calcular_rendimento(vendas, mes, ano)

            if total == 0:
                print("Não houve vendas no período!")
            else:
                print(f"O total de vendas para o período foi R$ {total:.2f}")
        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    main()
