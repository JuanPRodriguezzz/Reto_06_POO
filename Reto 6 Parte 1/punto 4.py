# Excepciones personalizadas
class ListaInvalidaException(Exception):
    """Excepción si la lista no cumple con los requisitos mínimos."""
    pass

class MayorSumaConsecutiva:
    def __init__(self):
        pass

    def calcular_mayor_suma(lista):
        if len(lista) < 2:
            # No se puede calcular si hay menos de dos elementos
            return None

        mayor_suma = lista[0] + lista[1]
        for i in range(len(lista) - 1):
            suma_actual = lista[i] + lista[i + 1]
            if suma_actual > mayor_suma:
                mayor_suma = suma_actual
        return mayor_suma

    def ejecutar(self):
        while True:
            try:
                entrada = input("\nIngrese una lista de números enteros separados por espacios: ").strip()
                # Se da la excepción si no se ingresa ningún valor
                if not entrada:
                    raise ListaInvalidaException("No se ingresó ningún valor.")
                # Convertir la entrada en una lista de enteros
                lista = list(map(int, entrada.split()))
                # Se da la excepción si la lista ingresada tiene menos de 2 numeros
                if len(lista) < 2:
                    raise ListaInvalidaException("La lista debe contener al menos dos números.")

                resultado = self.calcular_mayor_suma(lista)
                print(f"\nLa mayor suma entre dos números consecutivos es: {resultado}\n")

            # Excepciones para el bloque Except
            except ListaInvalidaException as lie:
                print(f"\nError: {str(lie)}\n")
            # Valor de entrada incorrecto para la operación
            except ValueError:
                print("\nError: Asegúrese de ingresar solo números enteros separados por espacios.\n")
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {str(e)}\n")


programa = MayorSumaConsecutiva()
programa.ejecutar()