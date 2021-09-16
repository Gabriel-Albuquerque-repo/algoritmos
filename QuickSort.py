def quick_sort(lista, inicio = 0, fim = None):

    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        p = partition(lista, inicio, fim)

        quick_sort(lista, inicio, p - 1)
        quick_sort(lista, p + 1, fim)

    return lista

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio

    for j in range(inicio, fim):

        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]

            i = i + 1

    lista[i], lista[fim] = lista[fim], lista[i]

    return i

'''already_sorted = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]

a = [2,0, 4, -15, 1]

repeated = [7,7,7,7,7,7,7,1,99,0,1,1,1]

#print(quick_sort(already_sorted))
print(quick_sort(a))
print(quick_sort(repeated))'''

