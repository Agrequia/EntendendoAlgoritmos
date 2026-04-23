from collections import deque

def pessoa_vendedora(nome):
    return nome[-1] == 'm'

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

def pesquisa(pessoa):

    filaPesquisa = deque()
    filaPesquisa += grafo[pessoa]
    verificadas = []
    while filaPesquisa:
        nome = filaPesquisa.popleft()
        if not nome in verificadas:
            if pessoa_vendedora(nome):
                print(nome + ' vende manga!')
                return True
            else:
                print(nome + ' não vende manga')
                filaPesquisa += grafo[nome]
                verificadas.append(nome)
    return False

pesquisa("voce")