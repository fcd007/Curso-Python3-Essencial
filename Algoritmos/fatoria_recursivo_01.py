def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''
    if k == 0:
        k_fat = 1
    else:
        k_fat = k * fatorial(k - 1)

    return k_fat


# testes
print("0! =", fatorial(0))
print("1! =", fatorial(1))
print("5! =", fatorial(5))
print("6! =", fatorial(6))

