from exceptions import InvalidPointException
from math import sqrt

class Point:
    """Clase que representa un punto en un plano bidimensional."""
    def __init__(self, x: float = 0, y: float = 0):
        # Validar que x e y sean float o int
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise InvalidPointException("Las coordenadas deben ser numéricas.")
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        # Validación para el valor de X
        if not isinstance(value, (int, float)):
            raise InvalidPointException("Coordenada X no válida.")
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        # Validación para el valor de X
        if not isinstance(value, (int, float)):
            raise InvalidPointException("Coordenada Y no válida.")
        self._y = value

    def compute_distance(self, other_point):
        return sqrt((self.get_x() - other_point.get_x())**2 + (self.get_y() - other_point.get_y())**2)