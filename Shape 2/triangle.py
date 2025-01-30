from exceptions import DegenerateTriangleException
from shape import Shape
from point import Point
from line import Line
from math import sqrt

class Triangle(Shape):
    """Clase que representa un triángulo."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        vertices = [vertex1, vertex2, vertex3]

        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0])
        ]

        super().__init__(vertices, edges)

        # Verifica que sea un triángulo (área > 0)
        if abs(self.compute_area()) < 0:
            raise DegenerateTriangleException(
                "Los puntos son colineales; no se forma un triángulo."
            )

    def compute_area(self):
        """Calcula el área usando la fórmula de Herón."""
        a, b, c = (edge.get_length() for edge in self.edges)
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5