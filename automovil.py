class Automovil:
    def __init__(self, marca: str, modelo: str, velocidad_max: float,
                 nivel_combustible: float, año_fabricacion: int):
        self.marca = marca
        self.modelo = modelo
        # Se asignan por las propiedades para que se validen desde el inicio
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self) -> int:
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if not (1886 <= valor <= 2026):
            raise ValueError("El año de fabricación debe estar entre 1886 y 2026.")
        self._año_fabricacion = valor

    @property
    def nivel_combustible(self) -> float:
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if not (0.0 <= valor <= 100.0):
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0.")
        self._nivel_combustible = valor

    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor <= 0:
            raise ValueError("La velocidad máxima debe ser mayor a 0.")
        self._velocidad_max = valor



        
    def tiempo_llegada(self, distancia_km: float) -> float:
        return distancia_km / self.velocidad_max