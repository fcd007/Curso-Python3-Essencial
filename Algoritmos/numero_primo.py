numero = int(input("Digite um numero inteiro:"))
contador = 2
while numero % contador != 0 and contador <= numero:
    contador += 1
if contador == numero:
    print("primo")
else:
    print("nao primo")