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
            # Excepciones para el bloque Except
            except ListaDePalabrasVaciaException as lpe:
                print(f"\nError: {str(lpe)}\n")
            except Exception as e:
                print(f"\nError inesperado: {str(e)}\n")


MismosCaracteres().ejecutar()