# <p align="center">Algoritmo de Strassen</p>

<h3 align="center">Projeto de Análise e Algoritmos</h3>

<p align="center">
  O algoritmo de Strassen é um algoritmo de multiplicação de matrizes quadradas que é mais eficiente que o método tradicional de multiplicação de matrizes.
</p>

$$
Multi\_{Traditional} = O(n^3)
$$

$$
Multi\_{Strassen} = O(n^{log_2(7)}) \approx O(n^{2.81})
$$

<p align="center">
  Para o algoritmo funcionar, ele faz a divisão da matriz em 4 submatrizes de tamanho n/2 x n/2 e realiza 7 multiplicações de matrizes de tamanho n/2 x n/2, ao invés de 8 multiplicações de matrizes de tamanho n/2 x n/2. Se a matriz não for quadrada, ele completa a matriz com zeros para que ela seja quadrada.
</p>

$$
A = \begin{bmatrix} 
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}

B = \begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}

C = \begin{bmatrix}
c_{11} & c_{12} \\
c_{21} & c_{22}
\end{bmatrix}
$$

<p align="center">
    O algoritmo de Strassen é definido pelas seguintes equações, contabilizando 11, sendo 7 para definir os valores de S1, S2, S3, S4, S5, S6 e S7 e 4 para definir os valores de P1, P2, P3 e P4, sendo P o resultado da multiplicação de matrizes.
</p>

$$
S1 = A_{11} (B_{12} - B_{22})
$$

$$
S2 = (A_{11} + A_{12}) B_{22}
$$

$$
S3 = (A_{21} + A_{22}) B_{11}
$$

$$
S4 = A_{22} (B_{21} - B_{11})
$$

$$
S5 = (A_{11} + A_{22}) (B_{11} + B_{22})
$$

$$
S6 = (A_{12} - A_{22}) (B_{21} + B_{22})
$$

$$
S7 = (A_{11} - A_{21}) (B_{11} + B_{12})
$$

<br>

$$
P1 = S5 + S4 - S2 + S6
$$

$$
P2 = S1 + S2
$$

$$
P3 = S3 + S4
$$

$$
P4 = S5 + S1 - S3 - S7
$$


<h4 align="center">Execução</h4>

<p align="center">
  Para executar o algoritmo, basta rodar o comando abaixo. Dentro do código, é possível alterar o tamanho da matriz e os valores das matrizes A e B, sendo utilizado o numpy para gerar as matrizes.
</p>

```bash
python3 Strassen.py
```
