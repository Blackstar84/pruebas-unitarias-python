def suma_numeros_positivos(n1: int, n2: int) -> int:
    """Permite sumar 2 números enteros positivos

    Args:
        n1 (int): 
        n2 (int): 

    Returns:
        int: 
    """
    #if n1 < 0 or n2 < 0:
        #return None
    assert n1 > 0 and n2 > 0, 'Lo sentimos, sólo es posible sumar números positivos'

    return n1 + n2

if __name__ == '__main__':
    resultado = suma_numeros_positivos(-10, 20)
    print(resultado)