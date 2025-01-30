# Excepciones personalizadas
class EntradaInvalidaException(Exception):
    """Excepción si la entrada no es válida."""
    pass

class OperadorInvalidoException(Exception):
    """Excepción si el operador no es correcto."""
    pass

class DivisionPorCeroException(Exception):
    """Excepción cuando se intenta dividir entre cero."""
    pass

class Calculadora:

    def __init__(self):
        pass

    def operaciones_basicas(self, num1, num2, operador):
        # Verificaciones previas (validación)
        if operador not in ['+', '-', '*', '/']:
            raise OperadorInvalidoException(f"Operador '{operador}' no válido. Debe ser uno de: +, -, *, /.")
        if operador == '/' and num2 == 0:
            raise DivisionPorCeroException("No se puede dividir entre cero.")

        # Realizar la operación
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2

        return resultado

    def ejecutar(self):
        while True:
            try:
                entrada = input("Ingrese el 1er número, el 2do y el operador separados por comas (num1,num2,operador): ")
                # Excepción si no hay nada en la entrada
                if not entrada.strip():
                    raise EntradaInvalidaException("No se ingresó ningún valor. Debe ingresar num1,num2,operador.")

                num1_str, num2_str, operador = entrada.split(',')
                num1 = float(num1_str)
                num2 = float(num2_str)
                operador = operador.strip()

                # Intentar realizar la operación
                resultado = self.operaciones_basicas(num1, num2, operador)
                print(f"\nResultado: {num1} {operador} {num2} = {resultado}\n")

            # Bloque except para valor de entrada incorrecto, operador no valido, división por cero, entrada no válida o vacia.
            except ValueError:
                print("\nError: Entrada inválida. Asegúrate de usar el formato correcto (num1,num2,operador).")
            except OperadorInvalidoException as oe:
                print(f"\nError: {str(oe)}")
            except DivisionPorCeroException as dz:
                print(f"\nError: {str(dz)}")
            except EntradaInvalidaException as ee:
                print(f"\nError: {str(ee)}")
            except Exception as e:
                # Cualquier otro error
                print(f"\nOcurrió un error: {str(e)}")

calculadora = Calculadora()
calculadora.ejecutar()