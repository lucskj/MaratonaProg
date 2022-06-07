entrada = [["5", "50000"], 
           ["3","123456"], 
           ["9", "23454324543423"], 
           ["9", "99999999991999999"], 
           ["7", "777"], 
           ["0", "0"]]

j = 0
while(True):
    i = entrada[j]
    j += 1
    if i[0] == "0" and i[1] == "0":
        break
    aux = i[1].split(i[0])
    novo_numero = 0
    TemNumero = False
    IniciarVazios = True
    for x in aux:
        if x != "":
            novo_numero = novo_numero*10**(len(x)) + int(x)
            TemNumero = True
            IniciarVazios = True
        elif IniciarVazios:
            novo_numero = novo_numero*10
            IniciarVazios = False
    if TemNumero:
        print(novo_numero)
    else:
        print()
