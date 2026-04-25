#Pseudocodigo para encontrar a maior substring comum em duas palavras diferentes:
if palavraA[i] == palavraB[j]:      # type: ignore
    celula[i][j] = celula[i-1][j-1] # type: ignore
else:
    celula[i][j] = 0                # type: ignore
