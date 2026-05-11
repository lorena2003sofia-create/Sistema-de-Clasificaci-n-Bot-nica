from archivo import Archivador

class ServicioBotanico:
    def __init__(self):
        self.catalogo = []

    def agregar_planta(self, planta):
        self.catalogo.append(planta)

    def guardar_en_disco(self):
        return Archivador.guardar(self.catalogo)

    def listar_plantas(self):
        return self.catalogo
