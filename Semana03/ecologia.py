M = 4
N = 8
matriz = [[1, 1, 1, 1],
          [9, 9, 9, 1],
          [9, 1, 9, 1],
          [9, 9, 9, 1]]
resultados = []

i = 0
while i < M:
    caminhos = []
    lista = []
    maior = 0
    j = 0
    while j < M:
        if matriz[i][j] > matriz[i][maior]:
            maior = j
        j += 1
    j = maior
    x = 0
    lista.append(matriz[i][j])
    caminhos.append([i, j])
    auxi = i
    auxj = j
    while x < N - 1:
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        maior1 = 0
        if auxi - 1 > -1 and [auxi - 1, auxj] not in caminhos:
            if matriz[auxi - 1][auxj] > maior1:
                maior1 = matriz[auxi - 1][auxj]
                flag1 = True
        if auxj - 1 > -1 and [auxi, auxj - 1] not in caminhos:
            if matriz[auxi][auxj - 1] > maior1:
                maior1 = matriz[auxi][auxj - 1]
                flag1 = False
                flag2 = True
        if auxi + 1 < M and [auxi + 1, auxj] not in caminhos:
            if matriz[auxi + 1][auxj] > maior1:
                maior1 = matriz[auxi + 1][auxj]
                flag1 = False
                flag2 = False
                flag3 = True
        if auxj + 1 < M and [auxi, auxj + 1] not in caminhos:
            if matriz[auxi][auxj + 1] > maior1:
                maior1 = matriz[auxi][auxj + 1]
                flag1 = False
                flag2 = False
                flag3 = False
                flag4 = True
        if flag1:
            auxi -= 1
        if flag2:
            auxj -= 1
        if flag3:
            auxi += 1
        if flag4:
            auxj += 1
        caminhos.append([auxi, auxj])
        lista.append(maior1)
        x += 1
    soma = 0
    for valor in lista:
        soma += valor

    i += 1
    resultados.append(soma)

maior2 = 0
for numero in resultados:
    if numero > maior2:
        maior2 = numero

print(maior2)
