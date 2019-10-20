valor = int(input("Digite o valor de n:"))
fac = 1
while valor > 1:
    if valor == 0:
        fac = 1
    else:
        fac = fac *valor
        valor -= 1
print(fac)