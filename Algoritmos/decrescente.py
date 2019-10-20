anterior = int(input("Digite um primeiro valor inicial:"))

decrescente = True
valor = 1
while valor != 0 and decrescente:
    valor = int(input("Digite o valor da sequência:"))
    if anterior < valor:
        decrescente = False
    anterior = valor

if decrescente:
    print("Decrescente.")
else:
    print("Não decrescente.")