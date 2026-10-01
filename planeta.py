import math


class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float,
                 distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = masa                          # kg
        self.radio = radio                        # metros
        self.distancia_al_sol = distancia_al_sol  # UA
        self.tiene_vida = tiene_vida