# Docstring
#__doc__


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, palíndromo.

    Args:
        sentence (str): String a evaluar

    Returns:
        bool: True o False

    Examples:

    >>> palindromo('Anita lava la tina')
    True

    >>> sentence = 'Oso'
    >>> palindromo(sentence)
    True

    >>> palindromo('CodigoFacilito')
    False
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]
