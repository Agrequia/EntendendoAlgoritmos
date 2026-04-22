def pesquisaBinaria (lista: any, item:any):
    iteracao = 0
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio: int 
        meio = round((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            iteracao = iteracao + 1
            print("Iterações: ", iteracao)
            return meio #Posição na array
        if chute > item:
            iteracao = iteracao + 1
            alto = meio - 1
        else:
            iteracao = iteracao + 1
            baixo = meio +1
    return None

minhaLista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
print("Algoritmo de busca binaria")
valorDesejado = int(input("Insira o item que voce gostaria de saber a posição: "))
print(pesquisaBinaria(minhaLista, valorDesejado))