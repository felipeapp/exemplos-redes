paes = int(input("Digite a quantidade de pães: "))
envelhecidos = int(input(f"Dos {paes} pães, quantos são envelhecidos? "))

unidade = 0.25
preco_total_sem_desconto = paes * unidade
preco_paes_envelhecidos = envelhecidos * unidade * 0.5
preco_paes_novos = (paes - envelhecidos) * unidade
preco_total_com_desconto = preco_paes_envelhecidos + preco_paes_novos
valor_desconto = preco_total_sem_desconto - preco_total_com_desconto

print(f"Preço total sem desconto: R$ {preco_total_sem_desconto:.2f}")
print(f"Preço total com desconto: R$ {preco_total_com_desconto:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
