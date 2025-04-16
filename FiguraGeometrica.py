"""Módulo que define figuras geométricas con métodos para calcular áreas."""

from abc import ABC, abstractmethod
from math import pi


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""


    def nombre(self):
        """Devuelve el nombre de la figura."""
        return self.__class__.__name__


class Rectangulo(FiguraGeometrica):
    """Representa un rectángulo con base y altura."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    """Representa un triángulo con base y altura."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):
    """Representa un círculo con un radio."""

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return pi * (self.radio ** 2)


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3


# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")

    # Mostrar el nombre de las figuras
    print(f"Figura 1: {rectangulo.nombre()}")
    print(f"Figura 2: {triangulo.nombre()}")
