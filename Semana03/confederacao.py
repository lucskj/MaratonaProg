entrada = ["2 5", 
           "1 0 0 1", 
           "2 0 0 8", 
           "1 0 0", 
           "4 2 2", 
           "4 3 3", 
           "5 5 5", 
           "2 18 4"]

guia = entrada[0].split(" ")
n_planos = int(guia[0])
n_planetas = int(guia[1])

i = 1
while i <= n_planos:
    eq_plano = entrada[i].split(" ")
    A = int(eq_plano[0])
    B = int(eq_plano[1])
    C = int(eq_plano[2])
    D = int(eq_plano[3])

    entrada[i] = 0

    j = n_planos + 1
    while j <= n_planos + n_planetas:
        eq_planeta = entrada[j].split(" ")
        X = int(eq_planeta[0])
        Y = int(eq_planeta[1])
        Z = int(eq_planeta[2])

        if A*X + B*Y + C*Z == D:
            entrada[i] = entrada[i] + 1

        j += 1

    i += 1

maior = 0
l = 1
while l <= n_planos:
    if entrada[l] > maior:
        maior = entrada[l]

    l += 1

print(maior)
