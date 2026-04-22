#Exemplo de recursividade que gera um loop infinito (bug)
'''
def regressiva(i):
    print(i)
    regressiva(i-1)
'''
#Por conta disso a recursividade trata de dois casos o caso base (que encerra a recursao) e o caso recursivo (que mantem a função em recursao)
def regressiva(i):
    print(i)
    if i <= 0: #Caso base
        return
    else: #Caso recursivo
        regressiva(i-1)

regressiva(100)