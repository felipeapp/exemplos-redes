from dataclasses import dataclass


# @dataclass(frozen=True)
@dataclass
class Aluno:
    nome: str
    matricula: int
    nota1: float
    nota2: float
    cidade: str = "São Gonçalo do Amarante"


a1 = Aluno("Felipe", 1234, 9.5, 8.5)
a2 = Aluno("Maria", 4321, 10.0, 6.5, "Macaiba")
a3 = Aluno(nota1=9.8, nota2=6.5, nome="João", matricula=8080)

print()
print(a1)
print(a2)
print(a3)
print()
print("Valores para aluno 1:")
print("Nome:", a1.nome)
print("Matrícula:", a1.matricula)
print("Nota 1:", a1.nota1)
print("Nota 2:", a1.nota2)
print("Média:", (a1.nota1 + a1.nota2) / 2)
print()
print("Valores para aluno 2:")
print("Nome:", a2.nome)
print("Matrícula:", a2.matricula)
print("Nota 1:", a2.nota1)
print("Nota 2:", a2.nota2)
print("Média:", (a2.nota1 + a2.nota2) / 2)
print()
a1.nota1 = 10.0
print(a1)
print()
