import numpy as np

caixinha = np.array([1, 2, 3, 4, 5])
print("Array do Numpy")
print(caixinha)

print('\nAray multiplicando')
print(caixinha * 2)

caixinha_dois = np.array([10, 20, 30, 40, 50])
print('\nSomar duas arrays')
print(caixinha + caixinha_dois)

#criando uma matriz 2d
matriz = np.array([ [1, 2, 3],[4, 5, 6] ])
print('\nMatriz de 2x3:')
print(matriz)

print ('\n Soma de matriz')
print(np.sum(matriz))

print('\n Média dos elementos da matriz')
print(np.mean(matriz)) # temos tambem a median

print('\nMatriz transposta:')
print(matriz.T)

#gerar uma matriz com valores aleatorios
print('\nmatriz aleatoria')
print(np.random.rand(3,3))

