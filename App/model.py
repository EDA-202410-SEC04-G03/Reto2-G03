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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
assert cf
import Estructuras.Lista as lst
import Estructuras.Hash_chain as mp
import Estructuras.Sorts.quicksort as qs
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


def req_1(catalog, codPais, exp, n):

    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    jobs = catalog['jobs']
    infol, dic = filtro_r1(jobs, codPais, exp)
    x = lst.sublist(infol, 0, n)

    return x , dic

def filtro_r1(mapa,pais,exp):

    lista = lst.new_list()
    dic = {'pais': pais,
           'npais': 0,
           'exp': 0}

    for i in range(len(mapa['keys'])):
        for j in (mapa['keys'][i]):
            key = j[0]
            value = j[1]
            if value['country_code'] == pais:
                dic['npais'] += 1
                if value['experience_level'] == exp:
                    dic['exp'] += 1
                    lst.crit_add_ordered(lista,value,crit1)
                    
    return lista, dic

def crit1(oferta1, oferta2):
    fecha1=oferta1['published_at']
    fecha2=oferta2['published_at']
    empresa1=oferta1['country_code']
    empresa2=oferta2['country_code']

    if fecha1<fecha2 or (fecha1==fecha2 and empresa1<=empresa2):
        return False
    else: 
        return True

def req_2(catalog, ciudad,emp, n):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    jobs = catalog['jobs']
    infol = filtro_r2(jobs, ciudad,emp)
    size = lst.size(infol)
    x = lst.sublist(infol, 0, n)
    return x, size

def filtro_r2(mapa,ciudad,emp):
    """
    """

    lista_nueva=lst.new_list()

    for i in range(len(mapa['keys'])):
        for j in (mapa['keys'][i]):
            value = j[1]
            if value['city'] == ciudad:
                if value['company_name'] == emp:
                    lst.crit_add_ordered(lista_nueva,value, crit2)
                    
    return (lista_nueva)

def crit2(oferta1, oferta2):
    fecha1=oferta1['published_at']
    fecha2=oferta2['published_at']
    empresa1=oferta1['city']
    empresa2=oferta2['city']

    if fecha1<fecha2 or (fecha1==fecha2 and empresa1<=empresa2):
        return False
    else: 
        return True

def req_3(catalog, empresa, fi, ff):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    jobs = catalog['jobs']
    infol, dic = filtro_r3(jobs, empresa, fi, ff)
    return infol, dic 

def filtro_r3(mapa,empresa,fi, ff):
    """
    retorna un mapa y una lista de las ofertas en un pais segun nivel de experticia.
    """

    lista_nueva=lst.new_list()
    dic = {'mid': 0,
           'senior': 0,
           'junior': 0}

    for i in range(len(mapa['keys'])):
        for j in (mapa['keys'][i]):
        
            key = j[0]
            value = j[1]

            if value['company_name']==empresa: 
                if fi <= value['published_at'] <= ff:
                    lst.crit_add_ordered(lista_nueva,value, crit3)
                    if value['experience_level'] == 'mid':
                        dic['mid'] += 1
                    if value['experience_level'] == 'senior':
                        dic['senior'] += 1
                    if value['experience_level'] == 'junior':
                        dic['junior'] += 1

    return lista_nueva, dic

def crit3(oferta1, oferta2):
    fecha1=oferta1['published_at']
    fecha2=oferta2['published_at']
    empresa1=oferta1['country_code']
    empresa2=oferta2['country_code']

    if fecha1<fecha2 or (fecha1==fecha2 and empresa1<=empresa2):
        return False
    else: 
        return True

def req_4(catalog, code, fi, ff):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    jobs = catalog['jobs']
    dic = filtro_r4(jobs, code, fi, ff)
    return dic

def filtro_r4(mapa, code, fi, ff):
    lista_ofertas = lst.new_list()
    lista_empresas = lst.new_list()
    lista_ciudades = lst.new_list()
    for i in range(len(mapa['keys'])):
        for j in(mapa['keys'][i]):
            key = j[0]
            value = j[1]

            if value['country_code'] == code:
                if fi <= value['published_at'] <= ff:
                    lista_ofertas = lst.addlast(lista_ofertas, value)

            if value['country_code'] == code:
                if fi <= value['published_at'] <= ff:
                    if lst.is_present(lista_empresas, value['company_name']) == False:
                        lista_empresas = lst.addlast(lista_empresas, value)

            if value['country_code'] == code:
                if fi <= value['published_at'] <= ff:
                    if lst.is_present(lista_ciudades, value['city']) == False:
                        lista_ciudades = lst.addlast(lista_ciudades, value)

    total_ofertas = lst.size(lista_ofertas)
    total_empresas = lst.size(lista_empresas)
    total_ciudades = lst.size(lista_ciudades)

    response = {
        "TOTAL_OFERTAS": total_ofertas,
        "TOTAL_EMPRESAS": total_empresas,
        "TOTAL_CIUDADES": total_ciudades
    }

    return response

def req_5(jobs,ciudad,fecha1,fecha2):
    """
    Función que soluciona el requerimiento 5
    """
    (mapa_ofertas,lista_ofertas)=filtro_r5(jobs['jobs'],ciudad,fecha1,fecha2)
    num_ofertas=mapa_ofertas['load']

    (mapa_empresas,lista_empresas)=empresas_r5(mapa_ofertas)
    (mejor_empresa,peor_empresa,num_ofertas_max,num_ofertas_min)=empresas_extremales_r5(mapa_empresas,lista_empresas)
    num_empresas=lista_empresas['size']

    dic={
        'num_ofertas':num_ofertas,
        'num_empresas':num_empresas,
        'mejor_empresa':mejor_empresa,
        'max_ofertas':num_ofertas_max,
        'peor_empresa':peor_empresa,
        'min_ofertas':num_ofertas_min
        }

    return (dic,lista_ofertas)

def filtro_r5(mapa,ciudad,fecha1,fecha2):
    """
    Da un mapa y una lista de las ofertas en la ciudad entre ambas fechas.
    """

    mapa_nuevo=mp.new_map(int(mapa['capacity']//500)+1) 
    lista_nueva=lst.new_list()

    for i in range(len(mapa['keys'])):
        for j in (mapa['keys'][i]):
            key = j[0]
            value = j[1]

            if value['city']==ciudad: 
                if (fecha1 <= value['published_at']) and (value['published_at'] <= fecha2):
                    mapa_nuevo=mp.put(mapa_nuevo,value,key)
                    lst.crit_add_ordered(lista_nueva,value,crit_r5)

    return (mapa_nuevo,lista_nueva)

def empresas_r5(mapa):
    """
    A partir del mapa filtrado, crea una lista con las empresas relevantes y un mapa que a cada empresa asigna el numero de ofertas. 
    """
    mapa_emp=mp.new_map(int(mapa['capacity']//5)+1) #TODO: Cambiar 5 por el numero promedio de ofertas en algun ejemplo
    lista_emp=lst.new_list()

    for i in range(len(mapa['keys'])):
        for j in range(len(mapa['keys'][i])):
            key=mapa['keys'][i][j][0]
            value=mapa['keys'][i][j][1]
            empresa=value['company_name']

            if not mp.contains(mapa_emp,empresa):
                num_ofertas=1
                mapa_emp=mp.put(mapa_emp,num_ofertas,empresa)
                lista_emp=lst.addlast(lista_emp,empresa)
            else:
                for k in range(len(mapa_emp['keys'][mp.hash_fun(mapa_emp, empresa)])):
                    value = mapa_emp['keys'][mp.hash_fun(mapa_emp, empresa)][k]
                    llave = value[0]
                    num = value[1]
                    if llave == empresa:
                        mapa_emp['keys'][mp.hash_fun(mapa_emp, empresa)][k] = (llave, num+1)                        

    return (mapa_emp,lista_emp)
        
def empresas_extremales_r5(mapa,lista):
    '''
    A partir del mapa y la lista anterior, retorna la empresa con más ofertas laborales y la empresa con menos ofertas laborales, 
    junto con el número de ofertas que cada una ofrece.
    Si hay dos empresas con la cantidad maximal, devuelve la primera en salir.
    Si hay dos empresas con la cantidad minimal, devuelve la primera en salir.
    '''
    it = lst.iterator(lista)
    empresa=it['value']

    mejor_empresa=empresa
    peor_empresa=empresa
    num = mp.getvalue(mapa, empresa) 
    num_ofertas_max=num
    num_ofertas_min=num

    while lst.hasNext(it):
        it=lst.Next(it)
        empresa=it['value']
        num_ofertas=mp.getvalue(mapa, empresa)

        if num_ofertas>num_ofertas_max:
            num_ofertas_max=num_ofertas
            mejor_empresa=empresa

        if num_ofertas<num_ofertas_min:
            num_ofertas_min=num_ofertas
            peor_empresa=empresa

    return (mejor_empresa,peor_empresa,num_ofertas_max,num_ofertas_min)

def crit_r5(oferta1,oferta2):
    '''
    Es el criterio de comparación para dos ofertas. Retorna True si la primera debería ir antes o en la misma posición que la segunda y False de lo contrario.
    '''
    fecha1=oferta1['published_at']
    fecha2=oferta2['published_at']
    empresa1=oferta1['company_name'].lower()
    empresa2=oferta2['company_name'].lower()

    if fecha1<fecha2 or (fecha1==fecha2 and empresa1<=empresa2):
        return True
    else: 
        return False


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


def isremoto(lt):
    if lt == 'remoto':
        return True
    else:
        return False

def printlt(lista):
    x = []
    size = lst.size(lista)
    if size >= 10:
        return sub5(lista, size)
    else:
        node = lista['head']
        i = 0
        while i < size: 
            x.append(node['value'])
            node = node['next']
            i += 1
        return x

def sub5(lista, size):
    s1 = lst.sublist(lista, 0, 5)
    s2 = lst.sublist(lista, size-5, 5)
    orde1 = []
    orde2 = []
    node = s1['head']
    i = 0
    while i < 5:
        orde1.append(node['value'])
        node = node['next']
        i += 1
    node = s2['head']
    j = 0
    while j < 5:
        orde2.append(node['value'])
        node = node['next']
        j += 1
    return orde2, orde1
    
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

def sortcritr1(v1, v2):
    if (v1['published_at'] < v2['published_at']):
        return True
    elif  ((v1['published_at'] == v2['published_at']) and (v1['country_code'] < v2['country_code'])):
        return True
    else: 
        return False