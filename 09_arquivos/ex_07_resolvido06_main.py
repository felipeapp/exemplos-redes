from ex_07_resolvido06_leituras import (
    ler_codigo,
    ler_data,
    ler_mes_ano,
    ler_nome,
    ler_opcao,
    ler_valor,
)
from ex_07_resolvido06_vendas import (
    Venda,
    buscar_por_codigo,
    calcular_periodo,
    imprimir,
    listar,
    salvar,
    verificar_arquivo,
)


def main() -> None:  # noqa: PLR0912
    verificar_arquivo()

    while True:
        opcao = ler_opcao()

        if opcao == 0:
            print("Finalizando programa...")
            break
        elif opcao == 1:  # noqa: RET508
            codigo = ler_codigo()
            venda = buscar_por_codigo(codigo)

            if venda is None:
                salvar(Venda(codigo=codigo, nome=ler_nome(), valor=ler_valor(), data=ler_data()))
                print("Cadastro da venda realizado!")
            else:
                print("O código já está cadastrado para a venda:")
                imprimir(venda)
        elif opcao == 2:
            listar()
        elif opcao == 3:
            codigo = ler_codigo()
            resultado = buscar_por_codigo(codigo)

            if resultado is None:
                print("O código não foi encontrado!")
            else:
                imprimir(resultado)
        elif opcao == 4:
            mes = ler_mes_ano("Digite o mês da busca: ", 1, 12)
            ano = ler_mes_ano("Digite o ano da busca: ", 2000, 2024)
            total = calcular_periodo(mes, ano)

            if total == 0:
                print(f"Não houve vendas no período de {mes}/{ano}!")
            else:
                print(f"O total de vendas para o período de {mes}/{ano} foi R${total:.2f}")
        else:
            print("Opção inválida, tente novamente!")


try:
    main()
except KeyboardInterrupt:
    print("\nExecução cancelada pelo usuário!")
