entrada = [[11,9,2,3],
           [7,8,3,2],
           [10,15,3,7],
           [8,9,3,2],
           [0,0,0,0]]

def hip(n1, n2):
    return ((n1**2) + (n2**2))**0.5

x = 0
while(True):
    i = entrada[x]
    if i[0] == 0 and i[1] == 0 and i[2] == 0 and i[3] == 0:
        break
    else:
        if hip(i[0], i[1]) >= (hip(i[2], i[2]) + i[2] + hip(i[3], i[3]) + i[3]):
            print("S")
        else:
            print("N")
    x += 1
