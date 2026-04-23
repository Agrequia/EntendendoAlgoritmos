#Hello World da tabela hash
caderno = dict()

caderno["maçã"] = 0.67
caderno["leite"] = 1.49
caderno["abacate"] = 1.49

print(caderno["abacate"])

#Lista telefonica
lista_telefonica = {}

lista_telefonica["Cintia"] = 49999498770
lista_telefonica["Eu"] = 49998087478
lista_telefonica["Farmacia"] = 4933234534
lista_telefonica["Policia"] = 190
lista_telefonica["Bombeiros"] = 193

print(lista_telefonica["Eu"])

#Eleitores na votação
eleitores = {}

def verificaEleitor(nome):
    if eleitores.get(nome):
        print(nome + " já votou, vá embora!")
    else:
        eleitores[nome] = True
        print(nome + " ainda não votou, pode ir votar!")

verificaEleitor("Arthur")
verificaEleitor("Cintia")
verificaEleitor("Heitor")
verificaEleitor("Arthur")