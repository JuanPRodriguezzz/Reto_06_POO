from exceptions import NotRightTriangleException
from point import Point
from triangle import Triangle

class TriRectangle(Triangle):
    """Clase que representa un triángulo rectángulo."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(vertex1, vertex2, vertex3)
        a, b, c = sorted(edge.get_length() for edge in self.edges)
        # Verifica si es triángulo rectángulo
        if not abs(c**2 - (a**2 + b**2)) < 1e-9:
            raise NotRightTriangleException("No es un triángulo rectángulo.")