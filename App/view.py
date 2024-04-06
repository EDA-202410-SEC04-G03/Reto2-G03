﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import threading
assert cf
from tabulate import tabulate
import Estructuras.Lista as lst
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")

def print_tabla(data):
    """
        Función que imprime un dato dado su ID
    """
    tabla = tabulate(data, tablefmt="pretty", headers="keys", missingval= 'Unkwnown', 
                     colalign=("left", "left", "right", "left"))
    print(tabla)
    print()

def load_data(control, mem):
    """N
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control, mem)

def tload(lista):
    orde2, orde1 = controller.sub3(lista)
    lt = []
    for i in orde2:
        dic ={
            'Fecha': i['published_at'], 'Titulo': i['title'],
            'Empresa': i['company_name'], 'Experiencia': i['experience_level'],
            'Pais': i['country_code'], 'Ciudad': i['city'] 
        }
        lt.append(dic)
    for i in orde1:
        dic ={
            'Fecha': i['published_at'], 'Titulo': i['title'],
            'Empresa': i['company_name'], 'Experiencia': i['experience_level'],
            'Pais': i['country_code'], 'Ciudad': i['city'] 
        }
        lt.append(dic)
    return lt

def print_load(control):
    
    jobs = control['model']['jobsLT']
    print()
    print('----- Primeras y ultimas 3 ofertas de trabajo -----')
    x = tload(jobs)
    print_tabla(x)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False
    
def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")


# Se crea el controlador asociado a la vista
control = new_controller()

# set el limite de recursion
default_limit = 1000


# main del reto
def menu_cycle():
    """
    Menu principal
    """
    working = True
    
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            answer = load_data(control, mem)
            print('se cargaron {} ofertas de trabajos.'.format(controller.jobsltsize(control)))
            print_load(control)
            printLoadDataAnswer(answer)
            
        elif int(inputs) == 2:
            pais = str(input("Ingrese el codigo del pais: "))
            exp = str(input("Ingrese el nivel de experiencia (junior, mid, o senior): "))
            n = int(input("Ingresa la cantidad de trabajos a consultar: "))
            print_req_1(control, pais, exp, n)

        elif int(inputs) == 3:
            city = str(input("Ingrese la ciudad de consulta: "))
            emp = str(input("Ingrese el nombre de la empresa: "))
            n = int(input("Ingresa la cantidad de trabajos a consultar: "))
            print_req_2(control, city, emp, n)

        elif int(inputs) == 4:
            empresa = str(input("Ingrese el nombre de la empresa: "))
            fi = str(input("Ingrese la fecha inicial de consulta (Y-M-D): "))
            ff = str(input("Ingresa la fecha final de consulta (Y-M-D): "))
            print_req_3(control, empresa, fi, ff)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            exp = str(input("Ingrese el nombre de la empresa: "))
            fi = str(input("fecha inicial: "))
            ff = str(input("fecha final: "))
            pais = str(input("pais: "))
            n = str(input("n: "))
            print_req_6(control, exp, fi, ff, pais, n)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

if __name__ == "__main__":
    
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()
   # menu_cycle()