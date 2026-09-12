from datetime import date

VENDA_BARATA = "Barata"
VENDA_MEDIA = "Média"
VENDA_ALTA = "Alta"


class Venda:
    def __init__(self, codigo: int, nome: str, valor: float, data: date) -> None:
        self._codigo = codigo
        self._nome = nome
        self._valor = valor
        self._data = data

    def __str__(self) -> str:
        return f"Código: {self._codigo}\nCliente: {self._nome}\nValor: R${self._valor:.2f}\nData: {self.data}"

    @property
    def data(self) -> str:
        return self._data.strftime("%d/%m/%Y")

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome.strip().upper()

    def classificar(self) -> str:
        if self._valor < 100:
            tipo = VENDA_BARATA
        elif self._valor < 500:
            tipo = VENDA_MEDIA
        else:
            tipo = VENDA_ALTA

        return tipo


# Criando objetos da classe Venda e testando os métodos
v1 = Venda(1, "Felipe", 100.0, date(2024, 6, 1))

# Funciona devido ao método __str__ implementado na classe Venda
print(v1)

# Funciona devido ao property nome implementado na classe Venda
print(v1.nome)

# Funciona devido ao setter nome implementado na classe Venda
v1.nome = "Maria"
print(v1)

# Chamando o método classificar() da classe Venda
print(v1.classificar())

# Lista de objetos da classe Venda
lista_vendas = [
    Venda(1, "Felipe", 99.99, date(2022, 12, 12)),
    Venda(2, "Maria", 50.99, date(2022, 10, 1)),
    Venda(3, "João", 9.99, date(2022, 10, 12)),
    Venda(4, "Ana", 500.00, date(2023, 1, 15)),
]

print(lista_vendas[0].nome)
print(lista_vendas[1].nome)
print(lista_vendas[2].nome)
print(lista_vendas[3].nome)

for venda in lista_vendas:
    print("-" * 30)
    print(venda)
    print(venda.classificar())
