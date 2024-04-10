import Estructuras.Lista as lst

def sort(lt):
    def le(a,b):
        if a <= b:
            return True
        else:
            return False
    return csort(lt,le)

def csort(lt, crit):
    
    l = lst.iterator(lt)
    if lt["size"] == 1:
        return lt
    else:
        pivot = l['value']
        lesser = split_less(l, pivot, crit)
        greater = split_great(l,pivot, crit)
        return merge(csort(lesser, crit),csort(greater, crit))

def split_less(l, element, crit):
	def split_less_it(node, res, crit):
		if node == None:
			return res
		elif crit(node['value'], element):
			val = node["value"]
			next = node['next']
			lst.addfirst(res, val)
			return split_less_it(next, res, crit)
		else:
			return split_less_it(node['next'], res, crit)
	return split_less_it(l,lst.new_list(), crit)

def split_great(l, element, crit):
	def split_great_it(node, res, crit):
		if node == None:
			return res
		elif not crit(node['value'], element):
			val = node['value']
			next = node['next']
			lst.addlast(res, val)
			return split_great_it(next, res, crit)
		else:
			return split_great_it(node['next'], res, crit)
	return split_great_it(l,lst.new_list(), crit)

def merge(l1, l2):
	return lst.append(l1, l2)

