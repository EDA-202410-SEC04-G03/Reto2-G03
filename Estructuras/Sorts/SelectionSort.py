import lista as lst

def sort(lista):
    x = lst.pythonificar(lista)
    s = selection_sort(x)
    y = lst.depythonificar(s)
    return y

def selection_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
    return list