entrada = [289384, 930887, 692778, 636916, 747794, 238336, 885387, 760493, 516650, 641422]
saida = []

primos = [2]

i = 3

fim = entrada[len(entrada) - 1]

while i < fim:
    primo = True
    x = 0
    while primos[x]*primos[x] <= i:
        if i%primos[x] == 0:
            primo = False
            break

        x = x + 1

    if primo:
        primos.append(i)

    i = i + 1

for i in entrada:
    fatores = {1}
    for x in primos:
        while i%x == 0:
            if x == i:
                if not(x in fatores):
                    fatores.add(x)
                else:
                    break
            else:
                if not(x in fatores):
                    fatores.add(x)
                i = i/x

    i = len(fatores)-1
    saida.append(i)

cont = 0
while cont < len(saida):
    print(str(entrada[cont]) + "->" + str(saida[cont]))
    cont = cont + 1
