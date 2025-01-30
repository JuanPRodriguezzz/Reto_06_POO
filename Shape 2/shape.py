from point import Point
from line import Line
from math import acos, degrees

class Shape:
    """Superclase que representa una figura geométrica."""
    def __init__(self, vertices: list[Point], edges: list[Line]):
        self.vertices = vertices
        self.edges = edges
        self.inner_angles = self.compute_inner_angles()
        self.is_regular = self.check_regular()

    def compute_area(self):
        """
        Método abstracto (no implementado) que las subclases deben sobrescribir.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self.edges)

    def compute_inner_angles(self):
        """Calcula los ángulos internos (solo para polígonos convexos)."""
        angles = []
        for i in range(len(self.vertices)):
            p1 = self.vertices[i - 1]
            p2 = self.vertices[i]
            p3 = self.vertices[(i + 1) % len(self.vertices)]

            a = p1.compute_distance(p2)
            b = p2.compute_distance(p3)
            c = p1.compute_distance(p3)

            angle = acos((a**2 + b**2 - c**2) / (2 * a * b))
            angles.append(degrees(angle))
        return angles

    def check_regular(self):
        """Verifica si la figura es regular."""
        if len(self.edges) < 3:
            return False

        first_length = self.edges[0].get_length()
        first_angle = self.inner_angles[0]

        return all(edge.get_length() == first_length for edge in self.edges) and \
               all(angle == first_angle for angle in self.inner_angles)