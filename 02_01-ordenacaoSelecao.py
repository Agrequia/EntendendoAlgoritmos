#Função que retorna o indice do menor item de uma lista
def buscaMenor (lista: any):
    tamanho = len(lista)
    menor = lista[0]
    indiceMenor = 0
    for i in range(1,tamanho):
        if lista[i] < menor:
            menor = lista[i]
            indiceMenor = i
            i += 1
    return indiceMenor

#Função que ordena um array por seleção
def ordenacaoPorSelecao(lista: any):
    novaLista = []
    iteracoes = 0
    tamanho = len(lista)
    for i in range(tamanho):
        menor = buscaMenor(lista)
        novaLista.append(lista.pop(menor))
        iteracoes += 1
    print("N° de iterações: ", iteracoes)
    return novaLista


minhaLista = [45, 12, 89, 56, 71, 23, 94, 18, 62, 33, 77, 5, 41, 99, 28, 66, 10, 50, 82, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
print("Algoritmo de ordenação por seleção")
print(ordenacaoPorSelecao(minhaLista))