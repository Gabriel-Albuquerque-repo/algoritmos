def merge_sort(lista):

    if len(lista) <= 1:  # Base da recursão

        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    #  Os dois if's são a base da recursão
    if not lado_esquerdo:  # Vai executar quando lado_esquerdo for uma lista vazia
        
        return lado_direito  # Aqui é o return final

    if not lado_direito:

        return lado_esquerdo  # Aqui é o return final

    if lado_esquerdo[0] < lado_direito[0]:

        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


lista = [9, 6, 5, 8, 4]
print(len(lista))
print(merge_sort(lista))

