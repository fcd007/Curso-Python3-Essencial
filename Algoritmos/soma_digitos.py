numero = int(input("Digite um número inteiro positivo:"))
resto = 0
divisao = 0
soma = 0
while numero != 0:
    resto = numero % 10
    soma +=resto
    numero = numero // 10
print("Resto:", resto,",divisão:",divisao,"soma:",soma)