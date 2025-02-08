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
    S1 = strassen(A11, (B12 - B22))
    S2 = strassen((A11 + A12), B22)
    S3 = strassen((A21 + A22), B11)
    S4 = strassen(A22, (B21 - B11))
    S5 = strassen((A11 + A22), (B11 + B22))
    S6 = strassen((A12 - A22), (B21 + B22))
    S7 = strassen((A11 - A21), (B11 + B12))

    # Combinar os resultados
    P11 = S5 + S4 - S2 + S6
    P12 = S1 + S2
    P21 = S3 + S4
    P22 = S5 + S1 - S3 - S7

    # Montar a matriz resultante
    P = np.zeros((n, n))
    P[:mid, :mid] = P11
    P[:mid, mid:] = P12
    P[mid:, :mid] = P21
    P[mid:, mid:] = P22

    return P

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