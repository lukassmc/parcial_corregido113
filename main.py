from random import *
from csv import *
from funciones import *     
from funciones_menu import *

bandera_carga_csv= False
bandera_carga_tiempos= False
bandera_ordenar_lista = False

lista_bicicletas= []
while True:
    
    match menu_bicicletas():
        
        case "a":
            try:
                nombre_archivo= input('Ingrese el nombre del archivo a crear:')
                cargar_csv(lista_bicicletas, nombre_archivo)
                bandera_carga_csv= True
            except:
                print('Ingrese un nombre de archivo valido:')
                
        case "b":
            if bandera_carga_csv == False:
                print("Primero debes cargar el archivo para imprimir la lista.")
            else:
                printear_listas(lista_bicicletas)
        case "c":
            
            if bandera_carga_csv == False:
                print("Primero debes cargar el archivo para cargar los tiempos.")
            else:
                cargar_tiempos_random(lista_bicicletas)
                bandera_carga_tiempos = True
                
        case "d":
                
            if bandera_carga_csv == False:
                print("Primero debes cargar el archivo para cargar los tiempos.")
            elif bandera_carga_tiempos == False:
                print("Primero debes cargar los tiempos para saber el ganador.")
            else:
                print(bici_mas_rapida(lista_bicicletas))
        
        case "e":
            if bandera_carga_csv == False:
                print("Primero debes cargar el archivo filtrar una lista.")
            else:
    
                crear_archivo_tipo(lista_bicicletas)
                print('Archivo creado con exito!')
        case "f":
            if bandera_carga_csv == False:
                print('Primero debes cargar el archivo para mostrar los promedios.')
            elif bandera_carga_tiempos == False:
                print('Para mostrar el promedio de tiempos, tienes que cargar los tiempos primero.')
            else:
                promedio_por_tipo(lista_bicicletas)
        case "g":
            if bandera_carga_csv == False:
                print('Primero debes cargar el archivo para ordenar la lista.')
            elif bandera_carga_tiempos == False:
                print('Para ordenar por tiempos, tienes que cargar los tiempos primero.')
            else:
                printear_listas(ordenar_lista_doble_criterio_ascendente(lista_bicicletas,'tipo' , 'tiempo'))
                bandera_ordenar_lista= True
        case 'h':
            if bandera_ordenar_lista == False:
                print('Para cargar un Json con las posiciones, primero debes ordenar la lista.')
            else:
                escritor_json('bicicletas.json', lista_bicicletas)
                print("Cargado a JSON con exito!")
        
        case "i":
            
            if confirmar_salida("Desea salir?\n "):
                break
            else:
                continue
        
    pausar() 