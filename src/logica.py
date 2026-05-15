from archivo import Archivador

class ServicioBotanico:
    def __init__(self):
        self.catalogo = []

    def agregar_planta(self, planta):
        self.catalogo.append(planta)
        print(f"Añadido: {planta.nombre_comun}")

    def guardar_en_disco(self):
        if Archivador.guardar(self.catalogo):
            print("--- Archivo herbario.txt generado con exito ---")

    def listar_plantas(self):
        return self.catalogo
