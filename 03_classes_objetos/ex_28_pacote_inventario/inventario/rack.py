from inventario.dispositivo import Dispositivo


class Rack:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.dispositivos: list[Dispositivo] = []

    def adicionar(self, dispositivo: Dispositivo) -> None:
        self.dispositivos.append(dispositivo)

    def total_ativos(self) -> int:
        return len([d for d in self.dispositivos if d.esta_ativo()])

    def __str__(self) -> str:
        return f"Rack {self.nome}: {len(self.dispositivos)} dispositivos, {self.total_ativos()} ativos"
