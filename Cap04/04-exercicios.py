def somaArray(lista):
    total = 0
    for x in lista:
        total += x
    return total

#4.1
def somaArrayRecursiva(lista):
    if lista == []:
        return 0
    return lista[0] + somaArrayRecursiva(lista[1:])

#4.2
def tamanhoArrayRecursivo(lista):
    if lista == []:
        return 0
    return 1 + tamanhoArrayRecursivo(lista[1:])

#4.3
def maiorValorArrayRecursivo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maiorValorArrayRecursivo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

'''
4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é
um algoritmo do tipo dividir para conquistar. Você consegue
determinar o caso-base e o caso recursivo para a pesquisa
binária?

R: Para a pesquisa binaria o caso base é quando o valor encontrado na lista é igual ao valor procurado enquanto que o caso recursivo é quando recursivo é quando o 
valor encontrado em determinada iteração e diferente (maior ou menor) do valor buscado

Quanto tempo levaria, em notação Big O, para completar cada uma
destas operações?
4.5 Imprimir o valor de cada elemento em um array.

R: O(n)

4.6 Duplicar o valor de cada elemento em um array.

R: O(n)

4.7 Duplicar o valor apenas do primeiro elemento do array.

R: O(1)

4.8 Criar uma tabela de multiplicação com todos os elementos do
array. Assim, caso o seu array seja [2, 3, 7, 8, 10], você primeiro
multiplicará cada elemento por 2. Depois, multiplicará cada
elemento por 3 e então por 7, e assim por diante.

R: O(n²)

'''

lista = [1, 2, 3, 24, 4, 10, 15]
print(somaArray(lista))
print(somaArrayRecursiva(lista))
print(tamanhoArrayRecursivo(lista))
print(maiorValorArrayRecursivo(lista))