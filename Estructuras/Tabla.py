#Linear Probing

def new_map(M):
    return {'capacity': M, 'load': 0, 'keys': [None] * M, 'size': 0}

def put(ht, key, value):
    if ht['load'] *  2 >= ht['capacity']:
        ht = resize
    pos = ht_hash(ht, key)
    while ht['keys'][pos] != None:
        pos = (pos + 1) % ht['capacity']
    ht['keys'][pos] = (key, value)
    ht['load'] += 1
    ht['size'] += 1
    return ht

def resize(ht):
    new = new_map(2 * ht['capacity'] + 1)
    for elem in len(ht['keys']):
        if elem != None:
            put(new, elem[0], elem[1])
    return new

def get(ht, key):
    pos = ht_hash(ht, key)
    while ht['keys'][pos] != None:
        k = ht['keys'][pos]
        if k[0] == key:
            return k
        pos +=1
    return None

def get_key(ht, key):
    pos = ht_hash(ht, key)
    while ht['keys'][pos] != None:
        k = ht['keys'][pos]
        if k[0] == key:
            return k[0]
        pos +=1
    return None
    

def get_value(ht, key):
    pos = ht_hash(ht, key)
    while ht['keys'][pos] != None:
        k, v = ht['keys'][pos]
        if k == key:
            return v
        pos +=1
    return None

def contains(ht, key):
    pos = ht_hash(ht, key)
    while ht['keys'][pos] != None:
        k, v = ht['keys'][pos]
        if k == key:
            return True
        pos +=1
    return False

def remove(ht, key):
    pos = ht_hash(ht, key)
    while ht['keys'][pos] != None:
        k, v = ht['keys'][pos]
        if k == key:
            ht['keys'][pos] = None
        pos +=1
    return None

def ht_hash(ht, elem):
    return hash(elem) % ht['size']

def hashfun(key):
    return hash(key)

def size(ht):
    return ht['size']
    