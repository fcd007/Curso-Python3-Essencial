def fatorial(numero):
    fac = 1
    while numero > 1:
        if numero == 0:
            fac = 1
        else:
            fac = fac * numero
        numero -= 1
    return fac

def numero_binomial(valor_n, valor_p):
    binomial = 0
    if valor_n >= valor_p:
        while valor_p >= 0:
            binomial = fatorial(valor_n) // (fatorial((valor_n - valor_p)) * fatorial(valor_p))
            valor_p -= 1
            print(binomial)
        return binomial
    else:
        print("P < que N, valor inválido!")

numero_binomial(20,17)