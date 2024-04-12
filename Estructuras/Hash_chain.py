
factor=4


def new_map(M):
    M = next_prime(M)
    keys=[]
    for i in range(M):
        l=[]
        keys.append(l)
    return {'capacity':M, 'load':0, 'keys':keys}

def is_empty(map):
    if map['load']==0:
        return True
    else:
        return False

def hash_fun(map,key):
    
    if type(key) == int:
        n = key
    else:
        
        i = 0
        n = 0
        x = {}
        for l in 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789':
            x[l] = i
            i += 1
        for l in str(key):
            if l in 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789':
                n += x[l]

    return int(n)%(int(map['capacity'])) 
    
def size(map):
    return map['load']

def getvalue(map, key):
    for i in map['keys'][hash_fun(map, key)]:
        if i[0] == key:
            return i[1]
    return None


def next_prime(n):
    ###
    #Recibe un número entero IMPAR y devuelve el menor primo mayor a n.
    ###
    if n%2==0:
        n=n+1
    p=n
    primo=False
    while primo==False:
        p=p+2
        primo=True
        for i in range(3,int(p**(1/2))+1):
            if p%i==0:
              primo=False
    return p
                
def rehash(map):
    nmap=new_map(next_prime(2*map['capacity']-1))
    for i in range(len(map['keys'])):
        for j in range(len(map['keys'][i])):
            elem = map['keys'][i][j]
            nmap=put(nmap,elem[1],elem[0])
    return nmap
    

def put(map, value, key):
    if size(map)>map['capacity']*factor:
        map=rehash(map)
    map['keys'][hash_fun(map,key)].append((key,value))
    map['load']=map['load']+1
    return map
     

def contains(map, key):
    esta=False
    pos=hash_fun(map,key)
    for element in map['keys'][pos]:
        if element[0]==key:
            esta=True
    return esta

def remove_key(map,key):
    i=0
    pos=hash_fun(map,key)
    for element in map['keys'][pos]:
        if element[0]==key:
            map['keys'][pos].remove(element)
            i=i+1
    map['load']=map['load']-i
    return map

