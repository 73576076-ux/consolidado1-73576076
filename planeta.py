import math


class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float,
                 distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = masa                          # kg
        self.radio = radio                        # metros
        self.distancia_al_sol = distancia_al_sol  # UA
        self.tiene_vida = tiene_vida



   
    def calcular_densidad(self) -> float:
        volumen = (4 / 3) * math.pi * self.radio ** 3
        return self.masa / volumen

    def es_planeta_exterior(self) -> bool:
        return self.distancia_al_sol > 5.2     




    
    def __str__(self) -> str:
        tipo = "exterior" if self.es_planeta_exterior() else "interior"
        return (f"Planeta {self.nombre} | Densidad: {self.calcular_densidad():.2f} kg/m³ "
                f"| Tipo: {tipo}")


# ---- Instancias de prueba ----
tierra = Planeta("Tierra", 5.972e24, 6.371e6, 1.0, True)
jupiter = Planeta("Júpiter", 1.898e27, 6.9911e7, 5.203)

print(tierra)
print(jupiter)
print("¿Tierra es exterior?", tierra.es_planeta_exterior())
print("¿Júpiter es exterior?", jupiter.es_planeta_exterior())