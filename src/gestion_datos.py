class Archivador:
    @staticmethod
    def guardar(plantas, nombre_archivo="herbario.txt"):
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                for p in plantas:
                    f.write(f"{p.especie} | {p.nombre_comun} | {p.obtener_cuidados()}\n")
            return True
        except Exception as e:
            print(f"Error al escribir: {e}")
            return False
