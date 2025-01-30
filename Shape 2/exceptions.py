class InvalidPointException(Exception):
    """Excepcion cuando los valores de un punto no son válidos (ej. no numéricos)."""
    pass

class NegativeDimensionException(Exception):
    """Excepción cuando se detectan dimensiones negativas o iguales a cero."""
    pass

class DegenerateTriangleException(Exception):
    """Cuando el área de un triángulo es cero, indicando que los puntos son colineales y no forman un triángulo."""
    pass

class NotIsoscelesTriangleException(Exception):
    """Cuando se verifica que un triángulo sea isósceles pero no cumple."""
    pass

class NotEquilateralTriangleException(Exception):
    """Cuando se verifica que un triángulo sea equilátero pero no cumple."""
    pass

class NotScaleneTriangleException(Exception):
    """Cuando se verifica que un triángulo sea escaleno pero no cumple."""
    pass

class NotRightTriangleException(Exception):
    """Cuando se verifica que un triángulo sea rectángulo pero no cumple."""
    pass