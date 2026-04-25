#Pseudocodigo para encontrar a maior subsequencia comum em duas palavras diferentes:
if palavraA[i] == palavraB[j]:                              # type: ignore
    celula[i][j] = celula[i-1][j-1] + 1                     # type: ignore
else:
    celula[i][j] = max(celula[i-1][j-1], celula[i][j-1])    # type: ignore
