arquivo = open("contatos.txt", "w", encoding="utf-8")  # noqa: SIM115

# O write escreve dentro do arquivo, similar ao print para terminal, mas não quebra linha por padrão
arquivo.write("olá arquivo\n")
arquivo.write("olá arquivo de novo\n")

# O writelines pode ser usado para escrever toda uma lista de elementos dentro do arquivo
dados = ["Felipe\n", "Alves\n", "Maria\n", "Ana\n"]
arquivo.writelines(dados)

# Quando trabalhando com escrita, podemos perder dados caso o arquivo não seja fechado
arquivo.close()
