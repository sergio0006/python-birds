def contagem_caracteres(s):
    """
    >>> contagem_caracteres('sergio')
    e: 1
    g: 1
    i: 1
    o: 1
    r: 1
    s: 1

    >>> contagem_caracteres('banana')
    a: 3
    b: 1
    n: 2

    """

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contagem_caracteres('sergio')
    print()
    contagem_caracteres('banana')
