import lista as lst
import InsertionSort as ins

def sort(lista):
    x = lst.pythonificar(lista)
    s = bucket_sort(x)
    y = lst.depythonificar(s)
    return y


def bucket_sort(lista):
    
    max_value = max(lista)
    size = max_value/len(lista)

    buckets_list= []
    for x in range(len(lista)):
        buckets_list.append([]) 
    for i in range(len(lista)):
        j = int (lista[i] / size)
        if j != len (lista):
            buckets_list[j].append(lista[i])
        else:
            buckets_list[len(lista) - 1].append(lista[i])
    for z in range(len(lista)):
        ins.insertion_sort(buckets_list[z])
        
    lfinal = []
    for x in range(len (lista)):
        lfinal = lfinal + buckets_list[x]
    return lfinal