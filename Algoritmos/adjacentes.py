numero = int(input("Digite um número inteiro:"))

contaAdjacentes = 0
while numero != 0:
    restoAnterior = numero % 10
    numero = numero // 10
    restoProximo = numero % 10
    if restoAnterior == restoProximo:
        contaAdjacentes += 1
        print("Adjacentes:",restoAnterior,restoProximo)
print("numero de adjancentes:",contaAdjacentes)