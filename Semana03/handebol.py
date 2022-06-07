N = 5
M = 3
lista = [[0, 0, 0], 
         [1, 1, 5], 
         [0, 0, 0], 
         [1, 1, 2], 
         [1, 1, 2]]

def check():
    if 1 <= N <= 100 and 1 <= M <= 100:
        return True
    else:
        return False

def build_matrix(nova_matrix):
    i = 0
    while i < N:
        flag = True
        for x in lista[i]:
            if x == 0:
                flag = False
                break
        if flag:
            nova_matrix += 1
        i += 1
    return nova_matrix

bool = check()
if bool:
    nova_matrix = build_matrix(0)
    print(nova_matrix)
else:
    print("Valores inválidos") 
