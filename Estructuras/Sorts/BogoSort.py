import random
import lista as lst

def sort(lista):
    x = lst.pythonificar(lista)
    s = bogo_sort(x)
    y = lst.depythonificar(s)
    return y

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def is_sorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
