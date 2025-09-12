from dataclasses import asdict, dataclass
from json import dump, dumps, load


@dataclass
class Venda:
    codigo: int
    nome: str
    valor: float
    sucesso: bool


venda = Venda(1, "Felipe", 99.90, True)

print(venda)
print(asdict(venda))
print(dumps(asdict(venda)))

with open("venda.json", "w", encoding="utf-8") as arquivo:
    dump(asdict(venda), arquivo)

with open("venda.json", encoding="utf-8") as arquivo:
    dados_dic = load(arquivo)

print(dados_dic)

dados_dc = Venda(**dados_dic)
print(dados_dc)
