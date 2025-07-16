# Podemos usar chaves para criar um set
conjunto = {"Felipe", "Henio", "Matheus", "Felipe"}  # noqa: B033

# Mostra o set, não terá repetição
print(conjunto)

# Quantidade de elementos do conjunto
print(len(conjunto))

# Verifica se o elemento existe ou não no conjunto
print("Felipe" in conjunto)
print("Felipe" not in conjunto)

# Adiciona um elemento no conjunto
conjunto.add("João")
conjunto.add("Gustavo")
conjunto.add("Mary")
conjunto.add("Henio")
conjunto.add("Mary")
print(conjunto)

# Remove um elemento, causa exceção se ele não existir
conjunto.remove("Felipe")
# conjunto.remove("Maria")
print(conjunto)

# Remove um elemento, se ele existir
conjunto.discard("Maria")
conjunto.discard("Henio")
print(conjunto)

# Remove e retorna um elemento qualquer
elemento = conjunto.pop()
print(f"Elemento removido: {elemento}")
print(conjunto)

# Remove todos os elementos
conjunto.clear()
print(conjunto)

# Gerando um set a partir de uma lista já existente
lista = ["Felipe", "Henio", "Matheus", "Felipe"]
conjunto = set(lista)
print(conjunto)

# Criando um set vazio
vazio = set()
print(type(vazio))
print(vazio)

# Isto não é um set, e sim um dicionário vazio
vazio = {}
print(type(vazio))
print(vazio)
