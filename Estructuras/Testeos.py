import lista as lst
import BucketSort as buk


def lista(lt):
    lista = {'numero': None}
    lista['numero'] = lst.new_list()
    
    for i in (lt):
        lst.addlast(lista['numero'], i)
    
    return lista

lt = [3, 5, 7, 1, 9, 2, 6, 4, 8, 10]
a = lista(lt)
x = (buk.sort(a['numero']))
print(x)
print('aaaa')
