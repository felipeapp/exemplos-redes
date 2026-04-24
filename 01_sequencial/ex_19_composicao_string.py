nome = input("Digite seu nome: ")
media = float(input("Digite sua média: "))
faltas = int(input("Digite as faltas: "))

print(nome, "tem média", media, "e", faltas, "faltas!")
print("%s tem média %.2f e %d faltas!" % (nome, media, faltas))  # noqa: UP031 - Prefira usar f-string
print("{} tem média {:.2f} e {} faltas!".format(nome, media, faltas))  # noqa: UP032 - Prefira usar f-string
print(f"{nome} tem média {media:.2f} e {faltas} faltas!")
