def contagem_caracteres(s):
    """
    >>> contagem_caracteres('sergio')
    {'e': 1, 'g': 1, 'i': 1, 'o': 1, 'r': 1, 's': 1}

    >>> contagem_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    """

    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        print(contagem)
        contagem += 1
        print(contagem)
        resultado[caracter] = contagem
        print(resultado)
    return resultado


if __name__ == '__main__':
    print(contagem_caracteres('sergio'))
    print()
    print(contagem_caracteres('banana'))
