def primos(numero):
    if numero < 2 : return []
    if numero == 2: return [2]

    numeros = range(3,numero + 1,2)
    numeros_tamanho = (numero // 2) - 1 + (numero % 2)
    contador = 0
    contador_primo_num = (int(numero ** 0.5)- 3) // 2
    while contador <= contador_primo_num:
        numero_at_conta = (contador << 1) + 3
        for j in range(contador * (numero_at_conta + 3) + 3, numeros_tamanho, numero_at_conta):
            numeros[j] = 0
        contador += 1
        while contador <= contador_primo_num:
            if numeros[j] != 0:
                break
            contador += 1
        return [2] + [x for x in numeros if x != 0]

def meu_primos(limite):
    lista_de_primos = primos(limite)
    print("Primos:", " ".join(str(x) for x in lista_de_primos))
    print("\n\nForam encontrados %d números primos." % len(lista_de_primos))