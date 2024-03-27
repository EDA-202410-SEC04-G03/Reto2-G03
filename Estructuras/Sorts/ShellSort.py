import lista as lst

def sort(lista):
    x = lst.pythonificar(lista)
    s = shell_Sort(x)
    y = lst.depythonificar(s)
    return y

def shell_Sort(lista):
    n = len(lista)
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            temp = lista[i]
            pos = i
            while pos >= gap and lista[pos-gap] > temp:
                lista[pos] = lista[pos-gap]
                pos -= gap
                lista[pos] = temp
        gap = gap//2
    return lista
