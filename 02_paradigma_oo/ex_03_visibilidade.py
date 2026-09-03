# Exemplo de mapeamento do diagrama de classes do slide 03.


class Dispositivo:
    def __init__(self, nome: str, ip: str, status: str) -> None:
        self.__nome = nome  # Atributo privado
        self._ip = ip  # Atributo protegido
        self.status = status  # Atributo público

    def definir_ip(self, novo_ip: str) -> None:
        self.ip = novo_ip

    def esta_ativo(self) -> bool:
        return self.status == "ativo"

    def imprimir(self) -> None:
        print(f"Nome: {self.__nome}, IP: {self._ip}, Status: {self.status}")


d = Dispositivo("Switch 1", "10.230.0.4", "ativo")
d.__nome = "Roteador"  # Por convenção, não deveria acessar diretamente, mas não gera erro
d._ip = "10.225.0.4"  # Por convenção, não deveria acessar diretamente, mas não gera erro
d.status = "inativo"  # Público, pode ser acessado diretamente

# Veja que será mostrado: Nome: Switch 1, IP: 10.225.0.4, Status: inativo
# Ou seja, o atributo privado não foi alterado, mas o protegido e o público foram.
d.imprimir()
