from funciones import *
from os import system


def pausar()-> None:
    system("pause")

def limpiar_terminal()-> None:
    
    system("cls")

def menu_bicicletas()-> str:
    """Menu de opciones para obtener datos.

    Returns:
        str: Devuelve el dato de la opción elegida. 
    """
    limpiar_terminal()
    print("     Menu de opciones")
    print("A- Cargar archivos .CSV .")
    print("B- Mostrar lista de bicicletas.")
    print("C- Asignar tiempos .")
    print("D- Informar ganador")
    print("E- Filtrar por tipo de bicicleta")
    print("F- Mostrar promedio de tiempo por tipo de bicileta")
    print("G- Mostrar posiciones por tipo y tiempo.")
    print("H- Guardar posiciones en JSON")
    print("I- Salir")
    
    return obtener_opcion("Ingrese una opcion:  ").lower()


def confirmar_salida(mensaje: str)-> bool:
    """Le pregunta al usuario si desea salir o no.

    Args:
        mensaje (str): Mensaje para preguntar si desea salir

    Returns:
        bool: Devuelve True si la opción es "Si"
    """
    respuesta= input(mensaje).lower()
    
    return respuesta == "si"



def es_texto(entrada:str)-> bool:
    """Verifica si es str

    Args:
        entrada (str): Valor de entrada

    Returns:
        bool: devuelve true si es str
    """
    return isinstance(entrada, str)



def obtener_opcion(mensaje: str)-> str:
    """Valida que la opción ingresada esté dentro de las opciones validas.

    Args:
        mensaje (str): mensaje para pedir el dato

    Returns:
        str : deuelve la opcion ingresada. 
    """
    
    lista_opciones= ["a","b","c","d","e","f","g","h","i","j"]
    
    while True:
        
        entrada = input(mensaje)
        if entrada in lista_opciones:
            
            return entrada
        else:
            print("Entrada inválida. Por favor, ingrese una opción válida.")
            

            
