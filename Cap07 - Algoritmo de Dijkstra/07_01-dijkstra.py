#Tabela hash de grafo:
grafo = {}

#Tabela hash de cada um dos vertices (inicio, a, b e fim):
grafo["inicio"] = {}
grafo["a"] = {}
grafo["b"] = {}
grafo["fim"] = {}

#Alimentando a tabela hash de cada um dos vertices com seus respectivos vizinhos e pesos (fim nao possui vizinho, por isso nao aparece neste trecho):
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 5

grafo["a"]["fim"] = 1

grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

#Para visualizar os vizinhos de um elemento:
print(grafo["inicio"].keys())
#Para visualizar o peso entre dois elementos:
print(grafo["inicio"]["a"])

#Tabela hash que armazena o custo entre o inicio e determinado vertice:
custo = {}

#definindo constante com custo infinito para caminhos ainda desconhecidos:
infinito = float("inf")

#Definindo os custos ja conhecidos partindo de inicio:
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

#Tabela hash para os pais (de que aresta se veio para obter o custo determinado acima):
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

#Array que registra os vértices ja processados (isso evita que eles sejam processados mais de uma vez em casos que há a possibilidade de acessa-los novamente):
processados = []

#Função que encontra o menor custo
def acheVerticeDeMenorCusto(custos):
    menorCusto = infinito
    verticeDeMenorCusto = None
    for vertice in custos:
        custo = custos[vertice]
        if custo < menorCusto and vertice not in processados:
            menorCusto = custo
            verticeDeMenorCusto = vertice
    return verticeDeMenorCusto

#Implementação do algoritmo:
vertice = acheVerticeDeMenorCusto(custos)

while vertice is not None:
    custos = custos[vertice]
    vizinhos = grafo[vertice]
    for i in vizinhos.keys():
        novoCusto = custo + vizinhos[i]
        if custos[i] > novoCusto:
            custos[i] = novoCusto
            pais[i] = vertice
    processados.append(vertice)
    vertice = acheVerticeDeMenorCusto(custos)