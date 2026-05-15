from especies import Flor, Cactus
from logica import ServicioBotanico

def iniciar_programa():
    sistema = ServicioBotanico()
    
    sistema.agregar_planta(Flor("Girasol", "Helianthus", "Amarillo"))
    sistema.agregar_planta(Cactus("Saguaro", "Carnegiea", True))
    
    print("\n--- Ejecutando Polimorfismo ---")
    for p in sistema.listar_plantas():
        print(f"Planta: {p} -> Cuidado: {p.obtener_cuidados()}")
    
    sistema.guardar_en_disco()

if __name__ == "__main__":
    iniciar_programa()
