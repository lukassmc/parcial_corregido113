import random 
import json
import re



def generar_random(min:int, max:int)-> tuple:
    """genera un número entero aleatorio entre min y max.
    
    Args:
        min (int): valor minimo.
        max (int): valor maximo.
    
    Returns:
        tuple: tupla de numeros aleatorios generados.
    """
    tupla = random.randint(min, max)
    return tupla

def validar_lista(lista:list)-> None:
    """valida si la lista ingresada es una lista no vacía.
    
    Args:
        lista (list): Lista a validar.
    
    Raises:
        ValueError: Si la lista ingresada no es una lista o está vacía.
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")

def getpathactual(nombre_archivo)-> str:
    """obtiene la ruta completa del archivo en el directorio actual
    
    Args:
        nombre_archivo (str): nombre del archivo
    
    Returns:
        str: ruta completa del archivo
    """
    
    import os
    
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def printear_listas(lista:list)-> None:
    """funcion para mostrar de forma pareja los datos del archivo de bicicletas

    Args:
        lista (list): lista con los datos del archivo de biciletas
    """
    validar_lista(lista)

    print("                      LISTA DE CICLISTAS")
    print("ID     Nombre            Tipo        Tiempo")
    print("------------------------------------------------------------------------")
    for bici in lista:
        print(f"{bici["id_bike"]}    {bici["nombre"]:15}    {bici["tipo"]:10}    {bici["tiempo"]}")
   

def filtrar_lista(filtro, lista: list) -> list:
    """filtra una lista según un el filtro ingresado
    
    Args:
        filtro (function): Función de filtro
        lista (list): Lista a filtrar
    
    Returns:
        list: Lista filtrada
    """

    lista_retorno = []
    
    for el in lista:
        if filtro(el):
            lista_retorno.append(el)    
            
    return lista_retorno

def mapear_campo(campo, lista: list) -> list:
    """aplica una funcio a cada elemento de la lista
    
    Args:
        campo (function): funcion a aplicar
        lista (list): lista de entrada
    
    Returns:
        list: Lista con los resultados de aplicar la funcion
    """
    validar_lista(lista)
    lista_retorno = []
    for el in lista :
        lista_retorno.append(campo(el))
    return lista_retorno

def mapear_campo_doble_criterio(campo1, campo2 ,lista: list) -> list:
    """aplica dos funciones a cada elemento de una lista
    
    Args:
        campo1 (function): primera función a aplicar
        campo2 (function): segunda función a aplicar
        lista (list): lista a mapear
    
    Returns:
        list: lista con los resultados de aplicar las funciones
    """
    
    validar_lista(lista)
    lista_retorno = []
    for el in lista :
        lista_retorno.append(campo1(el))
        lista_retorno.append(campo2(el))
        
    return lista_retorno

def swap_lista(lista:list, i: int, j: int)-> None:
    """intercambia dos elementos en una lista
    
    Args:
        lista (list): Lista de entrada
        i (int): indice del primer elemento
        j (int): indice del segundo elemento
    """
    validar_lista(lista)
    aux= lista[i]
    lista[i]= lista[j]
    lista[j]= aux

def ordenar_lista_doble_criterio_ascendente(lista: list, campo1, campo2):
    """ordena una lista de diccionarios segun dos campos de manera sacendente
    
    Args:
        lista (list): lista de diccionarios a ordenar
        campo1 (str): primer campo de ordenación
        campo2 (str): segundo campo de ordenación
    
    Returns:
        list: lista ordenada
    """
    validar_lista(lista)
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            
            if lista[i][campo1] == lista[j][campo1]:
                
                if lista[i][campo2] > lista[j][campo2]:
                    
                    swap_lista(lista, i, j)
                    
            elif lista[i][campo1] > lista[j][campo1]:
                
                swap_lista(lista, i, j)
    
    return lista

def totalizar_lista(lista: list)-> int:
    """suma todos los elementos de una lista

    Args:
        lista (list): lista a totalizar

    Returns:
        int: valor de la suma total de la lista
    """
    validar_lista(lista)

    total= 0
    for el in lista:
      total += el
      
    return total                

   
def calcular_promedio_lista(lista: list)-> float:
   """calcula el promedio de los elementos de una lista
    
    Args:
        lista (list): lista de numeros
    
    Returns:
        float: promedio de los elementos de la lista de numeros
    
    Raises:
        ValueError: si la lista esta vacia o el argumento no es una lista
    """
   
   if isinstance (lista, list):
      cant= len(lista)
      if cant == 0:
         raise ValueError("El promedio de una lista no puede ser definido.")
      promedio= totalizar_lista(lista) / cant
   
      return promedio 
      
   raise ValueError("Esto no es una lista")     


def escritor_json(path: str, lista: list):
    """escribe una lista en un archivo JSON
    
    Args:
        path (str): Ruta del archivo
        lista (list): Lista a escribir
    """
    validar_lista(lista)
    
    with open(path, "w") as archivo:
        json.dump(lista, archivo, indent=4)
    
    print("Archivo creado correctamente!")








"------------------------------------------------- Lectura de CSV --------------------------------------------"

csv= "bicicletas.csv"
lista_bicicletas= []
def cargar_csv(lista: list, nombre_archivo: str)-> list:
    """Carga una lista vacia con los datos del csv

    Args:
        lista (list): lista a cargar
        nombre_archio (str): nombre del archivo 

    Returns:
        list: lista con la informacion cargada
    """
   
    with open(getpathactual(nombre_archivo + ".csv"), "r", encoding= "utf-8") as archivo:
        for linea in archivo:
            diccionario={}
            split= re.split(",|\n", linea)
            
            diccionario["id_bike"] = split[0]
            diccionario["nombre"] = split[1]
            diccionario["tipo"] = split[2]
            diccionario["tiempo"] = split[3]
            lista.append(diccionario)
    
    print("Lista cargada correctamente!")   
    return lista


"------------------------------------------------- Cargar tiempos random --------------------------------------------"

def cargar_tiempos_random(lista: list)-> None:
    """Se mapea el campo de tiempo, y se le cargan tiempos aleatorios entre 50 y 120.

    Args:
        lista (list): lista a mapear
    """
    validar_lista(lista)
    
    lista_tiempo= mapear_campo(lambda tiempo : tiempo["tiempo"] , lista)
    
    for  bici in range(len(lista_tiempo)):
        valor_de_tiempo= generar_random(50, 120)
        lista_tiempo[bici]= lista[bici]["tiempo"]= valor_de_tiempo
    
    print("Tiempos random cargados con exito!")
         

    
"------------------------------------------------- Bici mas rapida --------------------------------------------"

def bici_mas_rapida(lista: list)-> None:
    """Esta funcion recorre la lista de bicicletas, comparando sus tiempos, y guarda en variables las mas rapidas.

    Args:
        lista (list): lista a recorrer
    """
    
    nombre_menor_tiempo = ""
    bandera_mas_rapida= False
    bandera_empate= False
    menor_tiempo= lista[0]
    for bici in lista:
    
        if bici["tiempo"] == menor_tiempo:
            menor_tiempo_empate= bici["tiempo"]
            nombre_tiempo_empate = bici["nombre"]
            bandera_empate = True     
            
        if bandera_mas_rapida == False or bici["tiempo"] < menor_tiempo:
           
            menor_tiempo= bici["tiempo"]
            nombre_menor_tiempo = bici["nombre"]
            bandera_mas_rapida= True
        
        
    if bandera_empate == True:
        ganadores= { "menor tiempo": menor_tiempo,
                    "nombre": nombre_menor_tiempo,                    
                    "empato": menor_tiempo_empate,
                    "nombre_empate": nombre_tiempo_empate
        }
    else:
        ganadores= { "menor tiempo": menor_tiempo,
                    "nombre": nombre_menor_tiempo
            
        }
             
    return ganadores


"------------------------------------------------- Archivo tipo bicicletas --------------------------------------------"

def crear_archivo_tipo(lista:list)->None:
    """ se le pide al usuario un tipo de bicicletas, y se filtra la lista ingresada segun el tipo ingresado, para crear un archivo con esta informacion

        lista (list): lista con datos para crear archivo
    """


    tipe_bike = input("Ingrese el tipo de bicicleta ").upper()
    lista_tipo = (filtrar_lista(lambda bike: bike["tipo"] == tipe_bike, lista))


    while tipe_bike != "BMX" and tipe_bike != "MTB" and tipe_bike != "PLAYERA" and tipe_bike != "PASEO":
        tipe_bike = input("Ingrese un tipo de bicicleta valido: ").upper()
   
   
   
    with open(getpathactual(tipe_bike + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_tipo)):
            l = ",".join(lista_tipo[i]) + "\n"

        for persona in lista_tipo:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)
    
   




"------------------------------------------------- Promedio por tipo --------------------------------------------"

def promedio_por_tipo(lista:list)-> None:
    """calcula y muestra el promedio de tiempo por tipo de bicicleta
    
    Args:
        lista (list): lista de bicicletas
    """
    lista_tipos= list(set(mapear_campo(lambda tipos_bicicleta: tipos_bicicleta['tipo'], filtrar_lista(lambda bici: bici['tipo'] != 'tipo', lista))))
    
    for tipo_de_bici in lista_tipos:
        
        corredores_por_tipo= filtrar_lista(lambda tipo: tipo["tipo"], filtrar_lista(lambda tipos: tipos['tipo'] == tipo_de_bici, lista))
        tiempo= mapear_campo(lambda tiempo: tiempo['tiempo'], corredores_por_tipo)
        
        promedio= calcular_promedio_lista(tiempo)
        print(f"El promedio de tiempo del tipo {tipo_de_bici} es: {round(promedio), 2} minutos")
    


"------------------------------------------------- Ordenar --------------------------------------------"

def ordenar_lista_doble_criterio_ascendente(lista: list, campo1, campo2):
    """ordena una lista de diccionarios segun dos campos de manera sacendente
    
    Args:
        lista (list): lista de diccionarios a ordenar
        campo1 (str): primer campo de ordenación
        campo2 (str): segundo campo de ordenación
    
    Returns:
        list: lista ordenada
    """
    validar_lista(lista)
    tam = len(lista)
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            
            if lista[i][campo1] == lista[j][campo1]:
                
                if lista[i][campo2] > lista[j][campo2]:
                    
                    swap_lista(lista, i, j)
                    
            elif lista[i][campo1] > lista[j][campo1]:
                
                swap_lista(lista, i, j)
    
    return lista



"------------------------------------------------- * --------------------------------------------"









