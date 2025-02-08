import numpy as np

def strassen(A, B):
    
    # Caso base: se a matriz for 1x1, multiplicamos diretamente
    n = len(A)
    if n == 1:
        return A * B

    # Dividir as matrizes em submatrizes
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Calcular os produtos intermediários de Strassen
    P1 = strassen(A11, (B12 - B22))
    P2 = strassen((A11 + A12), B22)
    P3 = strassen((A21 + A22), B11)
    P4 = strassen(A22, (B21 - B11))
    P5 = strassen((A11 + A22), (B11 + B22))
    P6 = strassen((A12 - A22), (B21 + B22))
    P7 = strassen((A11 - A21), (B11 + B12))

    # Combinar os resultados
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    # Montar a matriz resultante
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

# Exemplo de uso
A = np.array([[1, 2, 3, 4],
              [7, 8, 9, 10],
              [5, 2, 4, 3],
              [1, 1, 2, 7]])

B = np.array([[8, 10, 8, 10],
              [2, 2, 3, 1],
              [4, 7, 11, 9],
              [6, 5, 4, 3]])

C = strassen(A, B)
print("Resultado da multiplicação:")
print(C)