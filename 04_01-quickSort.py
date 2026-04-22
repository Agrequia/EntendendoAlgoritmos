import random

def quickSort(array):
    if len(array) < 2:
        return array
    #pivo = array[0] #A escolha de um pivo aleatório reduz o tempo de execução na notação Big O de (n²) para O(n*log n)
    indice = random.randint(0, (len(array)-1))
    pivo = array[indice]
    maiores = [i for i in (array[:indice] + array[indice + 1:]) if i >= pivo]
    menores = [i for i in (array[:indice] + array[indice + 1:]) if i < pivo]
    return  quickSort(menores) + [pivo] + quickSort(maiores)

lista = [11, 5, 14, 9, 1, 10, 6, 3, 13, 7, 4, 15, 8, 2, 12, 0]
print(quickSort(lista))