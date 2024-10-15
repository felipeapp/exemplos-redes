from ex_03_resolvido_funcoes import Venda, buscar_por_codigo, calcular_periodo, imprimir
from ex_03_resolvido_leituras import ler_codigo, ler_data, ler_valor


def main() -> None:
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
            codigo = ler_codigo("Digite o código: ", 1)
            resultado = buscar_por_codigo(vendas, codigo)

            if resultado is None:
                nome = input("Nome do cliente: ")
                valor = ler_valor("Digite o valor: ", 0.01)
                data = ler_data("Digite a data (hh:mm dd/mm/aaaa): ")

                vendas.append(Venda(codigo=codigo, nome=nome, valor=valor, data=data))
                print("Cadastro da venda realizado!")
            else:
                print("O código já está cadastrado!")
        elif opcao == 2:
            if vendas:
                for v in vendas:
                    imprimir(v)
            else:
                print("Não há vendas cadastradas!")
        elif opcao == 3:
            codigo = ler_codigo("Digite o código da busca: ", 1)
            resultado = buscar_por_codigo(vendas, codigo)

            if resultado is None:
                print("O código não foi encontrado!")
            else:
                imprimir(resultado)
        elif opcao == 4:
            mes = int(input("Digite o mês da busca: "))
            ano = int(input("Digite o ano da busca: "))
            total = calcular_periodo(vendas, mes, ano)

            if total == 0:
                print("Não houve vendas no período!")
            else:
                print(f"O total de vendas para o período foi R${total:.2f}")
        else:
            print("Opção inválida, tente novamente!")


try:
    main()
except KeyboardInterrupt:
    print("\nExecução cancelada pelo usuário!")
