#Complejidad: O(n^2)
import lista as lst

def sort(lista):
    x = lst.pythonificar(lista)
    s = insertion_sort(x)
    y = lst.depythonificar(s)
    return y

def insertion_sort(list):
    for i in range(len(list)):
        for j in range(i-1, -1, -1):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                i-=1
    return list