# Excepciones personalizadas
class PalabraVaciaException(Exception):
    """Excepción si la palabra ingresada está vacía."""
    pass

class PalindromoChecker:
    def __init__(self):
        pass

    def verif_palindromo(palabra):
        palabra = palabra.upper()
        longitud = len(palabra)

        for i in range(longitud // 2):
            if palabra[i] != palabra[longitud - i - 1]:
                return False
        return True

    def ejecutar(self):
        while True:
            try:
                palabra = input("\nIngrese una palabra para verificar si es un palíndromo: ").strip()
                if not palabra:
                    # Aquí entra la excepción personalizada si no hay nada en la entrada
                    raise PalabraVaciaException("No se ingresó ninguna palabra.")

                if self.verif_palindromo(palabra):
                    print(f"\n{palabra} es un palíndromo.\n")
                else:
                    print(f"\n{palabra} no es un palíndromo.\n")
            # Excepciones para el bloque Except
            except PalabraVaciaException as pve:
                print(f"\nError: {str(pve)}\n")
            except Exception as e:
                print(f"\nError: {str(e)}\n")

checker = PalindromoChecker()
checker.ejecutar()