"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import time
import tracemalloc
from datetime import datetime as dt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    
    control = {'model': None}
    control['model'] = model.new_data_structs()
    return control

# Funciones para la carga de datos


def load_data(control, memflag=True):
    """
    Carga los datos del reto
    """
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    structure = control['model']
    loadjobs(structure)
    loadskills(structure)
    loademployment(structure)
    loadmultilocation(structure)
    
    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return delta_time, delta_memory

    else:
        return delta_time

def loadjobs(structure):
    
    file = cf.data_dir + 'Challenge-2/data/small-jobs.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=';')
    for i in input_file:
        i['published_at'] = dt.strptime(i['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ') 
        model.addjobs(structure, i)
        model.addjobsLT(structure, i)
def loadskills(structure):
    
    file = cf.data_dir + 'Challenge-2/data/small-skills.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=';')
    for i in input_file:
        model.addid(structure, i)

def loademployment(structure):
    
    file = cf.data_dir + 'Challenge-2/data/small-employments_types.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=';')
    for i in input_file:
        model.addid(structure, i)

def loadmultilocation(structure):
    
    file = cf.data_dir + 'Challenge-2/data/small-multilocations.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), delimiter=';')
    for i in input_file:
        model.addid(structure, i)

# Funciones de size

def jobsltsize(control):
    structure = control['model']
    return model.jobsltsize(structure)

def sub3(lista):
    orde2, orde1 = model.sub3(lista)
    return orde2, orde1


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
