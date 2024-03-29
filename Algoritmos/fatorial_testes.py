def fatorial(numero):
    if numero < 0:
        return 0
    i = fat = 1
    while i <= numero:
        fat = fat * i
        i += 1
    return fat

def teste_fatorial0():
    assert fatorial(0) == 1

def teste_fatorial1():
    assert fatorial(1) == 1

def teste_fatorial_negativo():
    assert fatorial(-10) == 0

def teste_fatorial4():
    assert fatorial(4) == 24

def teste_fatorial5():
    assert fatorial(5) == 120
