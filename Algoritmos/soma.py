numero = int(input("Digite um numero inteiro:"))
soma = 0
resto = 0
while numero != 0:
    resto = numero % 10
    numero = numero // 10
    soma += resto
print(soma)