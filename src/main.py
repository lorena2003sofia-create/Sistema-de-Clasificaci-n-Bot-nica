from domain import Flor, Cactus
from persistence import Archivador

def ejecutar():
    catalogo = [
        Flor("Girasol", "Helianthus", "Amarillo"),
        Cactus("Saguaro", "Carnegiea", True)
    ]
    
    print("--- Sistema Botanico ---")
    for p in catalogo:
        print(f"Registrando: {p}")
    
    Archivador.guardar(catalogo)

if __name__ == "__main__":
    ejecutar() 
