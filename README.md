# Reto_06_POO
# Juan Pablo Rodríguez Cruz

### 2. In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

```
Shape/
├── __init__.py
├── exceptions.py
├── point.py
├── line.py
├── shape.py
├── rectangle.py
├── square.py
├── triangle.py
└── triangles/
    ├── __init__.py
    ├── isosceles.py
    ├── equilateral.py
    ├── scalene.py
    └── tri_rectangle.py
```
### El paquete está adjunto en el repo como "Shape 2"

## 1. Add the required exceptions in the Reto 1 code assigments.

1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

```python

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
                # Cualquier otro error inesperado
                print(f"\nOcurrió un error: {str(e)}")

calculadora = Calculadora()
calculadora.ejecutar()

```


2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

```python

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
            # Excepciones para el bloque Except y except Exception para errores inesperados
            except PalabraVaciaException as pve:
                print(f"\nError: {str(pve)}\n")
            except Exception as e:
                print(f"\nError: {str(e)}\n")

checker = PalindromoChecker()
checker.ejecutar()
```

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

```python

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
            # Excepciones para el bloque Except y except Exception para errores inesperados
            except ListaVaciaException as le:
                print(f"\nError: {str(le)}")
            except Exception as e:
                print(f"\nError inesperado: {str(e)}")

primos_checker = Primos()
primos_checker.ejecutar()

```

4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.


```python

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

            # Excepciones para el bloque Except y except Exception para errores inesperados
            except ListaInvalidaException as lie:
                print(f"\nError: {str(lie)}\n")
            # Valor de entrada incorrecto para la operación
            except ValueError:
                print("\nError: Asegúrese de ingresar solo números enteros separados por espacios.\n")
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {str(e)}\n")


programa = MayorSumaConsecutiva()
programa.ejecutar()
```

5.Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.


```python

# Excepciones personalizadas
class ListaDePalabrasVaciaException(Exception):
    """Excepción si la lista de palabras está vacía."""
    pass

class MismosCaracteres:
    def __init__(self):
        pass

    def filtrar_mismos_caracteres(lista):
        grupos = {}  # Diccionario para agrupar palabras
        lista = list(set(lista))  # Elimina duplicados de la lista original

        for palabra in lista:
            clave = ''.join(sorted(palabra.lower()))  # Ordena los caracteres y convierte a minúsculas
            if clave not in grupos:
                grupos[clave] = []
            grupos[clave].append(palabra)

        # Filtra solo los grupos con más de una palabra
        resultado = [item for sublista in grupos.values() if len(sublista) > 1 for item in sublista]
        return resultado

    def ejecutar(self):
        while True:
            try:
                entrada = input("\nIngrese una lista de palabras separadas por espacios: ").strip()
                # Excepción si no hay nada en la entrada
                if not entrada:
                    raise ListaDePalabrasVaciaException("No se ingresó nada")

                lista_palabras = entrada.split()
                # Excepción si no se ingresan palabras separadas por espacios
                if not lista_palabras:
                    raise ListaDePalabrasVaciaException("La lista de palabras está vacía.")

                resultado = self.filtrar_mismos_caracteres(lista_palabras)
                if resultado:
                    print(f"\nLas palabras con los mismos caracteres son: {resultado}\n")
                else:
                    print("\nNo se encontraron palabras con los mismos caracteres.\n")
            # Excepciones para el bloque Except y except Exception para errores inesperados
            except ListaDePalabrasVaciaException as lpe:
                print(f"\nError: {str(lpe)}\n")
            except Exception as e:
                print(f"\nError inesperado: {str(e)}\n")


MismosCaracteres().ejecutar()
```
