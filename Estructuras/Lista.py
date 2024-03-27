#head = {'value': None, 'next': None} 
#last = head
#size = 0

#O(1)

def new_list():
    """
    crea una nueva lista
    """
    return {'head': None, 'last': None, 'size': 0}

def is_empty(lista):
    """"
    verifica si las lista esta vacia
    """
    if lista['size'] == 0:
        return True
    else:
        return False

def is_present(lista, element):
    """"
    verifica si la lista tiene un valor dado
    """
    if is_empty(lista) == True:
        return False
    else:
        if search(lista, element) == (False or None) :
            return False
        else:
            return True
        

def addlast(lista, new_elem):
    """
    adds an element at the end of the list
    """
    node = {'value': new_elem, 'next': None}
    if is_empty(lista):
        lista['head'] = node
        lista['last'] = node
        lista['size'] = 1
    else:
        lista['last']['next'] = node
        lista['last'] = node
        lista['size'] = lista['size']+1
    return lista

def addfirst(lista, new_elem):
    """
    adds an element at the start of the list
    """
    
    if is_empty(lista):
        node = {'value': new_elem, 'next': None}
        lista['head'] = node
        lista['last'] = node
        lista['size'] = 1
    else:
        node = {'value': new_elem, 'next': lista['head']}
        lista['head'] = node
        lista['size'] = lista['size']+1
        
    return lista    
    
def iterator(lista):
    """
    nadie sabe pa q es :p
    """
    return lista['head']
    
def hasNext(it):
    """
    Dice si un iterador esta en el ultimo nodo
    """
    if it['next'] == None:
        return False
    else:
        return True
    
def Next(it):
    
    return it['next']

def size(lista):
    """
    retorna el tamaño de una lista
    """
    return lista['size']
    
def get_first(lista):
    return get_element(lista, 0)    

def get_element(lista, pos):
    """
    retorna un elemento en una posicion dada
    Las posiciones empiezan desde 0 hasta size(lista) - 1
    """
    if size(lista) <= pos:
        return None
    else: 
        it = iterator(lista)
        i = 0
        while i < pos:
            it = Next(it)
            i = i + 1
        return it['value']
        
def sublist(lista, pos, no):  
    """
    retorna una lista nueva a partir de una posicion base dada y una cantidad establecida. 
    Las posiciones empiezan desde 0 hasta size(lista) - 1
    El largo de la sublista va a ser no
    """
    if size(lista) < pos + no:
        return None
     
    else: 
        nlista=new_list()
        it = iterator(lista)
        i = 0
        while i < pos + no:
            if i >= pos:
                addlast(nlista,it['value'])
            it = Next(it)
            i = i + 1
        return nlista
               
    
#O(n)
def delete(value):
    """
    Remove the first instance of the given element from 
    the list
    """
    pass

#O(n)
def search(lista, element):
    """
    Returna la posicion en la que se encuentra un elemento
    """
    i = 0
    if is_empty(lista):
        return None  
    else:
        esta = False
        it = iterator(lista)
        while hasNext(it) and esta == False:
            if it['value'] == element:
                esta = True
                return i
            i = i +1
            it = Next(it)
        if esta == False:
            return None
        
def append(l1,l2):
    l1["last"]["next"] = l2["head"]
    l1["size"] += l2["size"]
    l1["last"] = l2["last"]
    return l1

def suma(it, num):
    num=num+it['value']
    if hasNext(it):
        suma(next(it),num)
        num=num+it['value']
    else:
        return num

def promedio(lista):
    n=lista['size']
    it=iterator(lista)
    suma=it['value']
    while hasNext(it):
        it=next(it)
        suma=suma+it['value']
    return suma/n

def add_crit(lista,val):
    if True:
        lista = addlast(lista,val)
    return list

def crit(val):
    bool=False
    if val>5:
        bool=True
    return bool

def filtro(lista):
    it=iterator(lista)
    nlista=new_list()
    add_crit(nlista,it['value'])
    while hasNext(it):
        it=next(it)
        add_crit(nlista,it['value'])
    return

def llenar(it,nlista):
    add_crit(nlista,it['value'])
    if hasNext(it):
        llenar(next(it),nlista)
    else:
        return nlista

def pythonificar(lista):
    l=[]
    if is_empty(lista) == False:
        it=iterator(lista)
        l.append(it['value'])
        while hasNext(it):
            it = Next(it)
            l.append(it['value'])
    return l

def depythonificar(l):
    lista = new_list()
    for element in l:
        lista = addlast(lista,element)
    return lista
        