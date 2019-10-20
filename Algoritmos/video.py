numero = int(input("Digite um numero inteiro:"))
restoAnterior = 0
restoProximo = 0
adjacente = False
while numero != 0:
    restoAnterior = numero % 10
    numero = numero // 10
    restoProximo = numero % 10
    if restoAnterior == restoProximo:
        adjacente = True
if adjacente:
    print("sim")
else:
    print("não")