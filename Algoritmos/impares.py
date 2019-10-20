numero = int(input("Digite o valor de n:"))
contador = 0
impa = 0
while impa != numero:
    if contador % 2 != 0:
        print(contador)
        impa += 1
    contador += 1