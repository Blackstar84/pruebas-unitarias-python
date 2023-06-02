def suma(numero1: int, numero2: int) -> int:
    """Permite sumar 2 números enteros

    Args:
        numero1 (int): _description_
        numero2 (int): _description_

    Returns:
        int: _description_
    """
    
    print('Entramos aquí!!!!')
    
    resultado = numero1 + numero2
    
    print('Nos encontramos en esta línea')
    
    return resultado


if __name__ == '__main__':
    print('Antes del llamado de la función')
    
    resultado = suma(15, 20)
    
    print(resultado)