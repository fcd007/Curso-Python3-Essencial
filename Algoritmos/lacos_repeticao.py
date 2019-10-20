contador = int(input("Quantas somas deseja?"))
valor = int(input("Digite um valor a ser somado:"))
soma = valor
contador -=1
while contador > 0 and valor != 0:
    contador -=1
    valor = int(input("Digite um valor a ser somado:"))
    soma += valor
print("A soma total:", soma)