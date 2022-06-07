n_atual = ""
nome_atual = ""
nota_atual = 0

n_pior = ""
nome_pior = ""
nota_pior = 0

lista = ["1;Spock;99", "2;McCoy;1", "3;Data;56", "4;Kor;1"]

cont = 0

for i in lista:
    cont = cont + 1

    lista1 = i.split(";")
    n_atual = lista1[0]
    nome_atual = lista1[1]
    nota_atual = int(lista1[2])

    if nota_atual < nota_pior or nota_pior == 0:
        n_pior = n_atual
        nome_pior = nome_atual
        nota_pior = nota_atual

    elif nota_atual == nota_pior:
        if nome_atual > nome_pior:
            n_pior = n_atual
            nome_pior = nome_atual
            nota_pior = nota_atual

    print("instância " + str(cont))
    print(nome_pior)

print("Pior aluno:")
print("N:" + n_pior + " Nome:" + nome_pior + " Nota:" +  str(nota_pior))
