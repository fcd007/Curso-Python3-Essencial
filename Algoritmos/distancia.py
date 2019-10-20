import math

x1 = int(input("Digite o valor de X1:"))
y1 = int(input("Digite o valor de Y1:"))
x2 = int(input("Digite o valor de X2:"))
y2 = int(input("Digite o valor de Y2:"))
distancia = int(math.sqrt(((x2*x2) - (x1*x1)) + ((y2*y2)-(y1*y1))))
if distancia >= 10:
    print("longe")
else:
    print("perto")
