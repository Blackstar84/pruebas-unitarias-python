"""Este es el doctstring del módulo Documentables
"""
# Docstring
#__doc__

class User:
    """Permite representar un usuario"""

    def __init__(self, username: str, pasword: str) -> None:
        """Permite instanciar un objeto de tipo user

        Args:
            username (_type_): El username del usuario.
            pasword (_type_): El password del usuario.
        """


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, palíndromo.

    Args:
        sentence (str): String a evaluar

    Returns:
        bool: True o False
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]
