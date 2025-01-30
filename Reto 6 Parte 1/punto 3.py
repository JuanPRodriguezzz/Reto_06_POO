# Excepciones personalizadas
class ListaVaciaException(Exception):
    """Excepción si la lista o string está vacía."""
    pass

class Primos:
    def __init__(self):
        pass

    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def obtener_primos(lista):
        primos = []
        for item in lista:
            try:
                numero = int(item)
                if Primos.es_primo(numero):
                    primos.append(numero)
            except ValueError:
                print(f"[Aviso] \"{item}\" no es un número entero válido. Se ignora.")
        return primos

    def ejecutar(self):
        while True:
            try:
                entrada = input("Ingrese una lista de números separados por comas y sin espacios: ")
                if not entrada.strip():
                    # Excepción si no hay nada en la entrada
                    raise ListaVaciaException("No se ingresaron datos. La lista está vacía.")

                numeros = entrada.split(',')
                primos_encontrados = self.obtener_primos(numeros)
                print("\nNúmeros primos en la lista:", primos_encontrados)
            # Excepciones para el bloque Except
            except ListaVaciaException as le:
                print(f"\nError: {str(le)}")
            except Exception as e:
                print(f"\nError inesperado: {str(e)}")

primos_checker = Primos()
primos_checker.ejecutar()