class Ordenador:

    def selection_sort(self, lista):
        count_selec = 0
        
        for i in range(len(lista)): 
            posicao_do_minimo = i
            
            for j in range(i + 1, len(lista)):
            
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

                count_selec += 1

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        
        return lista         

    def bubble_sort(self, lista):
        count_bubble = 0
        fim = len(lista)

        for i in range(fim - 1, 0, -1):

            for j in range(i):

                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

                count_bubble += 1
        
        return lista

    def bubble_curto(self, lista):
        count_bubble_curto = 0
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            trocou = False
        
            for j in range(i):

                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

                    trocou = True
                    
                count_bubble_curto += 1
                
            if not trocou:  # Lembrar que "não Falso é Verdadeiro!

                return trocou

        return lista

    def insertion_sort(self, lista):
        n = len(lista)

        for i in range(1, n):

            chave = lista[i]
            j = i - 1
            
            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]

                j = j - 1

            lista[j + 1] = chave
            
        return lista


