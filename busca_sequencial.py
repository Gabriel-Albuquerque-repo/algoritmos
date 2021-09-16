def ordenada(lista):

    if len(lista) == 1:

        return True
    
    for i in range(len(lista) - 1):

        if lista[i] > lista[i + 1]:

            return False

        else:

            return True


def busca(lista, elemento):

    for i in range(len(lista)):

        if lista[i] == elemento:

            return i

    return False

