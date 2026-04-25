#o algoritmo dos k-vizinhos mais próximos consiste em, dado um conjunto de informações em um plano de n-dimensoes, 
#encontras os k-vizinhos mais proximos dentro desse plano para assim inferir onde este novo item se encaixa melhor
#essa distancia pode ser calculada pela distancia euclidiana ou tambem pela similaridade do cosseno. Abaixo temos
#um exemplo do calculo da distancia euclidiana entre dois pontos no plano da 5ª dimensão que foi solicitado no livro 
import math
distanciaPM = ((3-2)**2) + ((4-5)**2) + ((4-1)**2) + ((1-3)**2) + ((4-1)**2)
distanciaPM = math.sqrt(distanciaPM)
print(distanciaPM)