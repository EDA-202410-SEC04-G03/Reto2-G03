﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
assert cf
import Estructuras.Lista as lst
import Estructuras.Hash_chain as mp
from datetime import datetime as dt

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    structure = {'jobsLT': None,
                  'jobs': None,
                  'ID': None}
    
    structure['jobsLT'] = lst.new_list()
    structure['jobs'] = mp.new_map(114710)
    structure['ID'] = mp.new_map(114710)
    
    
    return structure


# Funciones para agregar informacion al modelo

def addjobsLT(struct, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    lst.addlast(struct['jobsLT'], job)
    return struct

def addjobs(struct, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    mp.put(struct['jobs'], job, job['published_at'])
    return struct

def addid(struct, id):
    """
    Función para agregar nuevos elementos a la lista
    """
    
    mp.put(struct['ID'], id, id['id'])
    return struct


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def jobsltsize(struct):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lst.size(struct['jobsLT'])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(jobs, code, fecha1, fecha2):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    (mapa_ofertas,lista_ofertas)=filtro_r4(jobs,code,fecha1,fecha2)
    lista_ofertas_ordenada=sort_r4(lista_ofertas)
    num_ofertas=mapa_ofertas['load']

    dic={
        'num_ofertas':num_ofertas,
        'lista_ofertas_ordenada':lista_ofertas_ordenada
        }

    return dic

def filtro_r4(mapa,code,fecha1,fecha2):
    """
    Retorna un mapa y una lista de las ofertas.
    """
    fecha1=dt.strptime(fecha1, '%Y-%m-%dT%H:%M:%S.%fZ')
    fecha2=dt.strptime(fecha2, '%Y-%m-%dT%H:%M:%S.%fZ')

    mapa_nuevo=mp.new_map(int(mapa['capacity']//50)+1)
    lista_nueva=lst.new_list()

    for i in range(len(mapa['keys'])):
        for j in len(mapa['keys'][i]):
            key=mapa['keys'][i][j][0]
            value=mapa['keys'][i][j][1]

            if value['country_code']==code and value['published_at']>=fecha1 and value['published_at']<=fecha2:
                mapa_nuevo=mp.put(map,value,key)
                lista_nueva=lst.addlast(lista_nueva,value)

    return (mapa_nuevo,lista_nueva)

def crit_r4(oferta1,oferta2):
    '''
    Compara dos ofertas.
    '''
    fecha1=oferta1['published_at']
    fecha2=oferta2['published_at']
    empresa1=oferta1['company_name'].lower()
    empresa2=oferta2['company_name'].lower()

    if fecha1<fecha2 or (fecha1==fecha2 and empresa1<=empresa2):
        return True
    else: 
        return False

def sort_r4(lista_ofertas):
    '''
    Ordena la lista de ofertas por quicksort.
    '''
    return qs.csort(lista_ofertas,crit_r4)


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sub3(lista):
    size = lst.size(lista)
    s1 = lst.sublist(lista, 0, 3)
    s2 = lst.sublist(lista, size-3, 3)
    orde1 = []
    orde2 = []
    node = s1['head']
    for i in s1:
        orde1.append(node['value'])
        node = node['next']
    node = s2['head']
    for i in s2:
        orde2.append(node['value'])
        node = node['next']
    return orde2, orde1
